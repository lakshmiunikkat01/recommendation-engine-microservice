# recommendation-engine-microservice

A production-ready recommendation engine built as a RESTful microservice.  
The system generates personalized user recommendations and similar item suggestions using collaborative filtering and cosine similarity, exposed via FastAPI.

---

##  Features

- Personalized user → item recommendations
- Similar item** recommendations (item–item similarity)
- Collaborative filtering using a user–item interaction matrix
- REST APIs built with FastAPI
- Interactive API documentation using Swagger UI
- Uses real-world MovieLens (Kaggle) dataset
- Clean separation between model, service, and API layers

---

##  Tech Stack

- **Python 3.10**
- **FastAPI**
- **pandas**
- **NumPy**
- **scikit-learn**
- **Uvicorn**
- **MovieLens dataset (Kaggle)**

---

##  Project Structure
recommendation-engine-microservice/
│
├── app/
│ ├── main.py # FastAPI app
│ ├── models/
│ │ └── collaborative_filtering.py
│ └── services/
│ └── recommendation_service.py
│
├── data/
│ └── interactions.csv # Processed dataset
│
├── convert_dataset.py
├── requirements.txt
└── .gitignore


---

##  Setup & Installation

1. Clone the repository

git clone https://github.com/lakshmiunikkat01/recommendation-engine-microservice.git
cd recommendation-engine-microservice

2️. Install dependencies
py -3.10 -m pip install -r requirements.txt

3️. Run the application
py -3.10 -m uvicorn app.main:app --reload
The server will start at:
http://127.0.0.1:8000

## API Endpoints
## Get User Recommendations
GET /recommend/user/{user_id}?n=5


Example Response

{
  "user_id": 1,
  "recommendations": [
    { "item_id": 318, "score": 2.655 },
    { "item_id": 589, "score": 2.087 }
  ]
}

## Get Similar Items
GET /similar/item/{item_id}?n=5


Example Response

{
  "item_id": 318,
  "similar_items": [
    { "item_id": 356, "score": 0.713 },
    { "item_id": 296, "score": 0.702 }
  ]
}



