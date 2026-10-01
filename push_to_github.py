import os
import sys
from dulwich import porcelain

def push_repo(remote_url, branch="main"):
    repo_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        porcelain.push(repo_dir, remote_url, branch)
        print("Successfully pushed to GitHub repository:", remote_url)
    except Exception as e:
        print("Push error:", str(e))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        remote_url = sys.argv[1]
        push_repo(remote_url)
    else:
        print("Usage: py push_to_github.py https://<TOKEN>@github.com/<USERNAME>/<REPO>.git")
