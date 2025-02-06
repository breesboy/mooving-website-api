from fastapi import FastAPI
from src.bookings.routes import booking_router
from src.db.main import init_db
from src.auth.routes import auth_router



version = "v1"
description=""


app = FastAPI(
    title="Moving Website API",
    description=description,
    version=version,
)

app.include_router(booking_router,prefix=f"/api/{version}/bookings", tags=["Bookings"])


app.include_router(auth_router,prefix=f"/api/{version}/auth", tags=["Auth"])