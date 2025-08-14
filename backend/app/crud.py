from sqlalchemy.orm import Session
from app.models import User, Hotel, Room, Booking, Payment, Review, Amenity, HotelImage, HotelAmenity
from app.schemas import UserCreate, HotelCreate, RoomCreate, BookingCreate, ReviewCreate, AmenityCreate, HotelImageCreate
from passlib.context import CryptContext
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_hotel(db: Session, hotel: HotelCreate):
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

def get_hotel(db: Session, hotel_id: int):
    return db.query(Hotel).filter(Hotel.id == hotel_id).first()

def search_hotels(db: Session, search: schemas.HotelSearch):
    query = db.query(Hotel)
    
    if search.destination:
        query = query.filter(
            (Hotel.city.ilike(f"%{search.destination}%")) |
            (Hotel.country.ilike(f"%{search.destination}%"))
        )
    if search.min_price:
        query = query.join(Room).filter(Room.base_price >= search.min_price)
    if search.max_price:
        query = query.join(Room).filter(Room.base_price <= search.max_price)
    if search.star_rating:
        query = query.filter(Hotel.star_rating == search.star_rating)
    
    offset = (search.page - 1) * search.per_page
    return query.offset(offset).limit(search.per_page).all()

def create_room(db: Session, room: RoomCreate):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def create_booking(db: Session, booking: BookingCreate, user_id: int):
    db_booking = Booking(
        **booking.dict(),
        user_id=user_id,
        total_amount=calculate_total_amount(db, booking),
        booking_reference=str(uuid.uuid4())
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def calculate_total_amount(db: Session, booking: BookingCreate):
    room = db.query(Room).filter(Room.id == booking.room_id).first()
    if not room:
        raise ValueError("Room not found")
    delta = (booking.check_out_date - booking.check_in_date).days
    return room.base_price * delta

def get_user_bookings(db: Session, user_id: int):
    return db.query(Booking).filter(Booking.user_id == user_id).all()

def create_payment(db: Session, payment: schemas.PaymentBase):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def create_review(db: Session, review: ReviewCreate, user_id: int):
    db_review = Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def create_amenity(db: Session, amenity: AmenityCreate):
    db_amenity = Amenity(**amenity.dict())
    db.add(db_amenity)
    db.commit()
    db.refresh(db_amenity)
    return db_amenity

def create_hotel_image(db: Session, image: HotelImageCreate):
    db_image = HotelImage(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image