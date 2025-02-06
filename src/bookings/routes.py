from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.bookings.schemas import Bookings, UpdateBooking,CreateBooking,UpdateBookingStatus,RescheduleBooking
from src.db.main import get_session
from .service import BookingService
from src.auth.dependencies import AccessTokenBearer


booking_router = APIRouter()
booking_service = BookingService()
access_token_bearer = AccessTokenBearer()



@booking_router.post("/new_booking", status_code=status.HTTP_201_CREATED, response_model=Bookings)
async def create_new_booking(booking_data: CreateBooking, session:AsyncSession = Depends(get_session)) -> dict:
	new_booking = await booking_service.create_new_booking(booking_data,session)

	return new_booking


@booking_router.get("/get_all_bookings", response_model = List[Bookings])
async def get_all_bookings(session:AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)):
	bookings = await booking_service.get_all_bookings(session)

	return bookings


@booking_router.get("/get_booking/{booking_uid}", response_model = Bookings)
async def get_booking(booking_uid:str, session:AsyncSession = Depends(get_session)):
	booking = await booking_service.get_booking(booking_uid,session)

	if booking is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")

	else:
		return booking



@booking_router.patch("/update_booking/{booking_uid}", response_model=Bookings)
async def update_booking(booking_uid:str, update_booking_data: UpdateBooking, session:AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)) -> dict:
	update_booking = await booking_service.update_booking(booking_uid,update_booking_data,session)

	if update_booking is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")

	else:
		return update_booking



@booking_router.patch("/reschedule_booking/{booking_uid}", response_model=Bookings)
async def reschedule_booking(booking_uid:str, reschedule_booking_data: RescheduleBooking, session:AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)) -> dict:
	reschedule_booking = await booking_service.reschedule_booking(booking_uid,reschedule_booking_data,session)

	if reschedule_booking is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")

	else:
		return reschedule_booking

@booking_router.patch("/booking_status/{booking_uid}")
async def update_booking_status(booking_uid:str, booking_status_data: UpdateBookingStatus, session:AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)) -> dict:
	booking_status = await booking_service.booking_status(booking_uid,booking_status_data,session)

	if booking_status is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")

	else:
		return booking_status


@booking_router.patch("/cancel_booking/{booking_uid}", response_model=Bookings)
async def cancel_booking(booking_uid:str, session:AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)) -> dict:
	cancel_booking = await booking_service.cancel_booking(booking_uid,session)

	if cancel_booking is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")

	else:
		return cancel_booking




# @booking_router.put("/", status_code=status.HTTP_204_NO_CONTENT)
# async def shit_bookingsssss(booking_uid:str, session:AsyncSession = Depends(get_session)):
# 	cancel_booking = await booking_service.cancel_booking(booking_uid,session)

# 	if cancel_booking is None:
# 		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Booking not found")


# 	else:
# 		return {}

