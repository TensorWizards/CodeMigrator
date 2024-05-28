from github import Github
import os
from dotenv import load_dotenv
import google.generativeai as genai
import subprocess
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
API_TOKEN = os.getenv("GEMINI_API_TOKEN")

genai.configure(api_key=API_TOKEN)

model = genai.GenerativeModel('gemini-1.5-pro-latest')


g = Github(GITHUB_TOKEN)

user = g.get_user()

# def get_github_contents(githubRepo):
#     repo = g.get_repo(githubRepo)
#     # repo_name = githubRepo.split("/")[1]

#     contents = repo.get_contents("")

#     for content in contents:
#         if content.type == "file" and content.name.endswith(".py"):
#             file_content = content.decoded_content.decode("utf-8")
#             name = content.name
#             file_name = name.split(".")[0]
            
#             return file_content
        

def create_test_case(code, path):
    prompt = f"""
{code}
the above code is a python file. give a python code that imports this code as a main file and then uses it.
Let the response be a python file in a markdown file do not include output.
Make sure to import all the packages that will be used by the program.
while importing the file name is {path}
"""
    code_response = model.generate_content(prompt)

    mark_text = code_response.text
    lines = mark_text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)

    with open("test.py", 'w') as test_code:
        test_code.write(stripped_text)


    return stripped_text

def run_test_case():
    subprocess.run(["pip", "install", "-r", "requirements.txt", "-q"])
    subprocess.run("python test.py 2> output.log", shell=True)


def run_test_case_intermediate(repo_name):
    subprocess.run("python test.py 2> output.log", shell=True)
    with open('output.log', 'r') as log_file:
        content = log_file.read()

    if content == "":
        repo = g.get_repo(repo_name)
        issues = repo.get_issues(state="open")
        issue = repo.get_issue(issues[0].number)
        issue.edit(state="close")

def issue_creation(repo_name):

    repo = g.get_repo(repo_name)
    with open('output.log', 'r') as log_file:
        content = log_file.read()

    if content:
        repo.create_issue(title="Error", body=content)
        return "Error"
    else:
        return "No Error"

    # elif repo.get_issue(1):
    #     issue = repo.get_issue(1)
    #     issue.edit(state="closed")

        

