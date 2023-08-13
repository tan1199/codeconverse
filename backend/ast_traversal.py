

# Generate a random UUID
random_uuid = uuid.uuid4()
random_uuid


def traverse_ast(node,file_extension,current_path,function_definition,method_definition,class_definition,field_definition,decorated_definition,root_node_type,block_child_list,identifier_index):
    print("mnb")
    node_type=node.type
    node_name=node.text
    parent=node.parent
    child_count=node.child_count
    if node.has_error:
      has_error='Y'
    else:
      has_error='N'
    prev_sibling="Previous sibling does not exist"
    next_sibling="Next sibling does not exist"
    # Print information about the current node
    print(f"Node Type: {node.type}")
    print(f"Node Text: {node.text}")
    print(f"Start Point: {node.start_point}")
    print(f"End Point: {node.end_point}")
    print(f"Child Count: {node.child_count}")
    print(f"Named Child Count: {node.named_child_count}")
    print(f"Has Error: {node.has_error}")
    print(f"Is Missing: {node.is_missing}")
    print(f"Is Named: {node.is_named}")
    print(f"children_by_field_name: {node.children_by_field_name}")
    if node.prev_sibling is not None:
      # print(f"prev_sibling: {node.prev_sibling.text.decode()}")
      # prev_sibling=node.prev_sibling.text.decode()
      if node.prev_sibling.text.decode() not in (";","{","}"):
        prev_sibling=node.prev_sibling.text.decode()
      else:
        if node.prev_sibling.prev_sibling is not None:
          prev_sibling=node.prev_sibling.prev_sibling.text.decode()
        else:
          next_sibling="Previous sibling does not exist"

    if node.next_sibling is not None:
      if node.next_sibling.text.decode() not in (";","{","}"):
        next_sibling=node.next_sibling.text.decode()
      else:
        if node.next_sibling.next_sibling is not None:
          next_sibling=node.next_sibling.next_sibling.text.decode()
        else:
          next_sibling="Next sibling does not exist"

      # # print(f"next sibling: {node.next_sibling.text.decode()}")
      # next_sibling=node.next_sibling.text.decode()
    print(f"parent: {node.parent}")
    # Recursively traverse child nodes
    lexical_function=False
    field_definition_arg=field_definition
    if node_type=='lexical_declaration' and node.children[1].children[2].type=='arrow_function':
      print("lexo")
      lexical_function=True
    if node_type=='mod_item' and 'declaration_list' in [child.type for child in node.children]:
      field_definition="mod_item"
      print("45456",node.type,field_definition)
    global df,file_name,file_path,concat
    if node_type in(function_definition,method_definition,class_definition,field_definition) or lexical_function:
      if file_extension ==".cpp":
        if node.type in (class_definition):
          for child in node.children:
            if child.type=='type_identifier':
              code_identifier = child.text.decode()
        else:
          for child in node.children:
            if child.type in ('function_declarator','pointer_declarator'):
              code_identifier = child.children[0].text.decode()
      if file_extension in (".py",".java"):
        for child in node.children:
          if child.type=='identifier':
            code_identifier = child.text.decode()
      if file_extension ==".rs":
        if node.type in (function_definition,"mod_item"):
          for child in node.children:
            if child.type=='identifier':
              code_identifier = child.text.decode()
        else:
          for child in node.children:
            print("90900",node.type,child.type,field_definition)
            if child.type=='type_identifier':
              code_identifier = child.text.decode()
      if file_extension ==".js":
        print("uiui")
        if node.type in (function_definition,class_definition):
          for child in node.children:
            if child.type=='identifier':
              code_identifier = child.text.decode()
        elif lexical_function:
          for child in node.children:
            if child.type in ('variable_declarator'):
              code_identifier = child.children[0].text.decode()
        else:
          print("rtrt")
          for child in node.children:
            if child.type in ('property_identifier','variable_declarator'):
              code_identifier = child.text.decode()
    elif node_type ==decorated_definition:
      code_identifier = node.children[child_count-1].text.decode()
    else:
      print("uiouio")
      code_identifier = node_type

    if parent is not None:
      if node.parent.type in block_child_list:
        parent_info = current_path[current_path.rfind("-") + 1:-1]
        # print("iiiiii",parent_info)
      else:
        parent_info=node.parent.type

    else:
       parent_info = "NA"
    # print("qqqqq",node.text.decode())
    num_tokens_in_chunk = num_tokens_from_string(node.text.decode(), "cl100k_base")
    print("num_toke",num_tokens_in_chunk)
    if node_type ==decorated_definition:
      if concat:
        prev_sibling=df.at[df.index[-1], "code_chunk"].decode()
        concat=False
      print("ddddd")
      print(node.children)
      df_to_append = pd.DataFrame([{'code_chunk': node.text,'file_name':file_name, 'file_path': file_path,'path_to_code_chunk' :current_path,'parent' :parent_info,
       'prev_sibling':prev_sibling,'next_sibling':next_sibling,'start_point':node.start_point,'end_point':node.end_point,'has_error':has_error,'code_node_type':node.children[child_count-1].type,
                      'code_identifier':code_identifier,'is_chunked':"",'num_tokens':num_tokens_in_chunk,'uuid_str':str(uuid.uuid4())}])
      df = pd.concat([df, df_to_append], ignore_index=True)
    elif node_type in(function_definition,method_definition,class_definition,field_definition,root_node_type) or lexical_function:
      if concat:
        prev_sibling=df.at[df.index[-1], "code_chunk"].decode()
        concat=False
      print("kkkkk",node.type)
      df_to_append = pd.DataFrame([{'code_chunk': node.text,'file_name':file_name, 'file_path': file_path,'path_to_code_chunk' :current_path,'parent' :parent_info,
       'prev_sibling':prev_sibling,'next_sibling':next_sibling,'start_point':node.start_point,'end_point':node.end_point,'has_error':has_error,'code_node_type':node.type,
                      'code_identifier':code_identifier,'is_chunked':"",'num_tokens':num_tokens_in_chunk,'uuid_str':str(uuid.uuid4())}])
      df = pd.concat([df, df_to_append], ignore_index=True)
    else:
      if num_tokens_in_chunk>500:
        print("lllll")
        texts = text_splitter.split_text(node.text.decode())
        print(type(texts))
        if concat:
          prev_sibling=df.at[df.index[-1], "code_chunk"].decode()
          concat=False
        for index, split_text in enumerate(texts):
          if index !=0:
            prev_sibling1=texts[index-1]
            prev_sibling=texts[index-1]
          if index !=len(texts)-1:
            next_sibling=texts[index+1]
          else:
            if node.next_sibling is not None:
              if node.next_sibling.text.decode() not in (";","{","}"):
                next_sibling=node.next_sibling.text.decode()
              else:
                if node.next_sibling.next_sibling is not None:
                  next_sibling=node.next_sibling.next_sibling.text.decode()
                else:
                  next_sibling="Next sibling does not exist"

            else:
              next_sibling="Next sibling does not exist"
          print("ooooooo "+split_text)
          df_to_append = pd.DataFrame([{'code_chunk': split_text.encode('utf-8'),'file_name':file_name, 'file_path': file_path,'path_to_code_chunk' :current_path,'parent' :parent_info,
       'prev_sibling':prev_sibling,'next_sibling':next_sibling,'start_point':node.start_point,'end_point':node.end_point,'has_error':has_error,'code_node_type':node.type,
                      'code_identifier':code_identifier,'is_chunked':node.text.decode(),'num_tokens':len(split_text),'uuid_str':str(uuid.uuid4())}])
          df = pd.concat([df, df_to_append], ignore_index=True)
      else:
        print("7474")
        if(len(df)>0):
          print("tyty")
          num_of_token_at_last_row = df.at[df.index[-1], "num_tokens"]
          path_to_code_chunk_of_last_row = df.at[df.index[-1], "path_to_code_chunk"]
          if (num_tokens_in_chunk+num_of_token_at_last_row<500) and (path_to_code_chunk_of_last_row == current_path) and (df.at[df.index[-1], "code_node_type"] not in (function_definition,method_definition,class_definition,field_definition)):


            df.at[df.index[-1], "code_chunk"]+=b'\n'+node.text
            df.at[df.index[-1], "end_point"]=node.end_point
            df.at[df.index[-1], "code_node_type"]+=","+node.type

            df.at[df.index[-1], "has_error"]='N'
            df.at[df.index[-1], "num_tokens"]+=num_tokens_in_chunk
            df.at[df.index[-1], "next_sibling"]=next_sibling
            if(len(df)>1):
              df.at[df.index[-2], "next_sibling"]=df.at[df.index[-1], "code_chunk"].decode()
            # running_previous_sibling=df.at[df.index[-2], "code_chunk"].decode()
            concat=True;
          else:
            if node.text.decode() not in (";","{","}"):
              df_to_append = pd.DataFrame([{'code_chunk': node.text,'file_name':file_name, 'file_path': file_path,'path_to_code_chunk' :current_path,'parent' :parent_info,
       'prev_sibling':prev_sibling,'next_sibling':next_sibling,'start_point':node.start_point,'end_point':node.end_point,'has_error':has_error,'code_node_type':node.type,
                      'code_identifier':code_identifier,'is_chunked':"",'num_tokens':num_tokens_in_chunk,'uuid_str':str(uuid.uuid4())}])
              df = pd.concat([df, df_to_append], ignore_index=True)
        else:
          if node.text.decode() not in (";","{","}"):
            df_to_append = pd.DataFrame([{'code_chunk': node.text,'file_name':file_name, 'file_path': file_path,'path_to_code_chunk' :current_path,'parent' :parent_info,
       'prev_sibling':prev_sibling,'next_sibling':next_sibling,'start_point':node.start_point,'end_point':node.end_point,'has_error':has_error,'code_node_type':node.type,
                      'code_identifier':code_identifier,'is_chunked':"",'num_tokens':num_tokens_in_chunk,'uuid_str':str(uuid.uuid4())}])
            df = pd.concat([df, df_to_append], ignore_index=True)


    #main logic goes above
    if parent is not None:
        print("Parent Details:")
        print(f"p Type: {parent.type}")
        print(f"p Text: {parent.text}")
    if parent is None:
      for child in node.children:
        print(f" phho : {child.type}")
        traverse_ast(child,file_extension,current_path+node.type+"/",function_definition,method_definition,class_definition,field_definition_arg,decorated_definition,root_node_type,block_child_list,identifier_index)

    if lexical_function:
      for child in node.children[1].children[2].children[2].children:
        print("2424",child)
        lex_child=False
        if child.type=='lexical_declaration' and child.children[1].children[2].type=='arrow_function':
          lex_child=True
        if (num_tokens_in_chunk>500) or (child.type  in (function_definition,method_definition,class_definition,method_definition,decorated_definition)) or lex_child:
          traverse_ast(child,file_extension,current_path + node_type + "-"+ code_identifier+"/",function_definition,method_definition,class_definition,field_definition_arg,decorated_definition,root_node_type,block_child_list,identifier_index)

    if node_type in(function_definition,method_definition,class_definition,field_definition,decorated_definition):
      for child in node.children:
        print(child.type," dsf ")
        if child.type in block_child_list:
          if code_identifier=='main':
            print("azaz",num_tokens_in_chunk,)
          for block_child in child.children:
            lex_child=False
            if child.type=='lexical_declaration' and child.children[1].children[2].type=='arrow_function':
              lex_child=True
            if (num_tokens_in_chunk>500) or (block_child.type  in (function_definition,method_definition,class_definition,field_definition,decorated_definition)) or lex_child:
              traverse_ast(block_child,file_extension,current_path + node_type + "-"+ code_identifier+"/",function_definition,method_definition,class_definition,field_definition_arg,decorated_definition,root_node_type,block_child_list,identifier_index)
        if child.type in (function_definition,method_definition,class_definition):
          print("bnp")
          for grand_child in child.children:
            if grand_child.type in block_child_list:
              for block_grand_child in grand_child.children:
                if (num_tokens_in_chunk>500) or (block_grand_child.type  in (function_definition,method_definition,class_definition,field_definition,decorated_definition)):
                  traverse_ast(block_grand_child,file_extension,current_path + node.children[child_count-1].type + "-"+ node.children[child_count-1].children[1].text.decode()+"/",function_definition,method_definition,class_definition,field_definition_arg,decorated_definition,root_node_type,block_child_list,identifier_index)

# Example usage:
# Assuming you have an AST root node called 'root_node'
def ast_traversal(fileName,filePath):

# traverse_ast(root,".rs","","function_item","trait_item","impl_item","field_definition","decorated_definition","source_file",["block","declaration_list"],2)
# traverse_ast(root,".py","","function_definition","#","class_definition","field_definition","decorated_definition","module",["block"],2)
# traverse_ast(root,".java","","method_declaration","constructor_declaration","class_declaration","field_definition","decorated_definition","program",["block","class_body","constructor_body"],2)
# traverse_ast(root,".cpp","","function_definition","method_definition","class_specifier","field_definition","decorated_definition","translation_unit",["compound_statement","field_declaration_list"],2)
    traverse_ast(root,".js","","function_declaration","method_definition","class_declaration","field_definition","decorated_definition","program",["statement_block","class_body"],2)





# traverse_ast(root,"","function_definition","class_specifier","decorated_definition","translation_unit","block","field_declaration_list",2)
# traverse_ast(root,"","method_declaration","class_declaration","decorated_definition","program","block","class_body",2)
def bytes_to_string(byte_str):
    return byte_str.decode('utf-8') if isinstance(byte_str, bytes) else byte_str

# Apply the function to the 'code_chunk' column to convert byte strings to strings
df['code_chunk'] = df['code_chunk'].apply(bytes_to_string)