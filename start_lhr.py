import subprocess
import re
import time
import sys

def main():
    print("Connecting to localhost.run tunnel...")
    cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ServerAliveInterval=30",
        "-R", "80:localhost:5000",
        "nokey@localhost.run"
    ]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore")
    
    online_url = None
    with open(r"c:\Users\ACER\Desktop\docomin\lhr_output.txt", "w", encoding="utf-8") as f:
        while True:
            line = p.stdout.readline()
            if not line:
                if p.poll() is not None:
                    break
                time.sleep(0.1)
                continue
            f.write(line)
            f.flush()
            print(line, end="", flush=True)
            
            # match any url containing lhr.life or localhost.run
            m = re.search(r"https://[a-zA-Z0-9.-]+\.lhr\.life", line)
            if not m:
                m = re.search(r"https://[a-zA-Z0-9.-]+\.localhost\.run", line)
            if m and not online_url:
                online_url = m.group(0)
                print("\n" + "="*50)
                print("FOUND LIVE URL:", online_url)
                print("="*50 + "\n")
                with open(r"c:\Users\ACER\Desktop\docomin\ONLINE_URL.txt", "w", encoding="utf-8") as uf:
                    uf.write(online_url)

if __name__ == "__main__":
    main()
