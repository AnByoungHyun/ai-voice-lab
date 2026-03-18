# AI Voice Lab

로컬 환경에서 AI 음성 클로닝 및 TTS 시스템을 구축하는 실습 프로젝트입니다.

## 대상 독자

- AI/ML에 관심 있는 **개발자** 또는 **엔지니어**
- Python 기본 문법을 알고 있는 분
- 터미널(CLI) 사용에 어려움이 없는 분
- 별도의 ML/딥러닝 사전 지식은 필요하지 않습니다

## 목표

- 오픈소스 TTS 모델을 활용한 음성 클로닝
- 로컬 머신러닝 기반 커스텀 음성 생성
- AI 어시스턴트(OpenClaw)와 연동

## 주요 기술 소개

| 기술 | 설명 |
|------|------|
| **[Coqui TTS](https://github.com/coqui-ai/TTS)** | 오픈소스 TTS 엔진. 다양한 음성 합성 모델을 제공한다 |
| **[XTTS v2](https://huggingface.co/coqui/XTTS-v2)** | Coqui의 다국어 음성 클로닝 모델. 6초 음성으로 화자 복제 가능 |
| **[OpenClaw](https://docs.openclaw.ai)** | AI 어시스턴트 플랫폼. 커스텀 TTS와 연동하여 나만의 음성 AI를 만들 수 있다 |

## 환경

- **하드웨어:** Apple M5 Max, 128GB RAM
- **OS:** macOS
- **Python:** 3.12+
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

각 단계별 문서를 순서대로 따라가면 됩니다:

- [x] **1단계:** [환경 설정](docs/01-setup.md) — Python, Coqui TTS 설치 및 동작 확인
- [x] **2단계:** [음성 샘플 녹음](docs/02-recording.md) — 녹음 가이드 문서 작성 완료
- [ ] **3단계:** [XTTS v2로 음성 클로닝](docs/03-cloning.md) — 음성 복제 실습
- [ ] **4단계:** [파인튜닝](docs/04-finetuning.md) — 클로닝 품질 향상
- [ ] **5단계:** [OpenClaw 연동](docs/05-integration.md) — AI 어시스턴트와 커스텀 음성 통합
