import Levenshtein
from rapidfuzz import fuzz
from openai.embeddings_utils import cosine_similarity
from openai.embeddings_utils import get_embedding
import ast
def calculate_levenshtein_fuzzy_distance_similarity(word_atribute,target_value):
    levenshtein_dist = Levenshtein.distance(word_atribute, target_value)
    fuzz_ratio = fuzz.WRatio(target_value, word_atribute)
    similarity_score = levenshtein_dist + 1 - (fuzz_ratio / 100)
    return similarity_score



def code_embedding_similarity_search(df, code_query, n=5, pprint=True, n_lines=25):
    print("ertgh",code_query)
    if isinstance(df.iloc[0]['code_embedding'], str):
        print("andar")
        df['code_embedding'] = df['code_embedding'].apply(lambda x: ast.literal_eval(x))
    embedding = get_embedding(code_query, engine='text-embedding-ada-002')
    print("ayyyndar")

    df['similarities'] = df.code_embedding.apply(lambda x: cosine_similarity(x, embedding))
    print("anggdar")

    # df['code_identifier_similarities'] = df.code_identifier_embedding.apply(lambda x: cosine_similarity(x, embedding))
    # df['similarities']=0.0*df['code_identifier_similarities']+1.0* df['code_chunk_similarities']

    # res = df.sort_values('similarities', ascending=False).head(n)
    res = df.sort_values('similarities', ascending=False)
    print("res",res)

    # if pprint:
    #     for r in res.iterrows():
    #         print(f"{r[1].file_path}:{r[1].code_identifier}  score={round(r[1].similarities, 3)}")
    #         print("\n".join(r[1].code_chunk.split("\n")[:n_lines]))
    #         print('-' * 70)
    # return res
    return res.loc[res.index[0], "code_chunk"]