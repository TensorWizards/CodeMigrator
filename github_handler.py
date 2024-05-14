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

def create_new_repo(repo_name,description="Demo Description",isPublic=False):

    repo = user.create_repo(
        name=repo_name,
        description=description,
        private = isPublic
    )
    
    return f"igsci/{repo_name}"


def save_files_to_repo(repo_name,filename,filecontent,language):
    repo = g.get_repo(repo_name)

    if language=="python":
        repo.create_file(f"{filename}.py","test",filecontent)
    if language=="java":
        repo.create_file(f"{filename}.java","test",filecontent)
    
