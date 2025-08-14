from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db
from app.auth import get_current_user
from app.config import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

router = APIRouter()

@router.post("/create-payment-intent", response_model=schemas.PaymentResponse)
def create_payment_intent(booking_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id, models.Booking.user_id == current_user.id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    intent = stripe.PaymentIntent.create(
        amount=int(booking.total_amount * 100),
        currency="usd",
        metadata={"booking_id": booking_id}
    )
    
    payment = schemas.PaymentBase(
        booking_id=booking_id,
        amount=booking.total_amount,
        currency="usd"
    )
    db_payment = crud.create_payment(db, payment)
    db_payment.stripe_payment_intent_id = intent.id
    db_payment.status = intent.status
    db.commit()
    db.refresh(db_payment)
    return db_payment

@router.post("/webhook")
def stripe_webhook(request: dict):
    event = stripe.Event.construct_from(request, settings.STRIPE_WEBHOOK_SECRET)
    if event.type == "payment_intent.succeeded":
        payment_intent = event.data.object
        booking_id = payment_intent.metadata.get("booking_id")
        db = next(get_db())
        payment = db.query(models.Payment).filter(models.Payment.stripe_payment_intent_id == payment_intent.id).first()
        if payment:
            payment.status = "succeeded"
            booking = db.query(models.Booking).filter(models.Booking.id == payment.booking_id).first()
            booking.status = schemas.BookingStatus.CONFIRMED
            db.commit()
    return {"status": "success"}