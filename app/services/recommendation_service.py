from app.models.collaborative_filtering import (
    load_data,
    create_user_item_matrix,
    compute_similarity,
    recommend_items,
    similar_items
)


class RecommendationService:
    def __init__(self):
        df = load_data()
        self.matrix = create_user_item_matrix(df)
        self.similarity_df = compute_similarity(self.matrix)

    def recommend_for_user(self, user_id: int, n: int = 5):
        return recommend_items(
            user_id=user_id,
            matrix=self.matrix,
            similarity_df=self.similarity_df,
            n=n
        )

    def similar_for_item(self, item_id: int, n: int = 5):
        return similar_items(
            item_id=item_id,
            matrix=self.matrix,
            n=n
        )
