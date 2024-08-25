from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from fastapi import RedirectResponse
from app.main import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, templates, get_current_user
from database.queries import get_user_by_username, insert_user
from mysql.connector import connect
from database.connection import get_db_connection  # Импортируем функцию подключения к БД

router = APIRouter()

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: connect = Depends(get_db_connection)):
    user = get_user_by_username(db, username)
    
    if user and user[1] == password:  # Предполагаем, что пароль хранится в user[1]
        access_token = create_access_token(data={"sub": username})
        response = RedirectResponse(url="/profile", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response
    
    raise HTTPException(status_code=400, detail="Incorrect username or password")

@router.get("/profile")
async def profile(request: Request, token: str = Depends(get_current_user), db: connect = Depends(get_db_connection)):
    user = get_user_by_username(db, token)
    
    if user:
        return templates.TemplateResponse("profile.html", {"request": request, "username": token})
    
    raise HTTPException(status_code=404, detail="User not found")
