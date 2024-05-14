import os
from dotenv import load_dotenv
from hugchat import hugchat
from hugchat.login import Login

load_dotenv()
EMAIL=os.getenv('EMAIL')
PASSWD=os.getenv('PASSWD')

cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

chatbot.get_available_llm_models()
chatbot.switch_llm(0)
chatbot.new_conversation(switch_to = True)


with open("./samples/TicTacTOBOL.cbl", 'r') as file:
    content = file.read()

prompt = f"You will be given legacy code as input. You need to understand the entire code and generate detailed description for code such  that the description generated explains all the variables, routines, classes, blocks or other structures present in the legacy code and if there are any hardcoded input values mentioned in the code show it in the description and how the code actually works. \n{content}"
  
query_result = chatbot.chat(prompt)
print(query_result)