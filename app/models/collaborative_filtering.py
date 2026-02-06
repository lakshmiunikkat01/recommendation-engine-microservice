import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    return pd.read_csv("data/interactions.csv")


def create_user_item_matrix(df):
    return df.pivot_table(
        index="user_id",
        columns="item_id",
        values="rating",
        fill_value=0
    )


def compute_similarity(matrix):
    similarity = cosine_similarity(matrix)
    return pd.DataFrame(
        similarity,
        index=matrix.index,
        columns=matrix.index
    )


def recommend_items(user_id, matrix, similarity_df, n=5):
    if user_id not in matrix.index:
        return []

    user_similarities = similarity_df.loc[user_id]
    weighted_sum = np.zeros(matrix.shape[1])
    similarity_sum = np.zeros(matrix.shape[1])

    for other_user in matrix.index:
        if other_user == user_id:
            continue

        similarity = user_similarities[other_user]
        ratings = matrix.loc[other_user].values

        weighted_sum += similarity * ratings
        similarity_sum += np.abs(similarity)

    similarity_sum[similarity_sum == 0] = 1
    scores = weighted_sum / similarity_sum

    scores = pd.Series(scores, index=matrix.columns)

    seen_items = matrix.loc[user_id][matrix.loc[user_id] > 0].index
    scores = scores.drop(seen_items)

    top_items = scores.sort_values(ascending=False).head(n)
    return list(zip(top_items.index.tolist(), top_items.values.round(3)))

if __name__ == "__main__":
    df = load_data()
    matrix = create_user_item_matrix(df)
    similarity_df = compute_similarity(matrix)

    recs = recommend_items(1, matrix, similarity_df)
    for item, score in recs:
        print(item, score)
def similar_items(item_id, matrix, n=5):
    if item_id not in matrix.columns:
        return []

    item_vector = matrix[item_id].values.reshape(1, -1)
    similarities = cosine_similarity(item_vector, matrix.T)[0]

    scores = pd.Series(similarities, index=matrix.columns)
    scores = scores.drop(item_id)

    top_items = scores.sort_values(ascending=False).head(n)
    return list(zip(top_items.index.tolist(), top_items.values.round(3)))

