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
# List the contents of the module
print(dir(code_splitter))
repo_path = os.path.join("root", "repositories", "repo_name")
print(type(repo_path))