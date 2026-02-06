import pandas as pd

df = pd.read_csv("data/ratings.csv")

df = df.rename(columns={
    "userId": "user_id",
    "movieId": "item_id"
})

df = df[["user_id", "item_id", "rating"]]

df.to_csv("data/interactions.csv", index=False)

print("interactions.csv created successfully")
