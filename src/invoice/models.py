from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class User(SQLModel, table=True):
	__tablename__ = "invoices"

	uid : uuid.UUID = Field(
		sa_column= Column(
			pg.UUID,
			nullable=False,
			primary_key=True,
			default=uuid.uuid4
		)
	)
	booking_uid : uuid.UUID = Field(foreign_key="users.uid", ondelete="SET NULL")
	stripe_invoice_id : uuid.UUID
	amount : float
	status: str
	issued_at : datetime = Field(default_factory=datetime.now)
	paid_at : datetime = Field(default=None, nullable=True)


	def __repr__(self):
		return f"<User {self.username}>"