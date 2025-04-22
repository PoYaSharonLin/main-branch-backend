from sqlalchemy.orm import Session
from fastapi import Request, HTTPException
from authlib.integrations.starlette_client import OAuth
from schemas.user import UserRead
from controllers.user import find_user, create_user
from controllers.token import create_access_token
from dotenv import load_dotenv
import os

load_dotenv()

oauth = OAuth()
oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    client_kwargs={'scope': 'read:user read:project'},
)

async def login_via_github(request: Request):
    callback_url = request.url_for('github_login_callback')
    return await oauth.github.authorize_redirect(request, callback_url)

async def auth_github(request: Request, db: Session):
    token = await oauth.github.authorize_access_token(request)
    user_info = await oauth.github.get('https://api.github.com/user', token=token)
    profile = user_info.json()

    db_user_auth = find_user(db, 'github', profile["id"])
    if db_user_auth != None:
        user = UserRead.model_validate(db_user_auth.user)
        return {"user": user, "access_token": create_access_token(user.model_dump()), "token_type":"Bearer"}
    
    db_user = create_user(db, 'github', profile["id"], profile["login"])
    user = UserRead.model_validate(db_user)

    return {"user": user, "access_token": create_access_token(user.model_dump()), "token_type":"Bearer"}