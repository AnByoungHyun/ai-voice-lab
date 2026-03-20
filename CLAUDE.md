# CLAUDE.md - Claude Code 전용 가이드

> Claude Code로 이 프로젝트 작업 시 반드시 읽을 것.
> 기존 AGENTS.md는 Codex/OpenClaw 등 다른 에이전트용이므로 수정하지 않는다.

## 프로젝트 개요

로컬 환경에서 AI 음성 클로닝 및 TTS 시스템을 구축하는 **교육용 실습 프로젝트**.
각 단계를 문서화(강의 자료)하면서 진행하며, 최종 목표는 OpenClaw AI 어시스턴트와 통합.

## 시작 전 체크리스트

1. `PROGRESS.md` 읽기 → 현재 어디까지 왔는지 파악
2. 해당 태스크 파일(`tasks/`) 읽기 → 작업 범위와 완료 기준 확인
3. 가상환경 활성화 확인: `source .venv/bin/activate`
4. 의존성 확인: `pip list | head -20` (필요 시)

## 환경 정보

- **하드웨어:** Apple M5 Max, 128GB RAM
- **OS:** macOS (Darwin arm64)
- **Python:** 3.12.13 (.venv), 시스템은 3.14.3
- **주요 기술:** Coqui TTS 0.27.5, XTTS v2, PyTorch 2.10+
- **주의:** transformers 5.x는 coqui-tts와 비호환 → 4.43~4.x 사용

## 프로젝트 구조

```
ai-voice-lab/
├── AGENTS.md          ← 범용 에이전트 가이드 (Codex/OpenClaw 등, 수정 금지)
├── CLAUDE.md          ← 현재 파일 (Claude Code 전용)
├── PROGRESS.md        ← 진행 상황 트래킹 (항상 최신 유지)
├── README.md          ← 프로젝트 소개
├── requirements.txt   ← Python 의존성
├── docs/              ← 단계별 강의 자료
│   ├── 00-glossary.md
│   ├── 01-setup.md
│   └── 02-recording.md
├── tasks/             ← 독립 태스크 정의
├── scripts/           ← 유틸리티 스크립트
├── notebooks/         ← Jupyter 실습 노트북
├── models/            ← 학습 모델 (커밋 금지)
├── samples/           ← 음성 샘플 (커밋 금지)
└── .cursor/           ← Cursor 전용 설정 (수정 금지)
```

## 코딩 컨벤션

- Python 3.11+ 문법 사용
- 타입 힌트 필수
- 함수마다 docstring 작성 (한국어 가능)
- 에러 핸들링 필수
- 문서는 한국어로 작성
- 커밋 메시지는 영어

## 문서 작성 규칙

이 프로젝트의 `docs/`는 교육용 강의 자료이므로 아래 기준을 따른다:

- **학습 목표** 명시 (각 문서 상단)
- **단계별 구조** (따라하면 결과가 나오는 형태)
- **코드 실행 가능성** (복사-붙여넣기로 동작)
- **트러블슈팅** 포함
- **용어 일관성** 유지 (docs/00-glossary.md 참조)
- 대상 독자: AI/ML에 관심 있는 **개발자** (완전 초보 아님)

## 태스크 작업 방법

1. `tasks/` 디렉토리에서 태스크 파일 확인
2. 태스크의 Input/Output/Depends 확인
3. 완료 기준(Completion Criteria) 모두 충족 시 `[x]` 체크
4. 새 태스크 생성 시 기존 태스크 포맷 따르기

## 작업 완료 후

1. `PROGRESS.md` 업데이트
2. 관련 `docs/` 문서 업데이트
3. 커밋 (커밋 메시지 영어, Conventional Commits 형식)
4. 필요 시 push

## 절대 금지 사항

- `samples/` 디렉토리 내용 커밋 (개인 음성 데이터)
- 모델 파일(.pth, .bin, .safetensors) 커밋
- `.env` 파일 커밋
- `AGENTS.md` 수정 (다른 에이전트용)
- `.cursor/` 디렉토리 수정 (Cursor 전용)

## 참고

- [PROGRESS.md](./PROGRESS.md) - 현재 진행 상황
- [AGENTS.md](./AGENTS.md) - 범용 에이전트 가이드 (참고용)
- [docs/00-glossary.md](./docs/00-glossary.md) - 용어집
