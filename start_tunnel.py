import subprocess
import re
import time
import sys

def main():
    print("Starting cloudflared tunnel...")
    process = subprocess.Popen(
        [r"c:\Users\ACER\Desktop\docomin\cloudflared.exe", "tunnel", "--url", "http://127.0.0.1:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    url = None
    start_time = time.time()
    
    with open(r"c:\Users\ACER\Desktop\docomin\tunnel_log.txt", "w", encoding="utf-8") as log_file:
        while True:
            line = process.stdout.readline()
            if not line:
                if process.poll() is not None:
                    break
                time.sleep(0.1)
                continue
            
            log_file.write(line)
            log_file.flush()
            print(line, end="")

            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
            if match and not url:
                url = match.group(0)
                print(f"\n==========================================")
                print(f"FOUND TUNNEL URL: {url}")
                print(f"==========================================\n")
                with open(r"c:\Users\ACER\Desktop\docomin\tunnel_url.txt", "w", encoding="utf-8") as uf:
                    uf.write(url)

            # keep running so tunnel stays alive
            if process.poll() is not None:
                break

if __name__ == "__main__":
    main()
