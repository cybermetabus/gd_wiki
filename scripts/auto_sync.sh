#!/bin/bash

# P-Reinforce Auto-Sync Script
# 주기적으로 GitHub에서 최신 지식을 가져옵니다.

PROJECT_DIR="/Users/gdstudio/build/Antigravity/위키에이전트"
cd "$PROJECT_DIR" || exit

# 1. 원격지 정보 업데이트
git fetch origin main

# 2. 로컬과 원격의 차이 확인
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ "$LOCAL" != "$REMOTE" ]; then
    echo "$(date): New knowledge found! Pulling..."
    git pull origin main
    
    # 텔레그램 알림을 원하시면 아래 주석을 해제할 수도 있습니다.
    # curl -s "https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<ID>&text=🔄 맥북 지식 동기화 완료"
else
    echo "$(date): Garden is up to date."
fi
