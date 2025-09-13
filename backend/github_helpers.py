import os
from github import Github  # PyGithub library for accessing GitHub API
from urllib.parse import urlparse  # To extract path from full GitHub URL

# Load GitHub token from environment variable (optional but recommended)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_readme_from_repo(repo_url: str):
    """
    Given a GitHub repository URL, fetches and returns the decoded README content.

    Args:
        repo_url (str): The full URL to a GitHub repository.

    Returns:
        str | None: The decoded README content, or None if the fetch fails.
    """
    try:
        # Extract "owner/repo" from the full URL
        path = urlparse(repo_url).path.strip('/')  # e.g., "numpy/numpy"

        # Create a GitHub client, using a personal access token if available
        if GITHUB_TOKEN:
            g = Github(GITHUB_TOKEN)  # Authenticated client (higher rate limits)
        else:
            g = Github()  # Unauthenticated client (lower rate limits)

        # Get the repo object from GitHub
        repo = g.get_repo(path)

        # Fetch the README file and decode its content
        readme = repo.get_readme()
        return readme.decoded_content.decode()

    except Exception as e:
        # Log the error and return None if anything goes wrong
        print(f"GitHub fetch failed: {e}")
        return None
