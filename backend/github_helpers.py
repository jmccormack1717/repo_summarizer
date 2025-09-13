import os
from github import Github
from urllib.parse import urlparse

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_readme_from_repo(repo_url: str):
    try:
        path = urlparse(repo_url).path.strip('/')
        if GITHUB_TOKEN:
            g = Github(GITHUB_TOKEN)  # Authenticated client with token
        else:
            g = Github()  # Unauthenticated client

        repo = g.get_repo(path)
        readme = repo.get_readme()
        return readme.decoded_content.decode()
    except Exception as e:
        print(f"GitHub fetch failed: {e}")
        return None
