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


def get_github_contents(githubRepo):
    repo = g.get_repo(githubRepo)
    repo_name = githubRepo.split("/")[1]

    contents = repo.get_contents("")

    for content in contents:
        if content.type == "file":
            file_content = content.decoded_content.decode("utf-8")
            name = content.name
            file_name = name.split(".")[0]
            
            return file_content, file_name, repo_name
        
def codeExplainFromContent(content):

    description_prompt = f"You will be given legacy code as input. You need to understand the entire code and generate detailed description of it such that the description generated explains all the variables, routines, classes, blocks or other structures present in the legacy code. \n{content}"
    description_response = model.generate_content(description_prompt)

    return description_response.text

def codeConvert(instructions,language = "python"):

    code_prompt = (
    f"You need to write a {language} code based on the given description such that the entire description provided is followed "
    f"without any loss in programming feature. Your response should be a single python markdown implementing "
    f"using relevant libraries for that task.\nDescription: {instructions}"
    f"Let the response contain only code in markdown format. Don't include any example usage."
    )

    code_response = model.generate_content(code_prompt)

    mark_text = code_response.text
    lines = mark_text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)

    return stripped_text

def file_creation(file_name, code):
    with open(f"{file_name}.py", 'w') as code_file:
        code_file.write(code)

    prompt = """{code}
    Give all packages used in the code in the format of requirements.txt. Do not include any explanation. Just the name of the packages. Let the response be in markdown.
    """
    requirement = model.generate_content(prompt)
    mark_text = requirement.text
    lines = mark_text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)

    with open('requirements.txt', 'w') as text_file:
        text_file.write(stripped_text)

def create_repo_and_file(repo_name,description="Demo Description",isPrivate=False, file_name=None):
    new_repo_name = repo_name+"-python"
    repo = user.create_repo(
        name= new_repo_name,
        description=description,
        private = isPrivate
    )
    file_path = f"{file_name}.py"
    commit_msg = f"{file_name} upload"
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, commit_msg, content, branch="main")

    with open('requirements.txt', 'r') as file:
        req_content = file.read()

    repo.create_file('requirements.txt', "requirements_file", req_content, branch="main")

    return file_path, "igsci/"+new_repo_name



