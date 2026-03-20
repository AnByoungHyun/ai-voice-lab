#!/usr/bin/env python3
"""XTTS v2 음성 클로닝 스크립트.

레퍼런스 음성 파일을 기반으로 텍스트를 음성으로 변환합니다.

사용법:
    python scripts/clone_voice.py --text "안녕하세요" --speaker_wav samples/voice_ref_01_24k.wav
    python scripts/clone_voice.py --text "Hello world" --language en --speaker_wav samples/voice_ref_01_24k.wav
    python scripts/clone_voice.py --text "안녕하세요" --speaker_wav samples/voice_ref_01_24k.wav --output output/result.wav
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import torch

# 프로젝트 루트 기준 기본 경로
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_SPEAKER_WAV = PROJECT_ROOT / "samples" / "voice_ref_01_24k.wav"
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"


def parse_args() -> argparse.Namespace:
    """커맨드라인 인자를 파싱한다."""
    parser = argparse.ArgumentParser(
        description="XTTS v2 음성 클로닝 스크립트",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  # 한국어 합성 (기본)
  python scripts/clone_voice.py --text "안녕하세요, 반갑습니다."

  # 영어 합성
  python scripts/clone_voice.py --text "Hello, nice to meet you." --language en

  # 커스텀 레퍼런스 음성 사용
  python scripts/clone_voice.py --text "테스트입니다." --speaker_wav samples/my_voice.wav

  # 출력 파일 지정
  python scripts/clone_voice.py --text "안녕하세요." --output output/greeting.wav
        """,
    )
    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="합성할 텍스트",
    )
    parser.add_argument(
        "--speaker_wav",
        type=str,
        default=str(DEFAULT_SPEAKER_WAV),
        help=f"레퍼런스 음성 파일 경로 (기본: {DEFAULT_SPEAKER_WAV.relative_to(PROJECT_ROOT)})",
    )
    parser.add_argument(
        "--language",
        type=str,
        default="ko",
        choices=["ko", "en", "ja", "zh-cn", "de", "fr", "es", "pt", "pl", "tr", "ru",
                 "nl", "cs", "ar", "hu", "hi"],
        help="합성 언어 코드 (기본: ko)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="출력 파일 경로 (기본: output/clone_YYYYMMDD_HHMMSS.wav)",
    )
    parser.add_argument(
        "--use-gpu",
        action="store_true",
        default=False,
        help="GPU(MPS/CUDA) 사용 여부 (기본: CPU)",
    )
    return parser.parse_args()


def generate_output_path(output_dir: Path) -> Path:
    """타임스탬프 기반 출력 파일 경로를 생성한다."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return output_dir / f"clone_{timestamp}.wav"


def validate_speaker_wav(path: Path) -> None:
    """레퍼런스 음성 파일 존재 여부를 확인한다."""
    if not path.exists():
        print(f"[오류] 레퍼런스 음성 파일을 찾을 수 없습니다: {path}")
        print()
        print("해결 방법:")
        print("  1. docs/02-recording.md를 참고하여 음성을 녹음하세요.")
        print("  2. --speaker_wav 옵션으로 다른 파일 경로를 지정하세요.")
        sys.exit(1)

    if path.stat().st_size < 1000:
        print(f"[경고] 레퍼런스 음성 파일이 너무 작습니다: {path} ({path.stat().st_size} bytes)")
        print("  최소 6초 이상의 음성이 필요합니다.")


def clone_voice(
    text: str,
    speaker_wav: str | Path,
    language: str = "ko",
    output_path: str | Path = "output.wav",
    use_gpu: bool = False,
) -> Path:
    """XTTS v2를 사용하여 음성을 클로닝한다.

    Args:
        text: 합성할 텍스트
        speaker_wav: 레퍼런스 음성 파일 경로
        language: 합성 언어 코드
        output_path: 출력 파일 경로
        use_gpu: GPU 사용 여부

    Returns:
        생성된 음성 파일 경로
    """
    from TTS.api import TTS

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] 모델 로딩 중: {MODEL_NAME}")
    print(f"      GPU 사용 요청: {'예 (MPS/CUDA)' if use_gpu else '아니오 (CPU)'}")
    start = time.time()

    # Coqui TTS의 gpu=True는 macOS(MPS)에서 실패할 수 있어 항상 CPU로 안전 로드한다.
    # 이후 아래 분기에서 실행 디바이스를 명시적으로 선택해, CPU/CUDA/MPS를 동일한 방식으로 제어한다.
    tts = TTS(model_name=MODEL_NAME, gpu=False)
    device = "cpu"
    if use_gpu:
        # 우선순위:
        # 1) CUDA (NVIDIA 환경)
        # 2) MPS (Apple Silicon 환경)
        # 3) 둘 다 없으면 CPU 폴백
        #
        # 필요 시 정책 변경 가능:
        # - CPU 고정: `--use-gpu` 미사용
        # - CUDA 우선 대신 MPS 우선: 아래 if/elif 순서 변경
        if torch.cuda.is_available():
            device = "cuda"
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            print("[경고] 사용 가능한 GPU(CUDA/MPS)가 없어 CPU로 실행합니다.")

    # 최종 선택된 디바이스로 모델을 이동한다.
    # (cpu/cuda/mps 모두 동일 API)
    tts.to(device)

    load_time = time.time() - start
    print(f"      모델 로딩 완료 ({load_time:.1f}초)")
    print(f"      실행 디바이스: {device}")

    print(f"[2/3] 음성 합성 중...")
    print(f"      텍스트: \"{text}\"")
    print(f"      언어: {language}")
    print(f"      레퍼런스: {speaker_wav}")
    start = time.time()

    tts.tts_to_file(
        text=text,
        speaker_wav=str(speaker_wav),
        language=language,
        file_path=str(output_path),
    )

    synth_time = time.time() - start
    print(f"      합성 완료 ({synth_time:.1f}초)")

    file_size = output_path.stat().st_size
    print(f"[3/3] 출력 파일: {output_path} ({file_size / 1024:.1f} KB)")

    return output_path


def main() -> None:
    """메인 함수."""
    args = parse_args()

    speaker_wav = Path(args.speaker_wav)
    validate_speaker_wav(speaker_wav)

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = generate_output_path(DEFAULT_OUTPUT_DIR)

    print("=" * 60)
    print("XTTS v2 음성 클로닝")
    print("=" * 60)

    result_path = clone_voice(
        text=args.text,
        speaker_wav=speaker_wav,
        language=args.language,
        output_path=output_path,
        use_gpu=args.use_gpu,
    )

    print()
    print("=" * 60)
    print(f"완료! 재생: open {result_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
