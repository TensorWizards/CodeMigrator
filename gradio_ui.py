import gradio as gr
from main import codeConvert,codeExplain

def process_files(files,language):
    file_names = files[0]
    instructions =  codeExplain(file_names)
    generated_code = codeConvert(instructions,language)
    return  [instructions, generated_code]

demo = gr.Interface(
    process_files,
    inputs=['files',gr.Dropdown(["python","java"])],
    outputs=["markdown","markdown"],
    allow_flagging="never"
)

demo.launch()