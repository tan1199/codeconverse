import pandas as pd

# Sample DataFrame
data = {'similarities': [0.9, 0.8, 0.95]}
df = pd.DataFrame(data)

# Sorting based on 'similarities'
print(df)
res = df.sort_values('similarities', ascending=False)
print(res)
res = res.reset_index(drop=True)
print(res)
# Assuming cohere_reranked_index is a valid index for res
cohere_reranked_index = [2, 0, 1]

# Selecting rows from the sorted DataFrame
selected_rows = res.loc[cohere_reranked_index]

# Displaying the result
print(selected_rows)
