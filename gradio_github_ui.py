import gradio as gr

from main import codeExplain,codeConvert,save_file,codeExplainFromContent,solve_error
from github_handler import  get_github_contents,create_new_repo,save_files_to_repo
from testrun import run_code

instructions = []
generated_code = []
lang = ""
repo_name = ""


def process_files(githubRepo, language):
    global instructions
    global generated_code
    global lang

    lang = language
    instructions.clear()
    generated_code.clear()

    repoContent = get_github_contents(githubRepo)
    
    for content in repoContent:
        instruction = codeExplainFromContent(content)
        instructions.append(instruction)

    for instruction in instructions:
        code = codeConvert(instruction, language)
        generated_code.append(code)

    instructions_str = "\n\n".join(instructions)
    generated_code_str = "\n\n".join(generated_code)

    return [instructions_str, generated_code_str]


def push_github(reponame):
    global repo_name
    global lang
    global generated_code

    repo_name = create_new_repo(reponame)

    for i, code_block in enumerate(generated_code):
        code = strip_first_last_line(code_block)
        save_files_to_repo(repo_name, f"test{i}", code, lang)

    print("Successfully saved all the files to GitHub")


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
    cleaned_code = [strip_first_last_line(code) for code in generated_code]
    save_file(file_name, "\n\n".join(cleaned_code))


def generate_documentation():
    global generated_code
    documentation = ""

    for i, code_block in enumerate(generated_code):
        doc = f"# Documentation for Code Block {i + 1}\n\n"
        doc += "## Code:\n"
        doc += f"```{lang}\n{strip_first_last_line(code_block)}\n```\n\n"
        doc += "## Explanation:\n"
        doc += f"{instructions[i]}\n\n"
        documentation += doc

    return documentation

def generate_tests():
    
    test_results = f""
    global generated_code

    print(generated_code)

    for i in range(len(generated_code)):
        code = strip_first_last_line(generated_code[i])
        error_log = run_code(code)
        solutionCode = solve_error(code,error_log)
        test_results += f"\n\n{error_log}\{solutionCode}"
         

    print(test_results)

    return test_results
        
        


with gr.Blocks(title="CodeMigratorGithub") as demo:
    with gr.Column():
        gr.Interface(
            process_files,
            inputs=['textbox', gr.Dropdown(["python", "java"])],
            outputs=["markdown", "markdown"],
            allow_flagging="never"
        )
        file_name = gr.Textbox(label="Enter New Repo Name")
        btn_savecode = gr.Button("Save Code to GitHub")
        btn_savecode.click(push_github, inputs=file_name)




        btn_generate_doc = gr.Button("Generate Documentation")
        doc_output = gr.Markdown()
        btn_generate_doc.click(generate_documentation, outputs=doc_output)


        btn_run_test = gr.Button("Run Test Programs")
        test_outputs = gr.Textbox()
        btn_run_test.click(generate_tests, outputs=test_outputs)


demo.launch()
