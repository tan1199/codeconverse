import openai
from keys.api_key import API_KEY
from langchain.document_loaders import TextLoader
# from tenacity import (
#     retry,
#     stop_after_attempt,
#     wait_random_exponential,
# )  
# openai.api_key = API_KEY
# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx", API_KEY)
prompt="""classify the following tweet sentiment as positive or negative
Tweet: I pity the new Batman movie!
sentiment:"""
# response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=6)

# def getresponse_from_openai_api(prompt):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#   prompt=prompt,
#     temperature=0.1,
#     max_tokens=3900,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     return response.choices[0].text


# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def getresponse_from_openai_api(prompt, apikey):
   openai.api_key=apikey
   try:
    completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': prompt}
  ],
  temperature = 0  
)
    response = completion['choices'][0]['message']['content']
   except Exception as e:
    print("lllll")
    response = "##error##"+ str(e)
    print("reee ",response)
   return response