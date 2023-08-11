import tiktoken
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
print(num_tokens_from_string("""
  def test_child_by_field_id(self):
        parser = Parser()
        parser.set_language(PYTHON)
        tree = parser.parse(b"def foo():\n  bar()")
        root_node = tree.root_node
        fn_node = tree.root_node.children[0]
""", "gpt2"))



# Replace 'your_file_path.txt' with the actual path to your text file
file_path = r'D:\chromedownloads\qwe.txt'

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Split the content by two line breaks ('\n\n') and convert it to a list
result_list = file_content.split('def')

# Print the resulting list
for i in range(len(result_list)):
    result_list[i]="def"+result_list[i]
    print("oo")
    print(result_list[i])
    print("pp")

