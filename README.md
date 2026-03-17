# AI Voice Lab 🎙️

로컬 환경에서 AI 음성 클로닝 및 TTS 시스템을 구축하는 실습 프로젝트입니다.

## 목표

- 오픈소스 TTS 모델을 활용한 음성 클로닝
- 로컬 머신러닝 기반 커스텀 음성 생성
- AI 어시스턴트(OpenClaw)와 연동

## 환경

- **하드웨어:** Apple M5 Max, 128GB RAM
- **OS:** macOS
- **주요 기술:** Python, XTTS v2, Coqui TTS

## 프로젝트 구조

```
ai-voice-lab/
├── README.md
├── docs/                  # 과정 문서 및 강의 자료
│   ├── 01-setup.md        # 환경 설정
│   ├── 02-recording.md    # 음성 샘플 녹음
│   ├── 03-cloning.md      # 음성 클로닝 (XTTS v2)
│   ├── 04-finetuning.md   # 파인튜닝
│   └── 05-integration.md  # OpenClaw TTS 연동
├── samples/               # 녹음된 음성 샘플
├── models/                # 학습된 모델 저장
├── scripts/               # 유틸리티 스크립트
└── notebooks/             # Jupyter 실습 노트북
```

## 진행 단계

- [ ] 1단계: 환경 설정 (Python, Coqui TTS 설치)
- [ ] 2단계: 음성 샘플 녹음
- [ ] 3단계: XTTS v2로 음성 클로닝 테스트
- [ ] 4단계: 파인튜닝으로 품질 향상
- [ ] 5단계: OpenClaw TTS 연동

## 참고 자료

- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [XTTS v2](https://huggingface.co/coqui/XTTS-v2)
- [OpenClaw](https://docs.openclaw.ai)
