from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_name = "TheBloke/CodeLlama-7B-Instruct-GGUF"
model_file = "codellama-7b-instruct.Q4_K_M.gguf"

model_path = hf_hub_download(model_name, filename=model_file)

model_kwargs = {
  "n_ctx":4096,    # Context length to use
  "n_threads":4,   # Number of CPU threads to use
  "n_gpu_layers":0,# Number of model layers to offload to GPU. Set to 0 if only using CPU
}

## Instantiate model from downloaded file
llm = Llama(model_path=model_path, **model_kwargs)

generation_kwargs = {
    "max_tokens":200, # Max number of new tokens to generate
    "stop":["<|endoftext|>", "</s>"], # Text sequences to stop generation on
    "echo":False, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

def get_response(prompt):
    res = llm(prompt, **generation_kwargs)
    return res["choices"][0]["text"]