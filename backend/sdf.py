import requests
import subprocess
from pathlib import Path
import os
API_KEY = os.getenv("OPENAI_API_KEY")
print(API_KEY)


def get_default_branch(repo_owner, repo_name):
    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        default_branch = data.get('default_branch')
        return default_branch
    else:
        print(
            f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None


# Replace 'owner' and 'repo' with the actual owner and repository name
repo_owner = 'go-vgo'
repo_name = 'robotgo'

default_branch = get_default_branch(repo_owner, repo_name)

if default_branch:
    print(
        f"The default branch of {repo_owner}/{repo_name} is: {default_branch}")
else:
    print("Failed to retrieve the default branch.")

root = Path(__file__).parent
# Replace "/path/to/delete" with the actual path you want to delete
directory_to_delete = "C:\\Users\\Tanmay Saini\\Desktop\\codeconverse"

# Construct the command
command = ["ls", "-l", root]

# Run the command
result = subprocess.run(command, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, text=True)

# Check the result
if result.returncode == 0:
    print("Directory deleted successfully.")
else:
    print(f"Error: {result.stderr}")
