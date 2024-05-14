import gradio as gr

from main import codeExplain,codeConvert,save_file,codeExplainFromContent
from github_handler import  get_github_contents,create_new_repo_save_files

instructions = ""
generated_code = ""


def process_files(githubRepo,language):
    global instructions
    global generated_code

    repoContent = get_github_contents(githubRepo)
    repoContent = repoContent[0]

    instructions = codeExplainFromContent(repoContent)
    generated_code = codeConvert(instructions,language)

    return [instructions,generated_code]



def strip_first_last_line(text):
    """
    Removes markdown
    """
    lines = text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)
    return stripped_text



#Feature yet to be implemented.Temporarily we are just saving files in local directory
#This Feature will create a new repo and publish it to Github


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
    
    file_name = gr.Textbox(label="File Name")
    btn_savecode = gr.Button("Save Code")
    btn_savecode.click(save_code,inputs=file_name)


demo.launch()