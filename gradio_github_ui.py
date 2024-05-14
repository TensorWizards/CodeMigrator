import gradio as gr

from main import codeExplain,codeConvert,save_file,codeExplainFromContent
from github_handler import  get_github_contents,create_new_repo,save_files_to_repo

instructions = []
generated_code = []
lang = ""
repo_name = ""


def process_files(githubRepo,language):
    global instructions
    global generated_code
    global lang

    lang = language
    instructions.clear()
    generated_code.clear()


    repoContent = get_github_contents(githubRepo)
    repoContent = repoContent

    
    for j in range(len(repoContent)):
        i = codeExplainFromContent(repoContent[j])
        instructions.append(i)

    for j in range(len(instructions)):
        g = codeConvert(instructions[j],language)
        generated_code.append(g)

    instructions_str = ""
    generated_code_str = ""

    for i in range(len(instructions)):
        instructions_str += f"\n\n{instructions[i]}"

    for i in range(len(generated_code)):
        instructions_str += f"\n\n{generated_code[i]}"

    return [instructions_str,generated_code_str]


def push_github(reponame):

    global repo_name
    global lang
    global generated_code

    repo_name = create_new_repo(reponame)

    for i in range(len(generated_code)):
        code = strip_first_last_line(generated_code[i])
        save_files_to_repo(repo_name,f"test{i}",code,lang)

    print("Sucessfully saved all the files to github")



def strip_first_last_line(text):
    """
    Removes markdown
    """
    lines = text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)
    return stripped_text



def save_code(file_name):
    global generated_code
    generated_code = strip_first_last_line(generated_code)
    save_file(file_name,generated_code)
    
with gr.Blocks(title="CodeMigratorGithub") as demo:
    gr.Interface(
        process_files,
        inputs=['textbox',gr.Dropdown(["python","java"])],
        outputs=["markdown","markdown"],
        allow_flagging="never"
    )
    
    file_name = gr.Textbox(label="Enter New Repo Name")
    btn_savecode = gr.Button("Save Code to Github")
    btn_savecode.click(push_github,inputs=file_name)




demo.launch()