# 4단계: XTTS v2 파인튜닝

## 학습 목표

이 단계를 마치면 다음을 할 수 있습니다:

- 파인튜닝이 필요한 상황과 목표를 구체적으로 정의할 수 있다
- 파인튜닝용 데이터셋 구조와 메타데이터 포맷을 준비할 수 있다
- 학습 전 데이터 품질 검증을 자동화할 수 있다
- 학습 결과를 3단계 제로샷 결과와 비교 평가할 수 있다

**예상 소요 시간:** 2~6시간 (데이터 준비 포함)  
**난이도:** ★★★★☆ (중상급)

## 사전 지식

- [0단계(선택): 개념 이해](./00-tts-ml-concepts.md)
- [1단계: 환경 설정](./01-setup.md)
- [2단계: 음성 샘플 녹음](./02-recording.md)
- [3단계: 음성 클로닝](./03-cloning.md)

## 핵심 용어

| 용어 | 설명 |
|------|------|
| **Fine-tuning** | 사전학습 모델을 내 데이터로 추가 학습해 품질을 높이는 과정 |
| **Overfitting** | 학습 데이터에는 잘 맞지만 새로운 문장 일반화가 떨어지는 현상 |
| **Validation set** | 학습 중 품질 추이를 확인하기 위한 검증 데이터셋 |
| **Checkpoint** | 학습 중간 상태를 저장한 모델 파일 |

> 전체 용어집은 [99-glossary.md](./99-glossary.md)를 참고하세요.

## 왜 파인튜닝을 하는가?

3단계 제로샷 클로닝이 성공했더라도 아래 문제는 자주 남습니다:

- 긴 문장에서 억양이 흔들림
- 한국어 받침/고유명사 발음 불안정
- 문장마다 화자 느낌이 달라짐

4단계의 목적은 **음색 일관성, 발음 안정성, 문장 일반화 성능**을 높여 실사용 품질에 가깝게 만드는 것입니다.

## 준비 데이터 기준

| 항목 | 권장값 | 최소값 |
|------|--------|--------|
| 총 발화 길이 | 20~60분 | 10분 |
| 파일 길이(개별) | 3~12초 | 2초 |
| 샘플레이트 | 24kHz mono | 24kHz mono |
| 텍스트 품질 | 오탈자 최소화, 구두점 포함 | 문장 단위 분리 |

## 데이터셋 구조

```text
datasets/
  my_voice_ko/
    wavs/
      0001.wav
      0002.wav
      ...
    metadata.csv
```

`metadata.csv` 예시:

```csv
0001.wav|안녕하세요. 파인튜닝 데이터 첫 번째 문장입니다.|speaker_01
0002.wav|오늘은 음성 모델 품질을 높이기 위한 학습을 진행합니다.|speaker_01
0003.wav|문장 부호와 숫자 발음도 함께 점검합니다.|speaker_01
```

## 단계별 진행

### 1) 데이터 디렉토리 준비

```bash
cd ~/workspaces/ai-voice-lab
mkdir -p datasets/my_voice_ko/wavs
```

### 2) 오디오 포맷 통일 (24kHz, mono)

원본이 섞여 있으면 아래 방식으로 변환합니다.

```bash
ffmpeg -i samples/voice_ref_01_24k.wav -ar 24000 -ac 1 datasets/my_voice_ko/wavs/0001.wav
```

여러 파일 일괄 변환 예시:

```bash
for f in samples/*.wav; do
  b=$(basename "$f")
  ffmpeg -y -i "$f" -ar 24000 -ac 1 "datasets/my_voice_ko/wavs/$b"
done
```

### 3) 오디오 품질 빠른 검증

```bash
for f in datasets/my_voice_ko/wavs/*.wav; do
  ffprobe -v error -show_entries stream=sample_rate,channels -show_entries format=duration -of default=noprint_wrappers=1 "$f"
done
```

확인 기준:
- `sample_rate=24000`
- `channels=1`
- 발화 길이 2~15초 범위 권장

### 4) 메타데이터 검증

```bash
python - <<'PY'
from pathlib import Path

root = Path("datasets/my_voice_ko")
meta = root / "metadata.csv"
missing = []
bad = 0

for line_no, line in enumerate(meta.read_text(encoding="utf-8").splitlines(), start=1):
    parts = line.split("|")
    if len(parts) != 3:
        bad += 1
        print(f"[형식 오류] line {line_no}: {line}")
        continue
    wav, text, speaker = parts
    if not (root / "wavs" / wav).exists():
        missing.append((line_no, wav))
    if not text.strip():
        bad += 1
        print(f"[텍스트 누락] line {line_no}")
    if not speaker.strip():
        bad += 1
        print(f"[화자 누락] line {line_no}")

print(f"missing_files={len(missing)}")
print(f"bad_rows={bad}")
if missing:
    for line_no, wav in missing[:10]:
        print(f"[파일 누락] line {line_no}: {wav}")
PY
```

## 학습 실행 전략 (현재 단계 권장)

현재 프로젝트에서는 아래 순서로 진행하는 것을 권장합니다:

1. **데이터 준비/검증 자동화 먼저 완료**
2. **작은 데이터(10~20분)로 짧은 실험 학습 1회**
3. 결과를 3단계 출력과 A/B 비교
4. 품질 향상 확인 후 데이터 확장 및 본 학습

> 실제 학습 커맨드는 모델 버전/학습 스크립트 의존성이 커서, 다음 작업에서 환경에 맞는 실행 스크립트로 확정합니다.

## 품질 평가 체크리스트

- [ ] 3단계 대비 음색 일관성이 좋아졌는가?
- [ ] 긴 문장 발음이 덜 흔들리는가?
- [ ] 한국어 받침/고유명사 오류가 감소했는가?
- [ ] 문장별 화자 스타일 편차가 줄었는가?
- [ ] 추론 시간 증가 대비 품질 이점이 충분한가?

## 트러블슈팅

### 데이터는 많은데 품질이 안 오름

- 원인: 텍스트 정렬 품질이 낮거나, 잡음/중복 발화가 많음
- 해결: `metadata.csv` 오탈자/중복 제거, 잡음 구간 제거, 발화 길이 균일화

### 학습이 너무 빨리 과적합됨

- 원인: 데이터 다양성 부족, 에폭 과다
- 해결: 검증셋 분리, 에폭/학습률 조정, 발화 스타일 다양화

### 메모리 부족 (MPS/CPU)

- 원인: 배치 크기 과대, 긴 오디오 비율 과다
- 해결: 배치 크기 축소, 긴 파일 분할, 백그라운드 앱 종료

## 산출물

- `datasets/my_voice_ko/wavs/*.wav`
- `datasets/my_voice_ko/metadata.csv`
- (다음 작업) 학습 체크포인트 및 비교 결과 리포트

## 다음 단계

← [03-cloning.md](./03-cloning.md)  
→ [05-integration.md](./05-integration.md)
