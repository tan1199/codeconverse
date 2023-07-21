from openaiCompletion import getresponse_from_openai_api


def completion_endpoint_plain(prompt):
    return getresponse_from_openai_api(prompt)