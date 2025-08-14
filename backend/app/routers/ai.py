from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import settings
from openai import OpenAI

router = APIRouter()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

@router.post("/recommendations")
def get_recommendations(search: schemas.HotelSearch, db: Session = Depends(get_db)):
    hotels = crud.search_hotels(db, search)
    prompt = f"Recommend hotels based on: {search.dict()}. Available hotels: {[h.name for h in hotels]}"
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return {"recommendations": response.choices[0].text.strip()}

@router.post("/chat")
def chat_with_assistant(message: dict):
    response = client.completions.create(
        model="text-davinci-003",
        prompt=f"Act as a travel assistant for a hotel booking platform. User message: {message['message']}",
        max_tokens=200
    )
    return {"response": response.choices[0].text.strip()}