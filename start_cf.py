import subprocess
import re
import time
import sys

def main():
    print("Launching cloudflared with IPv4...")
    cmd = [
        r"c:\Users\ACER\Desktop\docomin\cloudflared.exe",
        "tunnel",
        "--edge-ip-version", "4",
        "--url", "http://127.0.0.1:5000"
    ]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore")
    
    tunnel_url = None
    with open(r"c:\Users\ACER\Desktop\docomin\cf_live.log", "w", encoding="utf-8") as f:
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
            
            m = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
            if m and "api.trycloudflare.com" not in m.group(0) and not tunnel_url:
                tunnel_url = m.group(0)
                print("\n" + "="*50)
                print("FOUND LIVE CLOUDFLARE URL:", tunnel_url)
                print("="*50 + "\n")
                with open(r"c:\Users\ACER\Desktop\ONLINE_WEBSITE_LINK.txt", "w", encoding="utf-8") as out:
                    out.write(tunnel_url)
                with open(r"c:\Users\ACER\Desktop\เปิดเว็บ_Docomin_ออนไลน์.url", "w", encoding="utf-8") as out:
                    out.write(f"[InternetShortcut]\nURL={tunnel_url}\n")
                with open(r"c:\Users\ACER\Desktop\คลิกเปิดเว็บ_Docomin_ออนไลน์.url", "w", encoding="utf-8") as out:
                    out.write(f"[InternetShortcut]\nURL={tunnel_url}\n")

if __name__ == "__main__":
    main()
