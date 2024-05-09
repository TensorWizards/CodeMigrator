import gradio as gr
from main import codeConvert,codeExplain

def process_files(files):
    file_names = files[0]
    instructions =  codeExplain(file_names)
    return codeConvert(instructions,"java")

demo = gr.Interface(
    process_files,
    inputs='files',
    outputs="markdown",
    allow_flagging="never"
)

demo.launch()