---
id: b9d4f0a1-7c5e-4b2a-8d1c-9f3a8b2d1e0f
category: "[[10_Wiki/🚀 Skills/Local_LLM_Environment]]"
confidence_score: 1.0
tags: [ollama, antigravity, local-llm, gemma, configuration]
last_reinforced: 2026-04-14
github_commit: "pending"
---

# [[Ollama 로컬 서버 구축 및 Antigravity 실전 연동 가이드]]

## 📌 한 줄 통찰 (The Karpathy Summary)
> Ollama를 활용한 로컬 모델 서버 구축부터 외부 에이전트 도구(Antigravity)와의 OpenAI 호환 API 연동까지의 전 과정을 정립함.

## 📖 구조화된 지식 (Synthesized Content)

### 1. Ollama 로컬 서버 활성화
외부 접속을 허용하기 위해 호스트 환경변수를 설정하여 서버를 구동합니다.
```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

### 2. 에이전트 소통 테스트 (API Verification)
`curl` 명령어를 사용하여 로컬 모델(gemma4)이 정상적으로 응답하는지 확인합니다.
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma4:e4b",
  "prompt": "gd는 제이는 누구야?",
  "stream": false
}'
```

### 3. Antigravity 환경 설정 (`antigravity.config.json`)
도구에서 로컬 모델을 기본 모델로 인식하도록 `openai-compatible` 프로바이더 설정을 적용합니다.
```json
{
  "models": {
    "local": {
      "provider": "openai-compatible",
      "baseUrl": "http://localhost:11434/v1",
      "model": "gemma4:e4b",
      "apiKey": "ollama",
      "temperature": 0.1,
      "maxTokens": 4096,
      "contextWindow": 128000
    }
  },
  "defaultModel": "local",
  "fallback": {
    "enabled": true,
    "model": "claude-opus-4-6",
    "trigger": "context_exceeded"
  }
}
```

## ⚠️ 모순 및 업데이트 (Contradictions & RL Update)
- **과거 데이터와의 충돌:** 없음.
- **정책 변화:** 기술적 가이드라인 카테고리(`🚀 Skills`)의 하위 분류로 `Local_LLM_Environment`를 새롭게 정의하여 구조화의 깊이를 더함.

## 🔗 지식 연결 (Graph)
- **Parent:** [[10_Wiki/🚀 Skills]]
- **Related:** [[10_Wiki/🛠️ Projects/System_Initialization/01_System_Validation]]
- **Raw Source:** [[00_Raw/2026-04-14/070734_오늘 배운 내용을 정리해볼께]]
