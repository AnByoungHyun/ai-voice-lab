# 1단계: 환경 설정

## 학습 목표

이 단계를 마치면 다음을 할 수 있습니다:

- Python 가상환경을 생성하고 활성화할 수 있다
- Coqui TTS와 XTTS v2 모델을 설치하고 동작을 확인할 수 있다
- Apple Silicon(MPS) 환경에서의 PyTorch 설정을 이해한다
- 의존성 충돌 발생 시 트러블슈팅 방법을 알 수 있다

**예상 소요 시간:** 30~60분  
**난이도:** ★★☆☆☆ (초급)

## 사전 지식

- 터미널(CLI) 기본 사용법
- Python 패키지 관리자(pip) 개념
- 가상환경(venv)의 역할에 대한 이해

## 핵심 용어

| 용어 | 설명 |
|------|------|
| **XTTS v2** | Coqui AI가 개발한 다국어 음성 클로닝 모델. 짧은 음성 샘플(6초)만으로 화자의 목소리를 복제할 수 있다 |
| **Coqui TTS** | 오픈소스 TTS(Text-to-Speech) 엔진. XTTS v2를 포함한 다양한 TTS 모델을 제공한다 |
| **MPS** | Metal Performance Shaders. Apple Silicon GPU를 PyTorch에서 활용하기 위한 백엔드 |
| **torchcodec** | PyTorch 2.9+에서 오디오/비디오 인코딩·디코딩을 처리하는 라이브러리 |
| **venv** | Python 내장 가상환경 도구. 프로젝트별로 독립된 패키지 환경을 만들어준다 |

> 전체 용어집은 [00-glossary.md](./00-glossary.md)를 참고하세요.

## 시스템 요구사항

- Apple Silicon (M1/M2/M3/M4/M5) 또는 CUDA GPU
- RAM 16GB 이상 권장 (128GB면 최상)
- macOS 또는 Linux
- Python 3.12+

## 설치

### 1. Python 환경 설정

```bash
cd ~/workspaces/ai-voice-lab

# 가상환경 생성 (Python 3.12 권장)
python3 -m venv .venv
source .venv/bin/activate

# pip 업그레이드
pip install --upgrade pip
```

### 2. 패키지 설치

```bash
# requirements.txt로 일괄 설치
pip install -r requirements.txt
```

또는 수동 설치:

```bash
# Coqui TTS + torchcodec (PyTorch 2.9+ 필수)
pip install 'coqui-tts[codec]'

# transformers 호환 버전 (5.x는 coqui-tts와 비호환)
pip install 'transformers>=4.43,<5.0'
```

### 3. 설치 확인

```bash
# TTS CLI 동작 확인
tts --list_models | grep xtts
```

정상 설치 시 아래 출력이 나타남:

```
  1: tts_models/multilingual/multi-dataset/xtts_v2
  2: tts_models/multilingual/multi-dataset/xtts_v1.1
```

### 4. 빠른 TTS 테스트

> **참고:** 음성 클로닝에는 레퍼런스 음성 파일이 필요합니다.
> 아직 녹음을 하지 않았다면 아래 **방법 A**(내장 화자)로 설치 확인만 먼저 진행하세요.
> 본인 음성으로 클로닝하는 것은 [2단계: 녹음 가이드](./02-recording.md)에서 다룹니다.

**방법 A — 내장 화자로 테스트 (레퍼런스 음성 불필요)**

```bash
tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
    --text "Hello, this is a test." \
    --speaker_idx "Claribel Dervla" \
    --language_idx en \
    --out_path output_test.wav
```

**방법 B — 본인 음성으로 클로닝 테스트 (2단계 이후)**

```bash
tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
    --text "Hello, this is a test." \
    --speaker_wav samples/your_voice.wav \
    --language_idx en \
    --out_path output_test.wav
```

정상 실행 시 `output_test.wav` 파일이 생성됩니다. 오디오 플레이어로 재생하여 결과를 확인하세요.

## 주요 설치 패키지 버전 (검증 완료)

| 패키지 | 버전 | 비고 |
|--------|------|------|
| coqui-tts | 0.27.5 | TTS 엔진 |
| torch | 2.10.0 | MPS(Apple Silicon) 지원 |
| torchaudio | 2.10.0 | 오디오 처리 |
| torchcodec | 0.10.0 | PyTorch 2.9+ 오디오 IO |
| transformers | 4.57.6 | 5.x 비호환 주의 |
| librosa | 0.11.0 | 오디오 분석 |

## 트러블슈팅

### `isin_mps_friendly` ImportError

`transformers` 5.x에서 발생. 해결:

```bash
pip install 'transformers>=4.43,<5.0'
```

### `torchcodec` 미설치 에러

PyTorch 2.9+부터 torchcodec이 필수. 해결:

```bash
pip install 'coqui-tts[codec]'
```

## 다음 단계

→ [02-recording.md](./02-recording.md)
