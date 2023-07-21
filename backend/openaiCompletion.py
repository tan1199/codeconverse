import openai
from keys.api_key import API_KEY
openai.api_key=API_KEY
prompt="""classify the following tweet sentiment as positive or negative
Tweet: I pity the new Batman movie!
sentiment:"""
# response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=6)

def getresponse_from_openai_api(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
  prompt=prompt,
    temperature=0.1,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].text


# def getresponse_from_openai_api(prompt):

#     completion = openai.ChatCompletion.create(
#   model = 'gpt-3.5-turbo',
#   messages = [
#     {'role': 'user', 'content': prompt}
#   ],
#   temperature = 0  
# )
#     return completion['choices'][0]['message']['content']