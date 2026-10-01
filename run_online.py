import subprocess
import re
import time
import os

def test_pinggy():
    print("Testing pinggy via ssh...")
    try:
        # pinggy works with simple ssh command without any registration
        cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=30", "-p", "443", "-R0:localhost:5000", "a.pinggy.io"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore")
        t0 = time.time()
        while time.time() - t0 < 8:
            line = p.stdout.readline()
            if not line:
                time.sleep(0.2)
                continue
            print("Pinggy:", line.strip())
            match = re.search(r"https://[a-zA-Z0-9-]+\.a\.pinggy\.link", line)
            if match:
                url = match.group(0)
                print("FOUND PINGGY URL:", url)
                return p, url
        p.kill()
    except Exception as e:
        print("Pinggy error:", e)
    return None, None

def test_localhost_run():
    print("Testing localhost.run...")
    try:
        cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:localhost:5000", "nokey@localhost.run"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore")
        t0 = time.time()
        while time.time() - t0 < 8:
            line = p.stdout.readline()
            if not line:
                time.sleep(0.2)
                continue
            print("LHR:", line.strip())
            match = re.search(r"https://[a-zA-Z0-9-]+\.lhr\.life", line)
            if match:
                url = match.group(0)
                print("FOUND LHR URL:", url)
                return p, url
        p.kill()
    except Exception as e:
        print("LHR error:", e)
    return None, None

def test_cloudflared():
    print("Testing cloudflared...")
    try:
        cmd = [r"c:\Users\ACER\Desktop\docomin\cloudflared.exe", "tunnel", "--url", "http://127.0.0.1:5000"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="ignore")
        t0 = time.time()
        while time.time() - t0 < 15:
            line = p.stdout.readline()
            if not line:
                time.sleep(0.2)
                continue
            print("CF:", line.strip())
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
            if match and "api.trycloudflare.com" not in match.group(0):
                url = match.group(0)
                print("FOUND CF URL:", url)
                return p, url
        p.kill()
    except Exception as e:
        print("CF error:", e)
    return None, None

if __name__ == "__main__":
    proc, url = test_cloudflared()
    if not url:
        proc, url = test_pinggy()
    if not url:
        proc, url = test_localhost_run()
        
    if url:
        with open(r"c:\Users\ACER\Desktop\docomin\ONLINE_URL.txt", "w", encoding="utf-8") as f:
            f.write(url)
        print("SUCCESS! Online URL saved to ONLINE_URL.txt:", url)
        # Keep process running forever
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            proc.kill()
    else:
        print("Could not find active tunnel URL.")
