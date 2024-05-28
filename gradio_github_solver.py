import gradio as gr


from github_handler import get_first_github_contents,update_code
from testrun import run_code
from main import solve_error,remove_markdown

repo_link = ""
updated_code = ""


def test_update_code(repolink):

    global repo_link
    global updated_code

    repo_link = repolink

    original_code =  get_first_github_contents(repolink)
    logs = run_code(original_code) 

    if logs == "Sucessfully Executed":
        return "Sucessfully Executed" , "" , ""
    else:
        solved_code = solve_error(original_code,logs)
        solved_code = remove_markdown(solved_code)

        updated_code = solved_code

        return logs, original_code, solved_code


def update_code_github():

    global repo_link
    global updated_code

    update_code(repo_link,"Atest.py",updated_code)



with gr.Blocks(title="CodeTester") as demo:
    gr.Interface(
        test_update_code,
        inputs=['textbox'],
        outputs=["textbox",gr.Code(),gr.Code()],
        allow_flagging="never"
    )

    btn_update = gr.Button("Update Code in Github")
    btn_update.click(update_code_github)


demo.launch()