# PROGRESS.md - 진행 상황

> 에이전트는 작업 시작/종료 시 이 파일을 반드시 읽고 업데이트할 것.

## 현재 상태

**단계:** 4단계 파인튜닝 준비
**마지막 업데이트:** 2026-03-20
**담당:** Claude Code

## 완료된 작업

- [x] 프로젝트 구조 생성
- [x] GitHub 리포지토리 생성 (https://github.com/AnByoungHyun/ai-voice-lab)
- [x] AGENTS.md, CLAUDE.md, PROGRESS.md 작성
- [x] 1단계 문서 초안 (docs/01-setup.md)
- [x] .gitignore 설정
- [x] Python 가상환경 설정 (.venv, Python 3.12.13)
- [x] Coqui TTS 설치 및 XTTS v2 확인 (coqui-tts 0.27.5)
- [x] transformers 호환성 이슈 해결 (5.x → 4.57.6)
- [x] torchcodec 설치 (PyTorch 2.10+ 필수 의존성)
- [x] requirements.txt 작성
- [x] docs/01-setup.md 실제 환경 기반으로 업데이트 (트러블슈팅 포함)
- [x] 교안 검수 Skill 생성 (.cursor/skills/review-edu-docs/)
- [x] 교안 검수 결과에 따른 문서 보완 (2026-03-18)
  - docs/01-setup.md: 학습 목표, 핵심 용어, 사전 지식, TTS 테스트 대안 추가
  - README.md: 대상 독자, 기술 소개 표, docs 링크 연결, Python 버전 통일
  - docs/99-glossary.md: 용어집 신규 생성
- [x] 2단계 녹음 가이드 작성 (docs/02-recording.md, task-002)
- [x] 개념 설명 문서 추가 (docs/00-tts-ml-concepts.md)

## 진행 중인 작업

- [ ] 4단계: 파인튜닝 (task-004 예정)

## 남은 작업

- [ ] 4단계: 파인튜닝
- [ ] 5단계: OpenClaw TTS 연동
- [ ] Jupyter 노트북 작성
- [ ] 강의용 슬라이드 자료 정리

## 최근 완료 작업

- [x] 3단계: XTTS v2 음성 클로닝 (task-003)
  - [x] 태스크 정의
  - [x] 클로닝 스크립트 작성 (`scripts/clone_voice.py`)
  - [x] 강의 문서 작성 (`docs/03-cloning.md`)
  - [x] 실제 음성 테스트 실행 (`output/clone_ko_test.wav`, `output/clone_en_test.wav`)

## 병렬 처리 가능한 태스크

아래 태스크들은 서로 독립적이므로 동시에 진행 가능:

| 태스크 | 담당 가능 에이전트 | 상태 |
|--------|------------------|------|
| Python 환경 설정 스크립트 작성 | 모든 에이전트 | **완료** |
| 녹음 가이드 문서 작성 | 모든 에이전트 | **완료** |
| Jupyter 노트북 뼈대 작성 | 모든 에이전트 | 대기 |

## 주요 결정 사항

- XTTS v2를 첫 번째 클로닝 도구로 선택 (이유: 6초 샘플로 클로닝 가능, 한국어 지원)
- 음성 샘플은 .gitignore 처리 (개인정보 보호)
- 강의 자료는 docs/ 디렉토리에 단계별로 관리
- **transformers 5.x는 coqui-tts 0.27.5와 비호환** → 4.43~4.x 사용 필수
- **PyTorch 2.9+부터 torchcodec 필수** → `coqui-tts[codec]`으로 설치

## 메모

- M5 Max + 128GB RAM → 로컬 학습 충분히 가능
- 추후 Gemini, Codex 등 다른 에이전트 투입 계획
- Python 3.12.13 사용 중 (시스템 Python은 3.14.3이나 .venv는 3.12)
