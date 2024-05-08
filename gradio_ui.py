import gradio as gr
from main import codeConvert

def process_files(files):
    file_names = files[0]
    return codeConvert(file_names)

demo = gr.Interface(
    process_files,
    inputs='files',
    outputs="markdown",
    allow_flagging="never"
)

demo.launch()