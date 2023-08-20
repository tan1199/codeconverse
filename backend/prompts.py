metadata_json_prompt="""
You will get a user query regarding a codebase .The user query can contain multiple instructions.
First you will split all the instruction and list them. Make sure that each instruction makes sense on its own. Do not add anythong which is not provided in the user query, but if suppose
the subsequent instruction are dependent on previous ones then please incorporate relevant information from them into the current one.
Make sure to replace pronouns in the instruction from the context available do that each instuction makes sense on its own
Just extract the instructions from the following user query and add them under instructions key in ```json```,each instruction will have its own json.
Then try to understand the objective of each instruction and assign command a command from {"explain","compare","fetch" }
if the instruction contains fetch and explain or compare and explain then command will be explain and compare respectively
Now extract metadata present in the instruction,
metadata can be in the form of function name/ method name, class name and file name, only populate te metadata value if u are certain, analyze the instruction and then if you can conclusively decide
that a certain value of metadata is present than use that value otherwise assume 'NA', if you want to decide for function_name then look for the keyword function or method, function_name will generally
precede or follow the key word funcion/method, similarlay for class_name look for words coming just before or after class. for filename look for words ending with extension or words coming before /after the word file;
If you do not find these influencing keywords please populate the value as 'NA'
Just extract the instructions,command and metadata from the following user query and output only in ```json```,each instruction will have its own json.
the metadata will be dictionary of key value pairs, the keys being function_name, class_name and file_name.
If the instruction is compare then there will be multiple values of function_name/class_name/file_name, so split the instruction into two instructions, first one contains
the first enitity for comparision and second instruction refers to the second enitiy of comparision and extract the relevant metadata and other keys for respective entities ib the both instructions.
remember that method name is interchangeably used for the function name
Finally populate the last key called additional_info, if you think intruction is to fetch or explain entire content or complete file, instead of a specific functionality or part then the value is 'Y' otherwise the default value is 'N' 
else if you think instruction is to fetch or explain all the functions present in a class or file then then the value is 'function_all'
else if you think instruction is to fetch or explain all the classes present in a file then then the value is 'class_all'
else if you think instruction is to fetch or explain all the imports or dependencies present in a specific file then then the value is 'import_all'
Sample json output
{
  "instructions": [
    {
      "instruction": "NA",
      "command": "NA",
      "metadata": {
        "function_name": "NA",
        "class_name": "NA",
        "file_name": "NA"
      },
      "additional_info": "N"
    },
    {
      "instruction": "NA",
      "command": "NA",
      "metadata": {
        "function_name": "NA",
        "class_name": "NA",
        "file_name": "NA"
      },
      "additional_info": "N"
	   
    }
  ]
}
	
Think step by step and reason yourself to the right decisions to make sure we only split into multiple instructions if we have conclusive evidence to do so and when we do each instruction should make sense on its own, we derive relevant information from previous instructions if required,
and also make sure you extract the metadata efficiently in the format explained above. The metadata values will not contain any space.

"""
