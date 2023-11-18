# Filename: check_commits.py
import requests
import subprocess

def get_latest_commit_sha():
    repo_url = "https://github.com/janisha42/CI-CDRepro.git"
    response = requests.get(repo_url)
    commits = response.json()

    if commits:
        latest_commit_sha = commits[0]['sha']
        return latest_commit_sha
    else:
        return None

def get_stored_commit_sha():
    try:
        with open("latest_commit.txt", "r") as file:
            stored_commit_sha = file.read().strip()
            return stored_commit_sha
    except FileNotFoundError:
        return None

def save_latest_commit_sha(commit_sha):
    with open("latest_commit.txt", "w") as file:
        file.write(commit_sha)

def main():
    latest_commit_sha = get_latest_commit_sha()
    stored_commit_sha = get_stored_commit_sha()

    if latest_commit_sha and latest_commit_sha != stored_commit_sha:
        print("New commits found!")
        save_latest_commit_sha(latest_commit_sha)
        # You can add additional actions here
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()
