# CLAUDE.md - Claude Code 전용 가이드

Claude Code로 이 프로젝트 작업 시 반드시 읽을 것.

## 시작 전 체크리스트

1. `PROGRESS.md` 읽기 → 현재 어디까지 왔는지 파악
2. 해당 태스크 파일(`tasks/`) 읽기
3. 가상환경 활성화 확인: `source .venv/bin/activate`

## 코딩 컨벤션

- Python 3.11+
- 타입 힌트 사용
- 함수마다 docstring 작성 (한국어 가능)
- 에러 핸들링 필수

## 작업 완료 후

1. `PROGRESS.md` 업데이트
2. 관련 `docs/` 문서 업데이트
3. `git add -A && git commit -m "..."` (커밋 메시지 영어)
4. `git push`

## 주의사항

- `samples/` 디렉토리 내용은 절대 커밋하지 말 것 (개인 음성 데이터)
- 모델 파일(.pth, .bin)도 커밋 금지
- 환경변수는 `.env` 파일 사용 (역시 커밋 금지)
