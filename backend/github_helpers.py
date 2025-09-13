from github import Github
from urllib.parse import urlparse

def get_readme_from_repo(repo_url: str):
    try:
        path = urlparse(repo_url).path.strip('/')
        g = Github()  # Can pass token here for higher rate limit
        repo = g.get_repo(path)
        readme = repo.get_readme()
        return readme.decoded_content.decode()
    except Exception as e:
        print(f"GitHub fetch failed: {e}")
        return None

