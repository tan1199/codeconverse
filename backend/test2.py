from count_token import num_tokens_from_string
x=num_tokens_from_string("""
from .ast_parser import ASTParser
import pyparsing
class BaseUtility():

    def __init__(self, language: str):
        self.language = language
        self.parser = ASTParser(language) 
    
    def parse(self, code_snippet):
        tree = self.parser.parse(bytes(code_snippet, "utf8"))
        return tree

    def remove_comments(self, code_snippet):
        if self.language == "python":
            commentFilter = pyparsing.pythonStyleComment.suppress()
        elif self.language == "c":
            commentFilter = pyparsing.cStyleComment.suppress()
        elif self.language == "cpp":
            commentFilter = pyparsing.cppStyleComment.suppress()
        else:
            commentFilter = pyparsing.javaStyleComment.suppress()
        
        code_snippet = commentFilter.transformString(code_snippet)
        return code_snippet
                         ""","cl100k_base")
print(x)
import code_splitter
import os
from pathlib import Path
# List the contents of the module
print(dir(code_splitter))
repo_path = os.path.join("root", "repositories", "repo_name")
print(type(repo_path))
root1 = Path(__file__).parent
def is_empty_file(filepath):
    return os.path.exists(filepath) and os.path.getsize(filepath) == 0

file_path = Path(os.path.join(root1,"repositories/data/Chat-with-Github-Repo-main/src/__init__.py"))
if is_empty_file(file_path):
    print("The file is empty.")
else:
    print("The file is not empty.")
