import gradio as gr
from main import codeConvert,codeExplain,save_file

instructions = ""
generated_code = ""

def process_files(files,language):
    file_names = files[0]
    global instructions
    global generated_code
    instructions =  codeExplain(file_names)
    generated_code = codeConvert(instructions,language)
    return  [instructions, generated_code]

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
    
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=4, min_width=600):
            gr.Interface(
                process_files,
                inputs=['files',gr.Dropdown(["python","java"])],
                outputs=["markdown","markdown"],
                allow_flagging="never"
            )

            
            file_name = gr.Textbox(label="File Name")
            btn_savecode = gr.Button("Save Code")
            btn_savecode.click(save_code,inputs=file_name)


demo.launch()