from openaiCompletion import getresponse_from_openai_api


def completion_endpoint_plain(prompt,apikey):
    print("making request to openai")
    return getresponse_from_openai_api(prompt,apikey)
