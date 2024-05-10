import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')



def codeExplain(filepath):
  with open(filepath, 'r') as file:
    content = file.read()


  prompt1 = f"Exlain me this code:\n{content}"
  explainCobol = model.generate_content(prompt1)

  return explainCobol.text

def strip_first_last_line(text):
    lines = text.splitlines()
    stripped_lines = lines[1:-1]
    stripped_text = '\n'.join(stripped_lines)
    return stripped_text

def codeConvert(instructions,language):

  prompt2 = f"Generate a {language} Code using Following Instruction :\n{instructions}"
  codeJava = model.generate_content(prompt2)

  generated_code =  codeJava.text

  return strip_first_last_line(generated_code)  # removes markdown


def save_file(filename,data):
  folder_path = './samples/' 
  file_name = filename 
  file_path = os.path.join(folder_path, file_name) 
  
  # Create the file 
  with open(file_path, 'w') as file: 
      file.write(data)




