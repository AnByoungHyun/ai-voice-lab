# Task 003: XTTS v2 음성 클로닝 실습

**상태:** 진행 중
**담당:** Claude Code
**의존성:** task-001 완료, task-002 완료 (음성 샘플 준비)
**시작일:** 2026-03-18

## 목표

XTTS v2 모델을 사용하여 레퍼런스 음성으로 텍스트를 음성으로 변환(클로닝)하는 실습 가이드와 스크립트를 작성한다.

## 입력 (Input)

- `docs/02-recording.md` (2단계 문서 - 음성 샘플 준비)
- `samples/` 디렉토리의 레퍼런스 음성 파일
- Coqui TTS 0.27.5 + XTTS v2 모델
- Apple Silicon MPS 환경

## 출력 (Output)

- `docs/03-cloning.md` 신규 작성
- `scripts/clone_voice.py` 실습 스크립트 작성
- CLI 및 Python API 두 가지 방식 모두 포함
- 한국어/영어 텍스트 합성 예제 포함

## 작업 단계

1. XTTS v2 Python API 동작 확인 및 스크립트 작성
2. CLI 방식과 Python API 방식 비교 정리
3. `docs/03-cloning.md` 강의 문서 작성
4. 한국어/영어 합성 결과 비교 섹션 추가
5. 트러블슈팅 및 품질 개선 팁 포함

## 완료 조건

- [ ] `scripts/clone_voice.py` 파일 존재 및 실행 가능
- [ ] `docs/03-cloning.md` 파일 존재
- [ ] 학습 목표/사전 지식/산출물이 명시됨
- [ ] CLI와 Python API 두 가지 방식 모두 설명
- [ ] 한국어/영어 합성 예제 포함
- [ ] 품질 평가 기준 및 트러블슈팅 포함
- [ ] `PROGRESS.md`에 진행 상태 반영

## 완료 후 할 일

1. `README.md` 진행 단계 체크 상태 업데이트
2. `PROGRESS.md` 현재 단계 업데이트
3. 사용자 승인 후 커밋/푸시
