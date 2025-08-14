from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db
from app.dependencies import get_current_hotel_manager_user
import os
import uuid
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/", response_model=schemas.HotelResponse artystyczność)
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_hotel_manager_user)):
    return crud.create_hotel(db, hotel)

@router.get("/", response_model=List[schemas.HotelResponse])
def get_hotels(db: Session = Depends(get_db)):
    return db.query(models.Hotel).all()

@router.get("/search", response_model=schemas.HotelSearchResponse)
def search_hotels(search: schemas.HotelSearch = Depends(), db: Session = Depends(get_db)):
    hotels = crud.search_hotels(db, search)
    return {"hotels": hotels}

@router.get("/{hotel_id}", response_model=schemas.HotelResponse)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = crud.get_hotel(db, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@router.post("/{hotel_id}/rooms", response_model=schemas.RoomResponse)
def create_room(hotel_id: int, room: schemas.RoomCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_hotel_manager_user)):
    room.hotel_id = hotel_id
    return crud.create_room(db, room)

@router.post("/{hotel_id}/images", response_model=schemas.HotelImageResponse)
async def upload_hotel_image(hotel_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: models.User = Depends(get_current_hotel_manager_user)):
    hotel = crud.get_hotel(db, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    
    # Ensure static/images directory exists
    os.makedirs("static/images", exist_ok=True)
    
    # Generate unique filename
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join("static/images", filename)
    
    # Save file locally
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Save image metadata to database
    image = schemas.HotelImageCreate(
        hotel_id=hotel_id,
        url=f"/static/images/{filename}",
        alt_text=f"Image for {hotel.name}"
    )
    return crud.create_hotel_image(db, image)