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

def codeConvert(instructions,language):

  prompt2 = f"Generate a {language} Code using Following Instruction :\n{instructions}"
  codeJava = model.generate_content(prompt2)

  return codeJava.text