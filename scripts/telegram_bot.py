import json
import time
import subprocess
import os
import urllib.request
import urllib.parse

# --- Configurations ---
TOKEN = "8622322269:AAGwYAYA2sdJ9dwWvMUTbI04L-93s0YYN74"
ALLOWED_CHAT_ID = "6507753780"
BASE_DIR = "/Users/gdstudio/build/Antigravity/위키에이전트"
INGEST_SCRIPT = os.path.join(BASE_DIR, "scripts/ingest.py")

def api_call(method, params=None):
    """Makes a call to the Telegram Bot API using built-in urllib."""
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    if params:
        query = urllib.parse.urlencode(params)
        url += f"?{query}"
    
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"⚠️ API Call Error: {e}")
        return None

def run_ingest(text):
    """Calls the local ingest script with the received text."""
    try:
        subprocess.run(["python3", INGEST_SCRIPT, text], check=True, cwd=BASE_DIR)
        print(f"✅ Ingested: {text[:20]}...")
        
        # Sync to GitHub
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"sync: Telegram knowledge received"], cwd=BASE_DIR)
        subprocess.run(["git", "push"], cwd=BASE_DIR)
        print("🚀 Synced to GitHub.")
    except Exception as e:
        print(f"❌ Error during ingestion/sync: {e}")

def main():
    print("🤖 P-Reinforce Telegram Bridge is active (using urllib)...")
    last_update_id = 0
    
    while True:
        try:
            # Long-polling Telegram API
            result = api_call("getUpdates", {"offset": last_update_id + 1, "timeout": 30})
            
            if result and result.get("ok"):
                updates = result.get("result", [])
                for update in updates:
                    last_update_id = update["update_id"]
                    
                    message = update.get("message", {})
                    chat_id = str(message.get("chat", {}).get("id", ""))
                    text = message.get("text", "")
                    
                    if chat_id == ALLOWED_CHAT_ID and text:
                        print(f"📩 Message received from user {chat_id}")
                        run_ingest(text)
                    elif chat_id and chat_id != ALLOWED_CHAT_ID:
                        print(f"🔒 Unauthorized access attempt from {chat_id}")
            else:
                if result:
                    print(f"⚠️ Error from Telegram API: {result}")
                
        except Exception as e:
            print(f"🔥 Unexpected error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
