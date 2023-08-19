from github import Github

def get_repository_info(owner: str, repo_name: list, access_token: str) -> None:
    # try:
    g = Github(owner, access_token)
    # get the authenticated user
    user = g.get_user()
    for repo_name_item in repo_name:
        # print(repo_name_item.strip())
        try:
            repo=g.get_repo(f"{owner}/{repo_name_item}")
            # print(repo)
            default_branch =repo.default_branch
            last_commit = repo.get_commit(sha=default_branch)
            last_commit_sha =last_commit.sha
            last_commit_message = last_commit.commit.message
            last_commit_author = last_commit.commit.author.name
            last_commit_date = last_commit.commit.author.date
            print(f"Repository: {repo.name}")
            print(f"Last Commit SHA: {last_commit_sha}")
            print(f"Last Commit Message: {last_commit_message}")
            print(f"Last Commit Author: {last_commit_author}")
            print(f"Last Commit Date: {last_commit_date}")
            print("-"*40)
                
        except Exception as e:
            print("Getting error while authenticating the account and repository. Please check Fine-grained personal access token and GitHub Username. Make sure that repository is present in the account and you are the owner of the same.")
            print("For more info see the error below:")
            print(f"Error: {e}")

if __name__ == "__main__":
    print("* To run this script, please make sure that PyGithub module is already installed in the system. For the installation of the same, use the 'pip install PyGithub'.")
    print("* In case of multiple repositories, user must be enter the comma separated value.\n* For Example:\n repo_name1,repo_name2,repo_name3: This type of inputs are correct \n repo_name1, repo_name2, repo_name3: This type input are not correct \n\n")
    owner = str(input("GitHub Username:\t")) # Replace with the GitHub username
    repo_name = input("Enter The Repository Name:\t").split(",")
    access_token = str(input("Fine-grained personal access token:\t")) # Replace with your personal Fine-grained personal access token
    get_repository_info(owner, repo_name, access_token)
