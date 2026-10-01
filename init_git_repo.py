import os
from dulwich import porcelain

repo_dir = os.path.abspath(os.path.dirname(__file__))

# 1. Init git repo if not already initialized
git_dir = os.path.join(repo_dir, '.git')
if not os.path.exists(git_dir):
    repo = porcelain.init(repo_dir)
    print("Initialized empty Git repository in", repo_dir)
else:
    repo = porcelain.open_repo(repo_dir)
    print("Opened existing Git repository in", repo_dir)

# 2. Add files
porcelain.add(repo_dir)
print("Added all files to staging")

# 3. Commit
try:
    commit_id = porcelain.commit(
        repo_dir,
        message=b"Initial commit: Docomin Thai Education Platform (Grades 1-12, 77 Provinces, O-NET)",
        author=b"Docomin <admin@docomin.th>",
        committer=b"Docomin <admin@docomin.th>"
    )
    print("Committed successfully! Commit hash:", commit_id.decode() if isinstance(commit_id, bytes) else commit_id)
except Exception as e:
    print("Commit status:", str(e))
