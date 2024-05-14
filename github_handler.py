from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'your_github_token_here' with your GitHub personal access token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Authenticate with your GitHub token
g = Github(GITHUB_TOKEN)

# Get the authenticated user
user = g.get_user()

# Create a new repository
repo_name = "MyNewRepository"
description = "This is my new repository created with PyGithub"
private = False  # Set to True for a private repository

# # Create the repository
# repo = user.create_repo(
#     name=repo_name,
#     description=description,
#     private=private,
#     has_issues=True,  # Enable issues
#     has_wiki=True,  # Enable wiki
#     has_downloads=True,  # Enable downloads
#     auto_init=True,  # Initialize with a README
# )


def get_github_contents(githubRepo):
    repo = g.get_repo(githubRepo)

    # Get the contents of the repository
    contents = repo.get_contents("")

    # Iterate over the contents and read each file

    files_list = []

    for content in contents:
        if content.type == "file":
            file_content = content.decoded_content.decode("utf-8")
            
            files_list.append(file_content)
        
    return files_list

def create_new_repo_save_files(repo_name,description="Demo Description",isPublic=False):
    repo = user.create_repo(
        name=repo_name,
        description=description,
        private = isPublic
    )
    print(f"New Repository {repo.name} sucessfully created")
        
