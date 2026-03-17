# 1단계: 환경 설정

## 시스템 요구사항

- Apple Silicon (M1/M2/M3/M4/M5) 또는 CUDA GPU
- RAM 16GB 이상 권장 (128GB면 최상)
- macOS 또는 Linux
- Python 3.10+

## 설치

### 1. Python 환경 설정

```bash
# pyenv로 Python 버전 관리 (권장)
brew install pyenv
pyenv install 3.11
pyenv local 3.11

# 가상환경 생성
python -m venv .venv
source .venv/bin/activate
```

### 2. Coqui TTS 설치

```bash
pip install TTS
```

### 3. 설치 확인

```bash
tts --list_models | grep xtts
```

## 다음 단계

→ [02-recording.md](./02-recording.md)
