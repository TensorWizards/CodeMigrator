from github import Github
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
API_TOKEN = os.getenv("GEMINI_API_TOKEN")

genai.configure(api_key=API_TOKEN)

model = genai.GenerativeModel('gemini-1.5-pro-latest')


g = Github(GITHUB_TOKEN)

user = g.get_user()

def get_repo_issue(repo_name):
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state="open")
    issue = repo.get_issue(issues[0].number)

    return issue

def solve_issue(issue, repo_name, test_code):
    repo = g.get_repo(repo_name)
    
    contents = repo.get_contents("")

    for content in contents:
        if content.type == "file" and content.name.endswith(".py"):
            file_content = content.decoded_content.decode("utf-8")
            name = content.name
            prompt = f"""{file_content}
produced the following error
{issue.body}
Solve this issue and give the updated python code.
let the response be python code in markdown state donot include any explanation.
 """
            response = model.generate_content(prompt)

            mark_text = response.text
            lines = mark_text.splitlines()
            stripped_lines = lines[1:-1]
            stripped_text = '\n'.join(stripped_lines)

            with open(f"{name}", 'w') as edited_file:
                edited_file.write(stripped_text)

def close_issue(issue):
    issue.close()