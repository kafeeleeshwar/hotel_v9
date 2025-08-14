from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.database import create_tables
from app.routers import auth, hotels, bookings, users, payments, ai
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="LuxStay AI API",
    description="API for luxury hotel booking platform with AI recommendations",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory for serving images
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(hotels.router, prefix="/api/hotels", tags=["hotels"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["bookings"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(ai.router, prefix="/api/ai", tags=["ai"])

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app_name": "LuxStay AI API",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    }