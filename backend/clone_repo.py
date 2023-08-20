import os
import subprocess
import re
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
def extract_user_repo_github(url,user_name,repo_name):
    # Define a regular expression pattern to match GitHub repository URLs
    destination = f"repositories/data/{user_name}_{repo_name}"
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
        return False
    
    return True
