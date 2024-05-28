from legacy_to_modern import *
from test_creation import *
from issue_solving import *
import gradio as gr
import time


# orig_repo_name = 'igsci/perceptron'
# repo_name = 'igsci/perceptron-python'


# # file_content, file_name, repo_name = get_github_contents(githubRepo=orig_repo_name)

# # description = codeExplainFromContent(file_content)

# # code_text = codeConvert(description)

# # file_creation(file_name=file_name, code=code_text)

# # create_repo_and_file(repo_name=repo_name, file_name=file_name)

# with open('perceptron.py', 'r') as f:
#     code = f.read()

# create_test_case(code=code)
# run_test_case()

# issue_creation(repo_name=repo_name)

# issue = get_repo_issue(repo_name=repo_name)
# solve_issue(issue=issue, repo_name=repo_name)

# run_test_case_intermediate(repo_name=repo_name)

def repo_handling(git_repo):
    file_content, file_name, repo_name = get_github_contents(githubRepo=git_repo)

    description = codeExplainFromContent(file_content)

    time.sleep(10)

    print("Description generated")

    code = codeConvert(description)

    time.sleep(10)

    print("Code migrated")

    file_creation(file_name=file_name, code=code)

    file_path, modern_repo = create_repo_and_file(repo_name=repo_name, file_name=file_name)

    print("New repository generated")

    test_code = create_test_case(code=code, path=file_path)

    print("Test case generated")

    time.sleep(10)

    run_test_case()

    val = issue_creation(repo_name=modern_repo)

    if val == "Error":
        print("Error found Issue created")
        issue = get_repo_issue(repo_name=modern_repo)
        solve_issue(issue=issue, repo_name=modern_repo, test_code=test_code)
        run_test_case_intermediate(repo_name=modern_repo)


    return ["https://github.com/"+modern_repo, code, test_code]



def error_handling(main_code, repo_name):

    file_creation(file_name="error_file", code=main_code)

    file_path, modern_repo = create_repo_and_file(repo_name=repo_name, file_name="error_file")

    print("New repository generated")

    test_code = create_test_case(code=main_code, path=file_path)

    print("Test case generated")

    time.sleep(10)

    run_test_case()

    val = issue_creation(repo_name=modern_repo)

    if val == "Error":
        print("Error found Issue created")
        issue = get_repo_issue(repo_name=modern_repo)
        solve_issue(issue=issue, repo_name=modern_repo, test_code=test_code)
        run_test_case_intermediate(repo_name=modern_repo)


    return "https://github.com/"+modern_repo



with gr.Blocks(title="CodeTester") as demo:
    gr.Interface(
        repo_handling,
        inputs=['textbox'],
        outputs=["textbox",gr.Code(),gr.Code()],
        allow_flagging="never"
    )

    gr.Interface(
        error_handling,
        inputs = [gr.Code(), 'textbox'],
        outputs=['textbox'],
        allow_flagging="never"
    )


demo.launch()
# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     outputs=["text", "number"],
# )
# if __name__ == "__main__":
#     demo.launch()

