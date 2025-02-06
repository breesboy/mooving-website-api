from fastapi import APIRouter,Depends,status
from .schemas import UserCreateModel, UserModel, UserLoginModel
from .services import UserService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from typing import List
from .utils import create_access_token, decode_token, verify_password
from datetime import timedelta,datetime
from fastapi.responses import JSONResponse
from .dependencies import RefreshTokenBearer


auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2


@auth_router.post('/signup', response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user_Account(user_data:UserCreateModel, session: AsyncSession = Depends(get_session)):
	email = user_data.email
	username = user_data.username

	username_exists = await user_service.username_exists(username, session)

	if username_exists:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Username already exists")
	
	email_exists = await user_service.email_exists(email, session)

	if email_exists:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User email already exists")
	

	new_user = await user_service.create_user_Account(user_data,session)

	return new_user

@auth_router.get("/get_all_users", response_model=list[UserModel])
async def get_all_users(session:AsyncSession = Depends(get_session)):
	users = await user_service.get_all_users(session)

	return users


@auth_router.post("/login")
async def login_user(login_data:UserLoginModel, session: AsyncSession = Depends(get_session)):
	email = login_data.email
	password = login_data.password

	user = await user_service.get_user_by_email(email, session)

	if user is not None:
		password_valid = verify_password(password, user.password_hash)

		if password_valid:
			access_token = create_access_token(
				user_data={
					"user_uid": str(user.uid),
					"username": user.username,
					"email": user.email
				}
			)

			refresh_token = create_access_token(
				user_data={
					"user_uid": str(user.uid),
					"username": user.username,
					"email": user.email
				},
				refresh=True,
				expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
			)

			return JSONResponse(
				content={
					"message": "Login successful",
					"access_token": access_token,
					"refresh_token": refresh_token,
					"user":{
						"username": user.username,
						"email": user.email
					}
				}
			)
		
	raise HTTPException(
		status_code=status.HTTP_403_FORBIDDEN,
		detail="Invalid email or password"
	)


@auth_router.get("/refresh_token")
async def get_new_access_token(token_details: dict = Depends(RefreshTokenBearer())):
	expiry_timestamp = token_details['exp']

	if datetime.fromtimestamp(expiry_timestamp) > datetime.now():
		new_access_token = create_access_token(
			user_data=token_details['user']
		)

		return JSONResponse(
			content={
				"access_token": new_access_token
			}
		)
	
	raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")