import openai
import os
import subprocess
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DeepLake

current_directory = r'C:\Users\Tanmay Saini\Desktop\codeconverse\backend\repos'
print("dfgdfg "+current_directory)

def clone_repository(local_path):
    """Clone the specified git repository to the given local path."""
    subprocess.run(["git", "clone", "https://github.com/peterw/Chat-with-Github-Repo", local_path])

clone_repository(current_directory)