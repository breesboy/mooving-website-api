from pydantic import BaseModel
import uuid
from datetime import datetime,date



class Bookings(BaseModel):
	uid : uuid.UUID
	pickup_address : str
	dropoff_address : str
	moving_date: date
	description : str
	status : str
	# agreed_price : float
	created_at : datetime
	updated_at : datetime


class CreateBooking(BaseModel):
	pickup_address : str
	dropoff_address : str
	moving_date: str
	description : str
	status : str


class UpdateBooking(BaseModel):
	pickup_address : str
	dropoff_address : str
	moving_date: datetime
	description : str
	status : str
	# agreed_price : float


class RescheduleBooking(BaseModel):
	moving_date: datetime


class UpdateBookingStatus(BaseModel):
	status: str
