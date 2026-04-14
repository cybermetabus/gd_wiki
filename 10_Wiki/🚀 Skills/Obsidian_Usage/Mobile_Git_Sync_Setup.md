---
type: guide
category: skills
topic: obsidian-mobile
created: 2026-04-14
---

# 📱 Obsidian 모바일 Git 동기화 가이드

이 가이드는 맥북의 지식 정원을 스마트폰(iOS/Android)에서도 동일하게 보고 편집할 수 있도록 설정하는 방법을 설명합니다.

---

## 🛠️ 사전 준비물
1.  **스마트폰**: Obsidian 앱이 설치되어 있어야 합니다.
2.  **GitHub 토큰 (PAT)**: 아까 발급받으신 긴 문자열(토큰)이 필요합니다. (메모장에 복사해 두셨죠?)
3.  **저장소 주소**: `https://github.com/cybermetabus/gd_wiki.git`

---

## 📥 1단계: Obsidian 앱 및 플러그인 설치
1.  앱스토어/플레이스토어에서 **Obsidian** 앱을 설치합니다.
2.  앱을 열고 **"Create new vault"**를 눌러 임시 저장소를 만듭니다. (이름은 아무거나 상관없습니다.)
3.  하단 메뉴의 **Settings (톱니바퀴)** ➔ **Community plugins** ➔ **Turn on community plugins**를 클릭합니다.
4.  **Browse**를 눌러 **"Obsidian Git"**을 검색하고 **Install** ➔ **Enable**을 차례로 누릅니다.

---

## 🔑 2단계: Git 연동 및 인증 설정 (핵심)
1.  설정창의 **Community plugins** 리스트에서 **Obsidian Git** 항목의 톱니바퀴를 누릅니다.
2.  **Authentication** 섹션을 찾습니다.
    -   **GitHub username**: 사용자님의 GitHub 아이디를 입력합니다.
    -   **Personal Access Token**: 준비해둔 **PAT(토큰)**를 붙여넣습니다.
3.  **Git repository** 섹션을 찾습니다.
    -   **Repository URL**: `https://github.com/cybermetabus/gd_wiki.git` 을 입력합니다.

---

## 🔄 3단계: 지식 수확 (Clone/Pull)
1.  Obsidian 앱의 왼쪽 사이드바(또는 명령어 팔레트 `Cmd/Ctrl + P`)를 엽니다.
2.  **"Git: Clone"** 또는 **"Git: Pull"** 명령어를 찾아 실행합니다.
3.  잠시 기다리면 맥북에 있던 모든 폴더(`00_Raw`, `10_Wiki` 등)가 스마트폰으로 쏟아져 들어옵니다!

---

## 💡 팁: 자동 동기화 설정
Obsidian Git 설정 메뉴 아래쪽에서 다음 두 가지를 활성화하면 더 편리합니다:
*   **Pull updates on startup**: 앱을 열 때마다 자동으로 새로운 지식을 가져옵니다.
*   **Auto backup interval**: 편집한 내용을 주기적으로 자동으로 GitHub에 올립니다.

이제 언제 어디서든 사용자님의 지식 정원을 손안에서 가꾸실 수 있습니다! 🚀🌿
