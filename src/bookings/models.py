from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class Bookings(SQLModel, table=True):
	__tablename__ = "bookings"

	uid : uuid.UUID = Field(
		sa_column= Column(
			pg.UUID,
			nullable=False,
			primary_key=True,
			default=uuid.uuid4
		)
	)
	pickup_address : str
	dropoff_address : str
	moving_date: datetime = Field(Column(pg.TIMESTAMP))
	description : str
	status : str
	created_at : datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
	updated_at : datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))



	def __repr__(self):
		return f"<Booking by user {self.user_uid} on {self.moving_date}>"