from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    GUEST = "GUEST"
    HOTEL_MANAGER = "HOTEL_MANAGER"
    ADMIN = "ADMIN"

class RoomType(str, Enum):
    STANDARD = "STANDARD"
    DELUXE = "DELUXE"
    SUITE = "SUITE"

class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]

class UserResponse(UserBase):
    id: int
    role: UserRole
    created_at: datetime
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    user: UserResponse

class HotelBase(BaseModel):
    name: str
    description: Optional[str]
    address: str
    city: str
    country: str
    star_rating: int = Field(ge=1, le=5)
    phone: str
    email: EmailStr
    latitude: Optional[float]
    longitude: Optional[float]

class HotelCreate(HotelBase):
    pass

class HotelResponse(HotelBase):
    id: int
    created_at: datetime
    rooms: List["RoomResponse"] = []
    images: List["HotelImageResponse"] = []
    amenities: List["AmenityResponse"] = []
    
    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    hotel_id: int
    room_number: str
    room_type: RoomType
    name: str
    description: Optional[str]
    max_occupancy: int = Field(ge=1)
    base_price: float = Field(ge=0.0)

class RoomCreate(RoomBase):
    pass

class RoomResponse(RoomBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    hotel_id: int
    room_id: int
    check_in_date: datetime
    check_out_date: datetime
    guests: int = Field(ge=1)
    special_requests: Optional[str]

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int
    user_id: int
    total_amount: float
    status: BookingStatus
    booking_reference: str
    created_at: datetime
    hotel: HotelResponse
    room: RoomResponse
    
    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    booking_id: int
    amount: float
    currency: str = "usd"

class PaymentResponse(PaymentBase):
    id: int
    stripe_payment_intent_id: str
    status: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    hotel_id: int
    rating: int = Field(ge=1, le=5)
    comment: Optional[str]

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    created_at: datetime
    user: UserResponse
    
    class Config:
        orm_mode = True

class AmenityBase(BaseModel):
    name: str
    category: Optional[str]

class AmenityCreate(AmenityBase):
    pass

class AmenityResponse(AmenityBase):
    id: int
    
    class Config:
        orm_mode = True

class HotelImageBase(BaseModel):
    hotel_id: int
    url: str
    alt_text: Optional[str]

class HotelImageCreate(HotelImageBase):
    pass

class HotelImageResponse(HotelImageBase):
    id: int
    
    class Config:
        orm_mode = True

class HotelSearch(BaseModel):
    destination: Optional[str]
    check_in_date: Optional[datetime]
    check_out_date: Optional[datetime]
    guests: Optional[int]
    min_price: Optional[float]
    max_price: Optional[float]
    star_rating: Optional[int]
    page: int = 1
    per_page: int = 20