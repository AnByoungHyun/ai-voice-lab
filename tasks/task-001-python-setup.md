# Task 001: Python 환경 설정

**상태:** 완료  
**담당:** Claude Code  
**의존성:** 없음 (병렬 실행 가능)  
**완료일:** 2026-03-17

## 목표

프로젝트 로컬 Python 환경을 구성하고 Coqui TTS를 설치한다.

## 입력 (Input)

- macOS arm64 (M5 Max)
- Python 3.11

## 출력 (Output)

- `.venv/` 가상환경 생성
- `requirements.txt` 작성
- `pip install TTS` 완료
- `tts --list_models | grep xtts` 성공 확인

## 작업 단계

```bash
# 1. 프로젝트 디렉토리로 이동
cd ~/workspaces/ai-voice-lab

# 2. Python 버전 확인
python3 --version  # 3.11 이상 필요

# 3. 가상환경 생성
python3 -m venv .venv
source .venv/bin/activate

# 4. pip 업그레이드
pip install --upgrade pip

# 5. Coqui TTS 설치
pip install TTS

# 6. 설치 확인
tts --list_models | grep xtts
```

## 완료 조건

- [x] `.venv/` 디렉토리 존재
- [x] `tts` 명령어 실행 가능
- [x] XTTS v2 모델 목록에 표시됨
- [x] `requirements.txt` 생성

## 완료 후 할 일

1. 이 파일의 상태를 `완료`로 변경
2. `PROGRESS.md` 업데이트
3. `docs/01-setup.md` 실제 설치 결과로 업데이트
4. 커밋 및 푸시
