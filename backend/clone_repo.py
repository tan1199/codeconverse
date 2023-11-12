import os
import subprocess
import re
import requests

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def extract_user_repo_github(url, user_name, repo_name, username):
    # Define a regular expression pattern to match GitHub repository URLs
    default_branch=""
    api_url = f'https://api.github.com/repos/{user_name}/{repo_name}'
    response = requests.get(api_url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        default_branch = data.get('default_branch')
    else:
        return False,default_branch
    destination = f"repositories/{username}/data/{user_name}_{repo_name}"
    create_folder(destination)  
    try:
        result = subprocess.run(["git", "clone", url, destination], capture_output=True, text=True, check=True)
        # 'check=True' raises a CalledProcessError if the command exits with a non-zero status
        # 'capture_output=True' captures the standard output and standard error

        # Print the output
        print("Clone Output:", result.stdout)
        
    except subprocess.CalledProcessError as e:
        # An error occurred, print the error message
        print("Error cloning repository nopes:", e.stderr)
        return False,default_branch
    
    return True,default_branch
