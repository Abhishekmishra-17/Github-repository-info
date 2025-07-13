from github import Github
from typing import List

def get_repository_info(owner: str, repo_names: List[str], access_token: str) -> None:
    """
    Fetch and display the latest commit details for the given repositories.

    Args:
        owner (str): GitHub username or organization name.
        repo_names (List[str]): List of repository names.
        access_token (str): Fine-grained personal access token.
    """
    try:
        github_client = Github(access_token)
        user = github_client.get_user()
        for repo_name in repo_names:
            repo_name = repo_name.strip()
            try:
                repo = github_client.get_repo(f"{owner}/{repo_name}")
                default_branch = repo.default_branch
                last_commit = repo.get_commit(sha=default_branch)
                print(f"Repository: {repo.name}")
                print(f"Last Commit SHA: {last_commit.sha}")
                print(f"Last Commit Message: {last_commit.commit.message}")
                print(f"Last Commit Author: {last_commit.commit.author.name}")
                print(f"Last Commit Date: {last_commit.commit.author.date}")
                print("-" * 40)
            except Exception as repo_error:
                print(
                    f"Error fetching repository '{repo_name}'. "
                    "Please check the repository name, access token, and ownership."
                )
                print(f"Details: {repo_error}")
    except Exception as auth_error:
        print("Authentication failed. Please verify your access token and username.")
        print(f"Details: {auth_error}")

def main():
    print(
        "To run this script, ensure that the 'PyGithub' module is installed.\n"
        "Install it using: pip install PyGithub\n"
        "For multiple repositories, enter comma-separated values (e.g., repo1,repo2,repo3).\n"
    )
    owner = input("GitHub Username or Organization: ").strip()
    repo_names = input("Enter Repository Name(s) (comma-separated): ").split(",")
    access_token = input("Fine-grained Personal Access Token: ").strip()
    get_repository_info(owner, repo_names, access_token)

if __name__ == "__main__":
    main()
