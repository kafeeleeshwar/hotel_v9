from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.BookingResponse)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_booking(db, booking, current_user.id)

@router.get("/", response_model=List[schemas.BookingResponse])
def get_bookings(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_user_bookings(db, current_user.id)

@router.post("/{booking_id}/cancel")
def cancel_booking(booking_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id, models.Booking.user_id == current_user.id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking.status = schemas.BookingStatus.CANCELLED
    db.commit()
    return {"message": "Booking cancelled"}