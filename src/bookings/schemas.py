from pydantic import BaseModel
import uuid
from datetime import datetime,date



class Bookings(BaseModel):
	uid : uuid.UUID
	firstName : str
	lastName : str
	email : str
	phoneNumber : str
	pickup_address : str
	dropoff_address : str
	moving_date: date
	service : str
	description : str
	status : str
	# agreed_price : float
	created_at : datetime
	updated_at : datetime


class CreateBooking(BaseModel):
	firstName : str
	lastName : str
	email : str
	phoneNumber : str
	pickup_address : str
	dropoff_address : str
	moving_date: str
	service : str
	description : str
	status : str


class UpdateBooking(BaseModel):
	firstName : str
	lastName : str
	phoneNumber : str
	pickup_address : str
	dropoff_address : str
	moving_date: date
	description : str
	status : str
	service : str
	# agreed_price : float


class RescheduleBooking(BaseModel):
	moving_date: date


class UpdateBookingStatus(BaseModel):
	status: str
