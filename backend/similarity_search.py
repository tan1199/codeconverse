import Levenshtein
from rapidfuzz import fuzz
from openai.embeddings_utils import cosine_similarity
from openai.embeddings_utils import get_embedding
import ast
from pathlib import Path
import openai
import cohere
from keys.api_key import COHERE_API_KEY
extension_to_language={
"py":"python",
"rs":"rust",
"js":"javascript",
"java":"java",
"cpp":"cpp",

}
def calculate_levenshtein_fuzzy_distance_similarity(word_atribute,target_value):
    levenshtein_dist = Levenshtein.distance(word_atribute.lower(), target_value.lower())
    fuzz_ratio = fuzz.WRatio(target_value.lower(), word_atribute.lower())
    similarity_score = levenshtein_dist + 1 - (fuzz_ratio / 100)
    # print(similarity_score)
    if "." in word_atribute:
        levenshtein_dist1 = Levenshtein.distance(word_atribute.lower().split('.')[0], target_value.lower())
        fuzz_ratio1 = fuzz.WRatio(target_value.lower(), word_atribute.lower().split('.')[0])
        similarity_score1 = levenshtein_dist1 + 1 - (fuzz_ratio1 / 100)
        similarity_score=min(similarity_score,similarity_score1)
    # if target_value=="dfs":
        # print(word_atribute,similarity_score)
    return similarity_score



def code_embedding_similarity_search(df, code_query,apikey,rerank, n=5, pprint=True, n_lines=25):
    openai.api_key=apikey
    print("ertgh",code_query)
    if isinstance(df.iloc[0]['code_embedding'], str):
        print("andar")
        df['code_embedding'] = df['code_embedding'].apply(lambda x: ast.literal_eval(x))
    embedding = get_embedding(code_query, engine='text-embedding-ada-002')
    print("ayyyndar",COHERE_API_KEY,rerank)

    df['similarities'] = df.code_embedding.apply(lambda x: cosine_similarity(x, embedding))
    print("anggdar")

    # df['code_identifier_similarities'] = df.code_identifier_embedding.apply(lambda x: cosine_similarity(x, embedding))
    # df['similarities']=0.0*df['code_identifier_similarities']+1.0* df['code_chunk_similarities']

    # res = df.sort_values('similarities', ascending=False).head(n)
    root = Path(__file__).parent


    res = df.sort_values('similarities', ascending=False)
    doc = res['code_chunk'].astype(str).tolist()
    doc1=doc[:9]
    print("lmiiiiiii",doc1)
    top_n=min(len(res),10)    
    
    res.to_csv(f"{root}/repositories/aaaa.csv", index=False)
    print("res00", res)
    res = res.reset_index(drop=True)
    print("res1", res)
    if rerank:
        co = cohere.Client(COHERE_API_KEY)
        results = co.rerank(query=code_query, documents=doc1, top_n=8, model="rerank-multilingual-v2.0")
        cohere_reranked_index = [result.index for result in results.results]
        print(cohere_reranked_index)
        res = res.loc[cohere_reranked_index]
        print("mjk",res)

    top_n=min(top_n,5)    
    top_n_similarities = res['similarities'].head(top_n).tolist()
    top_n_sources_file_path = res['file_path'].head(top_n).tolist()
    top_n_sources_start_line_no = res['start_point'].head(top_n).tolist()
    top_n_sources_end_line_no = res['end_point'].head(top_n).tolist()
    print(top_n_similarities,top_n_sources_file_path, top_n_sources_start_line_no, top_n_sources_end_line_no)
    res.to_csv(f"{root}/repositories/bbbb1.csv", index=False)

    # print(root)

    print("res2",res)

    # if pprint:
    #     for r in res.iterrows():
    #         print(f"{r[1].file_path}:{r[1].code_identifier}  score={round(r[1].similarities, 3)}")
    #         print("\n".join(r[1].code_chunk.split("\n")[:n_lines]))
    #         print('-' * 70)
    # return res
    print("lkklllaax", res.loc[res.index[0], 'code_chunk'])
    try:
        print(f"```{extension_to_language[res.loc[res.index[0], 'file_name'].split('.')[1]]}\n{res.loc[res.index[0], 'code_chunk']}```", res.loc[res.index[0], "similarities"], extension_to_language[res.loc[res.index[0], "file_name"].split(".")[1]], top_n_similarities, top_n_sources_file_path, top_n_sources_start_line_no, top_n_sources_end_line_no)
    except Exception as e:
        print(e)
    return f"```{extension_to_language[res.loc[res.index[0], 'file_name'].split('.')[1]]}\n{res.loc[res.index[0], 'code_chunk']}```", res.loc[res.index[0], "similarities"], extension_to_language[res.loc[res.index[0], "file_name"].split(".")[1]], top_n_similarities, top_n_sources_file_path, top_n_sources_start_line_no, top_n_sources_end_line_no
