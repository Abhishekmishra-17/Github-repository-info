# Github-repository-info

It will provide the latest details of the given repo of a particular owner (using the token of the same owner).

## Table of Contents

- [Overview](#overview)
- [Uses](#uses)
- [Process of Execution](#process-of-execution)
- [Input and Output](#input-and-output)
- [Owner Details](#owner-details)
- [Open for Suggestions](#open-for-suggestions)

## Overview

This project fetches and displays the latest details for any specified GitHub repository of a particular owner, leveraging the owner's personal access token for authentication. It is built in Python and designed for easy use from the command line.

## Uses

- **Repository Insights:** Get up-to-date stats and metadata about your own or others' repositories.
- **Automated Reporting:** Integrate with scripts to fetch repository details for dashboards or daily reports.
- **Monitoring:** Check the health and activity of repositories you maintain or follow.
- **Audit:** Quickly review open issues, forks, and watchers for compliance or activity checks.

## Process of Execution

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Abhishekmishra-17/Github-repository-info.git
    cd Github-repository-info
    ```

2. **Set Up Your Environment**
    - Ensure Python is installed.
    - Install required modules (if a `requirements.txt` is provided):
      ```bash
      pip install -r requirements.txt
      ```
    - Or manually install `PyGithub` if needed:
      ```bash
      pip install PyGithub
      ```

3. **Set Your GitHub Token**
    - Export your GitHub personal access token:
      ```bash
      export GITHUB_TOKEN=your_github_personal_access_token
      ```
      # How to Create a Personal Access Token (PAT) on GitHub

      Follow these steps to generate a personal access token (PAT) for use with GitHub API scripts and tools:
      
      ## 1. Log in to GitHub
      
      Go to [https://github.com/](https://github.com/) and sign in to your account.
      
      ## 2. Go to Settings
      
      - Click your profile picture in the top-right corner.
      - Select **Settings** from the dropdown menu.
      
      ## 3. Open Developer Settings
      
      - Scroll down the left sidebar.
      - Click on **Developer settings**.
      
      ## 4. Select Personal Access Tokens
      
      - Under **Access tokens**, click **Personal access tokens**.
      - Choose either **Fine-grained tokens** (recommended) or **Tokens (classic)**.
      
      ## 5. Generate a New Token
      
      - Click **Generate new token** (choose the type as needed).
      - Fill in the token name, expiration date, and select appropriate scopes/permissions (for repository info, typically `repo`).
      - Click **Generate token** at the bottom.
      
      ## 6. Copy Your Token
      
      - **Copy the token immediately.** You will not be able to see it again after you leave the page.
      
      ## 7. Use Your Token
      
      - Use this token as the `access_token` in your scripts or API requests.
      
      ---
      
      > **Tip:** Keep your token secure. Never share it or commit it to public repositories.
      
      **For more information, see the official documentation:**  
      [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

4. **Run the Script**
    ```bash
    python Repoinfo.py
    ```

## Input and Output

### Input

The script will prompt you to enter:
- **Repository owner** (GitHub username)
- **Repository name**

Example:
```
Enter the repository owner: octocat
Enter the repository name: Hello-World
```

### Output

You’ll receive details such as:
- Repository name and owner
- Description
- Stars, forks, watchers count
- Open issues
- Primary language
- Creation and last updated dates

In addition, you will get the latest commit details as follows:
- Last Commit SHA
- Last Commit Message
- Last Commit Author
- Last Commit Date

Example output:
```
Repository Name: Hello-World
Owner: octocat
Description: My first repository on GitHub!
Stars: 1599
Forks: 1320
Watchers: 1599
Open Issues: 42
Primary Language: Python
Created At: 2011-01-26T19:01:12Z
Last Updated: 2025-07-13T18:00:00Z

Last Commit SHA: 1a2b3c4d5e6f7g8h9i0j
Last Commit Message: Update README with latest instructions
Last Commit Author: The Octocat
Last Commit Date: 2025-07-13T18:00:00Z
```

## Owner Details

- **Owner:** [Abhishekmishra-17](https://github.com/Abhishekmishra-17)
- **Repository:** [Github-repository-info](https://github.com/Abhishekmishra-17/Github-repository-info)

## Open for Suggestions

Feedback and suggestions are welcome!  
If you have ideas for improvements, new features, or spot any bugs, please [open an issue](https://github.com/Abhishekmishra-17/Github-repository-info/issues) or submit a pull request.

---
