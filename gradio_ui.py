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

def save_code(file_name):
    global generated_code
    save_file(file_name,generated_code)

# demo = gr.Interface(
#     process_files,
#     inputs=['files',gr.Dropdown(["python","java"])],
#     outputs=["markdown","markdown"],
#     allow_flagging="never"
# )

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            gr.Interface(
                process_files,
                inputs=['files',gr.Dropdown(["python","java"])],
                outputs=["markdown","markdown"],
                allow_flagging="never"
            ) 
        with gr.Column(scale=2, min_width=600):

            gr.Interface(
                save_code,
                inputs=[gr.Textbox()],
                outputs=None,
                allow_flagging="never"
            ) 

demo.launch()