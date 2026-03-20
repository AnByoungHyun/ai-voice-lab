# 3단계: XTTS v2 음성 클로닝

## 학습 목표

이 단계를 마치면 다음을 할 수 있습니다:

- XTTS v2 모델로 레퍼런스 음성 기반 TTS를 실행할 수 있다
- CLI와 Python API 두 가지 방식으로 음성 클로닝을 수행할 수 있다
- 한국어/영어 텍스트를 본인 목소리로 합성할 수 있다
- 합성 결과의 품질을 평가하고 개선 방향을 판단할 수 있다

**예상 소요 시간:** 30~60분 (첫 모델 다운로드 포함)
**난이도:** ★★★☆☆ (중급)

## 사전 지식

- [1단계: 환경 설정](./01-setup.md) 완료
- [2단계: 음성 녹음](./02-recording.md) 완료 → `samples/` 디렉토리에 레퍼런스 음성 준비
- Python 기본 문법 (함수 호출, 변수 할당)

## 핵심 용어

| 용어 | 설명 |
|------|------|
| **Voice Cloning** | 레퍼런스 음성의 특성을 학습하여 새로운 텍스트를 해당 목소리로 합성하는 기술 |
| **Zero-shot Cloning** | 사전 학습 없이 짧은 레퍼런스 음성만으로 클로닝하는 방식. XTTS v2의 기본 모드 |
| **Speaker Embedding** | 화자의 음성 특성을 벡터로 압축한 표현. 모델이 내부적으로 생성 |
| **Inference** | 학습된 모델을 사용하여 결과를 생성하는 과정 (= 추론) |

> 전체 용어집은 [00-glossary.md](./00-glossary.md)를 참고하세요.

## 동작 원리

```
레퍼런스 음성 (.wav)  ──┐
                        ├──→  XTTS v2 모델  ──→  합성 음성 (.wav)
입력 텍스트 + 언어코드  ──┘
```

XTTS v2는 **zero-shot 클로닝** 모델입니다:
1. 레퍼런스 음성에서 **화자 특성**(음색, 억양, 속도)을 추출
2. 입력 텍스트를 해당 화자 스타일로 합성
3. 별도의 학습(fine-tuning) 없이 즉시 결과 생성

**지원 언어:** 한국어(ko), 영어(en), 일본어(ja), 중국어(zh-cn) 등 17개 언어

## 방법 1: CLI로 클로닝

가장 빠르게 시작하는 방법입니다. 터미널에서 바로 실행할 수 있습니다.

### 한국어 합성

```bash
cd ~/workspaces/ai-voice-lab
source .venv/bin/activate

tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
    --text "안녕하세요, AI Voice Lab 음성 클로닝 테스트입니다." \
    --speaker_wav samples/voice_ref_01_24k.wav \
    --language_idx ko \
    --out_path output/clone_ko_test.wav
```

### 영어 합성

```bash
tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
    --text "Hello, this is a voice cloning test from AI Voice Lab." \
    --speaker_wav samples/voice_ref_01_24k.wav \
    --language_idx en \
    --out_path output/clone_en_test.wav
```

> **첫 실행 시** 모델이 자동 다운로드됩니다 (~1.8GB). 인터넷 속도에 따라 수 분이 소요될 수 있습니다.

### 결과 확인

```bash
# macOS에서 바로 재생
open output/clone_ko_test.wav

# 파일 정보 확인
ffprobe -hide_banner output/clone_ko_test.wav
```

## 방법 2: Python API로 클로닝

프로젝트에 포함된 `scripts/clone_voice.py` 스크립트를 사용하면 더 유연하게 제어할 수 있습니다.

### 기본 사용법

```bash
cd ~/workspaces/ai-voice-lab
source .venv/bin/activate

# 한국어 합성 (기본)
python scripts/clone_voice.py \
    --text "안녕하세요, 반갑습니다." \
    --speaker_wav samples/voice_ref_01_24k.wav

# 영어 합성
python scripts/clone_voice.py \
    --text "Hello, nice to meet you." \
    --language en \
    --speaker_wav samples/voice_ref_01_24k.wav

# 출력 파일 지정
python scripts/clone_voice.py \
    --text "테스트입니다." \
    --speaker_wav samples/voice_ref_01_24k.wav \
    --output output/my_greeting.wav

# GPU(MPS) 사용
python scripts/clone_voice.py \
    --text "GPU로 합성합니다." \
    --speaker_wav samples/voice_ref_01_24k.wav \
    --use-gpu
```

### Python 코드에서 직접 사용

스크립트를 사용하지 않고 Python에서 직접 TTS API를 호출할 수도 있습니다.

```python
from TTS.api import TTS
import torch

# 모델 로딩 (첫 실행 시 다운로드)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# 실행 디바이스 선택 (CPU / CUDA / MPS)
device = "cpu"
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
tts.to(device)

# 한국어 음성 합성
tts.tts_to_file(
    text="안녕하세요, AI Voice Lab입니다.",
    speaker_wav="samples/voice_ref_01_24k.wav",
    language="ko",
    file_path="output/result_ko.wav",
)

# 영어 음성 합성 (같은 레퍼런스 음성)
tts.tts_to_file(
    text="Hello, this is AI Voice Lab.",
    speaker_wav="samples/voice_ref_01_24k.wav",
    language="en",
    file_path="output/result_en.wav",
)

print("합성 완료!")
```

> **참고:** 프로젝트의 `scripts/clone_voice.py`는 `--use-gpu` 옵션 사용 시 실행 환경을 확인해 `CUDA` 또는 `MPS`를 자동 선택합니다.
> GPU를 사용하지 않으려면 `--use-gpu`를 빼고 실행하면 됩니다(CPU 고정).
> Python API를 직접 쓸 때는 `gpu=False`로 모델을 로드한 뒤 `tts.to("cuda")` 또는 `tts.to("mps")`로 디바이스를 이동하세요.

## CPU vs GPU(MPS) 비교

| 항목 | CPU (`--use-gpu` 미사용) | MPS (`--use-gpu` 사용) |
|------|-------------------|-------------------|
| 합성 속도 | 느림 (문장당 10~30초) | 빠름 (문장당 2~8초) |
| 메모리 사용 | 낮음 (~2GB) | 높음 (~4GB) |
| 안정성 | 높음 | MPS 관련 오류 가능 |
| 권장 상황 | 첫 테스트, 디버깅 | 반복 합성, 긴 텍스트 |

> **팁:** 처음에는 CPU로 정상 동작을 확인한 뒤, GPU로 전환하세요.

## 합성 결과 품질 평가

### 체크리스트

- [ ] 합성된 음성이 레퍼런스 음성과 비슷한 음색인가?
- [ ] 발음이 명확하게 들리는가? (특히 한국어 받침)
- [ ] 속도와 억양이 자연스러운가?
- [ ] 잡음이나 끊김이 없는가?
- [ ] 문장 끝이 자연스럽게 마무리되는가?

### 품질 개선 팁

| 문제 | 원인 | 해결 방법 |
|------|------|-----------|
| 음색이 다르게 들림 | 레퍼런스 음성 품질 부족 | 2단계로 돌아가 재녹음 (15초+ 권장) |
| 발음이 뭉개짐 | 텍스트가 너무 길거나 복잡 | 짧은 문장으로 나누어 합성 |
| 잡음이 들림 | 레퍼런스 음성에 잡음 포함 | 조용한 환경에서 재녹음 |
| 속도가 부자연스러움 | 레퍼런스와 합성 언어가 다름 | 동일 언어로 합성 테스트 |
| 끊김/반복 | 긴 텍스트 합성 시 발생 | `split_sentences=True` 유지 (기본값) |

## 실험해보기

기본 클로닝이 성공했다면, 아래를 시도해보세요:

### 1. 다양한 텍스트 길이 비교

```bash
# 짧은 문장
python scripts/clone_voice.py --text "안녕하세요." --speaker_wav samples/voice_ref_01_24k.wav

# 긴 문장
python scripts/clone_voice.py --text "오늘은 AI 음성 클로닝 기술을 실습하고 있습니다. 이 기술은 짧은 음성 샘플만으로도 자연스러운 음성을 합성할 수 있어서 다양한 분야에서 활용되고 있습니다." --speaker_wav samples/voice_ref_01_24k.wav
```

### 2. 한국어 vs 영어 비교

같은 레퍼런스 음성으로 한국어와 영어를 비교해보세요. XTTS v2는 다국어 모델이므로 한 음성으로 여러 언어를 합성할 수 있습니다.

### 3. 여러 레퍼런스 음성 비교

`samples/` 디렉토리에 여러 음성 파일이 있다면, 각각으로 합성하여 어떤 레퍼런스가 가장 좋은 결과를 내는지 비교해보세요.

## 산출물

이 단계를 완료하면 다음 파일이 생성됩니다:

- `output/clone_ko_test.wav` — 한국어 합성 결과
- `output/clone_en_test.wav` — 영어 합성 결과 (선택)

> `output/` 디렉토리는 `.gitignore`에 추가하는 것을 권장합니다.

## 트러블슈팅

### 모델 다운로드 실패

```
Connection error / Timeout
```

- 인터넷 연결 확인
- 재실행하면 이어받기(resume) 됨
- 모델은 `~/.local/share/tts/` 에 캐시됨

### MPS 관련 에러

```
RuntimeError: MPS backend error
```

- 스크립트 사용 시: `--use-gpu` 옵션을 제거하여 CPU 모드로 전환
- Python API 사용 시: `gpu=False`로 로드하고 `tts.to("cpu")`로 실행
- PyTorch 버전 확인: `python -c "import torch; print(torch.__version__)"`
- 최소 PyTorch 2.10.0 필요

### CUDA 관련 에러 (macOS에서 자주 보이는 경우)

```
AssertionError: CUDA is not availabe on this machine.
```

- macOS에서는 CUDA 대신 MPS를 사용해야 합니다.
- `scripts/clone_voice.py` 사용 시 `--use-gpu` 옵션으로 MPS가 자동 선택되는지 확인하세요.
- Python API 직접 호출 시 `gpu=True` 대신 `gpu=False` + `tts.to("mps")` 방식으로 실행하세요.

### 메모리 부족

```
torch.OutOfMemoryError
```

- CPU 모드로 전환 (`--use-gpu` 제거)
- 텍스트를 짧게 분할
- 다른 프로그램 종료하여 메모리 확보

### 한국어 발음이 이상한 경우

- 영어/숫자가 섞인 텍스트는 한국어로 읽어쓰기 (예: "AI" → "에이아이")
- 문장 부호(마침표, 쉼표)를 적절히 넣으면 억양이 자연스러워짐

## 다음 단계

← [02-recording.md](./02-recording.md)
→ [04-finetuning.md](./04-finetuning.md)
