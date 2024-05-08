import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

# Read file 

file_path = ''

content = ""
with open('./samples/helloworld.cbl', 'r') as file:
  content = file.read()


prompt1 = f"Exlain me this code:\n{content}"
explainCobol = model.generate_content(prompt1)



prompt2 = f"Generate a Java Code using Following Instruction :\n{explainCobol.text}"
codeJava = model.generate_content(prompt2)

print(codeJava.text)