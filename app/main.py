from fastapi import FastAPI, HTTPException
from app.services.recommendation_service import RecommendationService

app = FastAPI(
    title="Recommendation Engine Microservice",
    version="1.0.0"
)

service = RecommendationService()


@app.get("/recommend/user/{user_id}")
def recommend_user(user_id: int, n: int = 5):
    recs = service.recommend_for_user(user_id, n)

    if not recs:
        raise HTTPException(status_code=404, detail="No recommendations found")

    return {
        "user_id": user_id,
        "recommendations": [
            {"item_id": int(item_id), "score": float(score)}
            for item_id, score in recs
        ]
    }
@app.get("/similar/item/{item_id}")
def get_similar_items(item_id: int, n: int = 5):
    recs = service.similar_for_item(item_id, n)

    if not recs:
        raise HTTPException(status_code=404, detail="No similar items found")

    return {
        "item_id": item_id,
        "similar_items": [
            {"item_id": int(item), "score": float(score)}
            for item, score in recs
        ]
    }
