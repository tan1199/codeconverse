import openai
from keys.api_key import API_KEY
openai.api_key=API_KEY



prompt="""classify the following tweet sentiment as positive or negative
Tweet: I pity the new Batman movie!
sentiment:"""
# response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=6)

# def getresponse_from_openai_api(prompt):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#   prompt=prompt,
#     temperature=0.1,
#     max_tokens=3900,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     return response.choices[0].text

prompt= """
Can you explain the roles of the corrects, wrongs, and node_eval variables in the evaluation process?
def evaluate(exp):
    processes = 32
    exp_dir = get_exp_dir(exp)
    infer_dir = path.join(exp_dir, 'inferences')
    eval_result_path = path.join(exp_dir, 'eval_result.yaml')
    if path.isfile(eval_result_path):
        # Already done
        return

    evaluator_path = path.join(exp_dir, 'evaluator.pt')
    fine_tune_complete_path = path.join(exp_dir, 'fine_tune_complete.yaml')
    if not path.isfile(evaluator_path) or not path.isfile(
            fine_tune_complete_path):
        print('Dependencies not met.')
        return

    dummy_config = {'eval_length_budget': 1000, 'num_workers': processes}
    generator = GPTDataGenerator(exp)
    evaluator = Evaluator(dummy_config, exp.paradigm, vocab=get_exp_vocab(exp))
    evaluator.load_state_dict(torch.load(evaluator_path))
    with open(fine_tune_complete_path, 'r') as f:
        fine_tune_complete = yaml.load(f, Loader=yaml.FullLoader)
    model_id = fine_tune_complete['fine_tuned_model']

    os.makedirs(infer_dir, mode=0o700, exist_ok=True)

    eval_data = []
    infer_args = []
    skip_count = 0
    for i, (prob_cls, args) in enumerate(tqdm(evaluator.sorted_probs)):
        x, y, _ = prob_cls.solve(args, paradigm=generator.paradigm)
        datum = generator.xy_to_gpt_data(generator.vocab(x), generator.vocab(y))
        eval_data.append(datum)
        for j, example in enumerate(datum):
            save_path = path.join(infer_dir, f'{i}-{j}.json')
            if path.isfile(save_path):
                # Already done
                skip_count += 1
                continue
            infer_args.append((example, save_path))

    print(
        f'Calling API for {len(infer_args)} examples, skipping already finished {skip_count} examples.')
    print(f'Model ID: {model_id}')
    with Pool(16) as pool:
        list(tqdm(
            pool.imap(partial(save_inference, model_id=model_id), infer_args),
            total=len(infer_args)))

    # Aggregate results
    corrects = []
    wrongs = []
    for i, datum in enumerate(tqdm(eval_data)):
        correct = True
        for j, example in enumerate(datum):
            result_path = path.join(infer_dir, f'{i}-{j}.json')
            with open(result_path, 'r') as f:
                result = json.load(f)
            if not result['choices'][0]['text'].startswith(
                    example['completion']):
                correct = False
                wrongs.append((
                    example['prompt'],
                    example['completion'],
                    result['choices'][0]['text'],
                    result['choices'][0]['finish_reason']
                ))
        corrects.append(correct)

    node_eval = {
        prob: correct
        for prob, correct in zip(evaluator.sorted_probs, corrects)
    }
    correct_deep, correct_shallow, prob_total = evaluator.aggregate_eval(
        node_eval)
    with open(eval_result_path, 'w') as f:
        eval_result = {
            'correct': sum(correct_deep.values()),
            'total': sum(prob_total.values()),
        }
        print(eval_result)
        yaml.dump(eval_result, f)
    print(f'Evaluation result written to {eval_result_path}')

"""

prompt="""
You will get a user query regarding a codebase .The user query can contain multiple instructions.
First you will split all the instruction and list them. Make sure that each instruction makes sense on its own. Do not add anythong which is not provided in the user query, but if suppose
the subsequent instruction are dependent on previous ones then please incorporate relevant information from them into the current one.
Make sure to replace pronouns in the instruction from the context available do that each instuction makes sense on its own
Just extract the instructions from the following user query and add them under instructions key in ```json```,each instruction will have its own json.
Then try to understand the objective of each instruction and assign command a command from {"expalin","compare","fetch" }
if the instruction contains fetch and explain or compare and explain then command will be explain and compare respectively
Finally extract metadata present in the instruction,
metadata can be in the form of function name/ method name, class name and file name, only populate te metadata value if u are certain, analyze the instruction and then if you can conclusively decide
that a certain value of metadata is present than use that value otherwise assume 'NA', if you want to decide for function_name then look for the keyword function or method, function_name will generally
precede or follow the key word funcion/method, similarlay for class_name look for words coming just before or after class. for filename look for words ending with extension or words coming before /after the word file;
If you do not find these influencing keywords please populate the value as 'NA'
Just extract the instructions,command and metadata from the following user query and output only in ```json```,each instruction will have its own json.
the metadata will be list of key value pairs, the keys being function_name, class_name and file_name.
if the instruction is compare then there will be multiple values of function_name/class_name/file_name, so split the instruction into two instructions, first one contains
the first enitity for comparision and second instruction refers to the second enitiy of comparision and extract the relevant metadata and other keys for respective entities ib the both instructions.
remember that method name is interchangeably used for the function name
Sample json output
{
    {
      "instruction": "NA",
      "command": "NA",
      "metadata": {
        "function_name": "NA",
		"class_name": "NA"
        "file_name": "NA"
      }
    },
 {
      "instruction": "NA",
      "command": "NA",
      "metadata": {
        "function_name": "NA",
		"class_name": "NA"
        "file_name": "NA"
      }
    },	
	}
	
Think step by step and reason yourself to the right decisions to make sure we only split into multiple instructions if we have conclusive evidence to do so and when we do each instruction should make sense on its own, we derive relevant information from previous instructions if required,
and also make sure you extract the metadata efficiently in the format explained above. The metadata values will not contain any space.
user query :'list the import statement'
"""


prompt0="""
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
and also make sure you extract the metadata efficiently in the format explained above. The metadata values will not contain any space."""

for x in [
          # "fetch the imports of qualifier",
          # "list the imports and thought function of question.java",
          #  "impr_thru function",
    # "explain bill method of gpt_fine_tune.py and compare thought method and _thought method of knapsack.py ",
    # "explain bill method of gpt_fine_tune.py and compare thought and question method of knapsack.py ",
    "solution class of findCircleNum.py",
    "explain evacuate method of gpt_fine_tune.py and fetch thought method of knapsack.py ",
    "explain fortiy method of abc class and _thought method of explore class of mcm.py ",
    # "explain all impoerts of mcm.py and javier class of algo.js",
    # "explain each class of movieSearch.js",
    # "explain all functions of fineTune.cpp",
    # "fetch every method  of evaluate clss",
    # "analyze all the dependencies required for knapsack.py",
          # "I'm curious about the 'getRemainingCapacity' function in the knapsack file. Could you elaborate on its purpose and implementation?",
    #       "Analyze method  processData  of class  DataProcessor  in file  data_handler.py  with method  handleData  of class  DataHandler  in file  file_handler.py ",
    # "Contrast function  calculateSum  of class  Calculator  in file  math_operations.py  with function  computeAverage  of class  Statistics  in file  statistics.py ",
    # "Examine method  getUserInfo  of class  UserManager  in file  user_management.py  against method  fetchUserInfo  of class  UserAPI  in file  api_handler.py ",
    # "Evaluate function  searchItem  of class  SearchEngine  in file  search_engine.py  with method  findItem  of class  ItemFinder  in file  item_locator.py ",
    # "Compare function  sendRequest  of class  APIHandler  in file  network_manager.py  with method  handleRequest  of class  HTTPClient  in file  http_client.py ",
    # "Contrast method  encryptData  of class  DataEncryptor  in file  security_module.py  with function  decryptData  of class  DataDecryptor  in file  encryption_utils.py ",
    # "Analyze function  generateReport  of class  ReportGenerator  in file  report_manager.py  against method  prepareReport  of class  ReportPreparer  in file  report_preparation.py ",
    # "Examine method  updateStatus  of class  StatusUpdater  in file  status_manager.py  with function  modifyStatus  of class  StatusModifier  in file  status_utility.py ",
    # "Evaluate function  validateInput  of class  InputValidator  in file  input_handling.py  with method  sanitizeInput  of class  InputSanitizer  in file  sanitization_utils.py ",
    # "Compare function  saveFile  of class  FileManager  in file  file_manager.py  to method  uploadFile  of class  FileUploader  in file  file_upload.py",
    # "get the  calculateTotal  function in file  financial_manager.py  and the  computeSum  method of class  MathProcessor",
    # "Examine class  CustomerDatabase  in file  database_handler.py  against the  getUserInfo  method in file  user_manager.py",
    # "compare the  generateReport  function in file  report_generator.py to prepareReport method of class  ReportPreparer",
    # "explain the  searchItem  function in file  search_module.py  along with the  findItem  method of class  ItemLocator",
    "Examine class  ProductCatalog  in file  catalog_manager.py  against the  getProductInfo  method in file  product_info_handler.py"]:
    # "Contrast the  processData  function in file  data_processor.py  with the  handleData  method of class  DataHandler",
    # "Analyze the  encryptData  function in file  security_module.py  with the  decryptData  method of class  DataDecryptor",
    # "explain  class  OrderManager  in file  order_handler.py   along with with the  processOrder  function in file  order_processor.py",
    # "fetch the  sendRequest  function in file  api_manager.py  and the  handleRequest  method of class  APIHandler",
    # "Compare the  saveConfig  function in file  config_manager.py  with the  updateConfig  method of class  ConfigUpdater",
    # "compare saveConfig  function in file  config_manager.py along with  updateConfig  method of class  ConfigUpdater"]:
    prompt1=f"user query :'{x}"
    prompt=prompt0+prompt1
    print(prompt1)
# user query :'explain the code in knapsack file which does not belong to the knapsack class'
# user query :'explain the code in knapsack file which does not belong to the knapsack class'
# user query :'explain the code in knapsack file which does not belong to the knapsack class'
# user query :'explain the code in knapsack file which does not belong to the knapsack class'
# user query :'explain the code in knapsack file which does not belong to the knapsack class'
#
# prompt="""
# given a user query which may contain multiple instruction return a json containing all the instructions, when splitting the user query into multiple instructions make sure to include proper context in each instruction if a particular instruction is dependent on its previous instruction, split only if necessary
# make sure to replace pronouns in the instruction from the context available do that each instuction makes sense on its own
# the only key in the json should be instruction
# user query :'compare the differences between _question and question method of evaluate'
# """
    def getresponse_from_openai_api(prompt):
        completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-16k',
        messages = [
            {'role': 'user', 'content': prompt}
        ],
        temperature = 0
    )
        return completion['choices'][0]['message']['content']

    # print(getresponse_from_openai_api(prompt))
# print(getresponse_from_openai_api("given a .dat fle stored in hdfs , it contains | separated values, one of the values is a date in yyyymmdd how to get the date value, the index of date column is  known, just read the second line,provide code in  java"))
# print(getresponse_from_openai_api("""objectmapper readvalue with typerefrence, the json to read has the following structure
# {
# "process_id_1": {
#       "date": 20230720,
#       "run_time": 1426968,
#       "dependencies": ["a","b","c"]
#         }
# }
#                                          """))
print(getresponse_from_openai_api("""update json of following structure stored on hdfs in java 
{
"process_id_1": {
      "date": 20230720,
      "run_time": 1426968,
      "dependencies": ["a","b","c"]
        }
}
   """))
import pandas as pd
from rapidfuzz import fuzz, process

# Sample DataFrame with a column containing words
data = {
    'word_column': [
        "evaluation",
        "evaluating",
        "evaluated",
        "calibrate",
        "appraisal",
        "evacuate",
    ]
}
df = pd.DataFrame(data)

target_word = "evaluate"

# Use process.extractOne to find the best match and its score
best_match, highest_score = process.extractOne(target_word, df['word_column'].tolist(), scorer=fuzz.WRatio)

print(f"Best match: {best_match} (Score: {highest_score})")



import Levenshtein

def has_at_most_two_edits(word1, word2):
    levenshtein_distance = Levenshtein.distance(word1, word2)
    return levenshtein_distance <= 2

# Example usage
word1 = "evaluate"
word2 = "evaluation"

if has_at_most_two_edits(word1, word2):
    print("The words have at most two additions or deletions.")
else:
    print("The words have more than two additions or deletions.")