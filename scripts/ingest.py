import os
import sys
from datetime import datetime, timedelta, timezone

def ingest():
    # 1. Base directory setup
    base_dir = "/Users/gdstudio/build/Antigravity/위키에이전트"
    raw_dir = os.path.join(base_dir, "00_Raw")
    
    # 2. Get current date for folder
    # 2. Get current date for folder (KST/UTC+9)
    KST = timezone(timedelta(hours=9))
    now_kst = datetime.now(KST)
    today = now_kst.strftime("%Y-%m-%d")
    target_dir = os.path.join(raw_dir, today)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 Created new directory: {today}")

    # 3. Handle Input
    content = ""
    if len(sys.argv) > 1:
        # One-liner mode
        content = " ".join(sys.argv[1:])
    else:
        # Interactive mode
        print("📝 Enter your knowledge (Press Ctrl+D to save):")
        try:
            content = sys.stdin.read().strip()
        except EOFError:
            pass

    if not content:
        print("⚠️ No content provided. Aborting.")
        return

    # 4. Generate metadata
    timestamp = now_kst.strftime("%H%M%S")
    full_time = now_kst.strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate title (first 30 characters or first line)
    first_line = content.split('\n')[0].strip()
    clean_title = "".join(x for x in first_line if x.isalnum() or x in " -_")[:30].strip()
    if not clean_title:
        clean_title = f"note_{timestamp}"
    
    filename = f"{timestamp}_{clean_title}.md"
    filepath = os.path.join(target_dir, filename)

    # 5. Write file with basic template
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"---\n")
        f.write(f"created: {full_time}\n")
        f.write(f"type: raw\n")
        f.write(f"---\n\n")
        f.write(content)
    
    print(f"✅ Knowledge harvested: {filepath}")

if __name__ == "__main__":
    ingest()
