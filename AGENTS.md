# AGENTS.md - AI Voice Lab

## 프로젝트 개요

로컬 환경에서 AI 음성 클로닝 및 TTS 시스템을 구축하는 실습 프로젝트.
강의 자료로 활용될 예정이며, 각 단계를 문서화하면서 진행한다.

## 환경 정보

- **하드웨어:** Apple M5 Max, 128GB RAM
- **OS:** macOS (Darwin arm64)
- **Python:** 3.11 권장
- **주요 경로:**
  - 프로젝트 루트: `~/workspaces/ai-voice-lab/`
  - 가상환경: `~/workspaces/ai-voice-lab/.venv/`
  - 음성 샘플: `~/workspaces/ai-voice-lab/samples/` (.gitignore됨)
  - 모델: `~/workspaces/ai-voice-lab/models/` (대용량 파일 제외)

## 프로젝트 구조

```
ai-voice-lab/
├── AGENTS.md          ← 현재 파일 (AI 에이전트 공통 가이드)
├── CLAUDE.md          ← Claude Code 전용 컨텍스트
├── README.md          ← 프로젝트 소개
├── PROGRESS.md        ← 진행 상황 트래킹 (항상 최신 상태 유지)
├── docs/              ← 단계별 문서 (강의 자료)
├── tasks/             ← 에이전트별 독립 태스크 정의
├── samples/           ← 음성 샘플 (.gitignore)
├── models/            ← 학습 모델
├── scripts/           ← 유틸리티 스크립트
└── notebooks/         ← Jupyter 실습 노트북
```

## 에이전트 운영 원칙

### 1. 문맥 유지
- 작업 시작 전 반드시 `PROGRESS.md` 읽기
- 작업 완료 후 반드시 `PROGRESS.md` 업데이트
- 중요한 결정사항은 해당 `docs/` 문서에 기록

### 2. 태스크 분리
- `tasks/` 디렉토리의 각 파일이 독립 태스크
- 각 태스크는 어떤 LLM/에이전트도 이어받을 수 있도록 자기완결적으로 작성
- 태스크 완료 시 `[x]` 체크 및 결과 요약 추가

### 3. 병렬 작업 가능한 태스크 설계
- 의존성이 없는 태스크는 병렬 실행 가능하도록 표시
- 각 태스크는 입력(Input), 출력(Output), 의존성(Depends)을 명시

### 4. 코드 품질
- 모든 스크립트에 주석 필수
- 환경 의존성은 `requirements.txt`에 명시
- 실행 결과 예시 포함

## 현재 담당 에이전트

- **지은 (OpenClaw/Claude Sonnet):** 전체 조율, 문서화, 환경 설정
- **추후 추가 가능:** Codex, Gemini, 로컬 LLM 등

## 참고

- [PROGRESS.md](./PROGRESS.md) - 현재 진행 상황
- [CLAUDE.md](./CLAUDE.md) - Claude Code 작업 시 참고
