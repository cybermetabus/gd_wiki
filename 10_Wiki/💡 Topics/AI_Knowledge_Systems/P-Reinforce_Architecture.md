---
id: c3e4f5g6-h7i8-9j0k-1l2m-3n4o5p6q7r8s
category: "[[10_Wiki/💡 Topics/AI_Knowledge_Systems]]"
confidence_score: 1.0
tags: [ai-architecture, knowledge-management, p-reinforce, obsidian, rl]
last_reinforced: 2026-04-14
github_commit: "pending"
---

# [[P-Reinforce 아키텍처: 자율형 지식 정원 시스템]]

## 📌 한 줄 통찰 (The Karpathy Summary)
> 파편화된 정보를 영속적 위키로 자동 변환하기 위해 강화학습 보상 함수를 적용한 지식 구조화 엔진의 설계 원칙.

## 📖 핵심 이론 (The Architecture)

### 1. 🧠 RL 기반 보상 로직
모든 지식 배치는 다음 보상 함수 $R$을 극대화하는 방향으로 수행됩니다.
$$R = w_1(\text{분류 정확도}) + w_2(\text{그래프 연결성}) + w_3(\text{사용자 만족도})$$

### 2. 📂 표준 폴더 구조 (The Soil to Garden)
- **`00_Raw/`**: 가공되지 않은 모든 데이터의 보관소 (Source of Truth).
- **`10_Wiki/`**: 강화학습에 의해 구조화된 지식 층 (Projects, Topics, Decisions, Skills).
- **`20_Meta/`**: 시스템의 두뇌 데이터 (Graph, Policy, Index).

---

## 🎨 Obsidian 활용 가이드 (Obsidian Integration)

이 위키 시스템은 Obsidian과의 완벽한 호환성을 고려하여 설계되었습니다.

1. **지식 그래프 확인**: Obsidian의 `Graph View`를 열면 `20_Meta/Graph.json`에 정의된 연결 관계를 시각적으로 한눈에 파악할 수 있습니다.
2. **양방향 링크 탐색**: 모든 문서 상단의 `category` 링크와 하단의 `🔗 지식 연결` 섹션을 통해 관련 지식 사이를 자유롭게 이동하세요.
3. **MOC(Map of Content) 활용**: `20_Meta/Index.md`를 홈 화면으로 설정하여 지식 지형도를 탐색의 출발점으로 삼으세요.

## 🔗 지식 연결 (Graph)
- **Parent:** [[10_Wiki/💡 Topics/AI_Knowledge_Systems]]
- **Related:** [[P-Reinforce_Skill]], [[10_Wiki/🚀 Skills/Creative_Prompts/Sand_Cheetah_Cinematic_Concept]]
- **Raw Source:** [[00_Raw/2026-04-14/071156_위키에이전트 핵심 코드 및 Obsidian 연동 메모]]
