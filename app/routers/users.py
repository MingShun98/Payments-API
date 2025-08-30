from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str

users = []

@router.post("/")
def create_user(user: UserCreate):
    new_user = {"id": len(users)+1, "username": user.username, "email": user.email}
    users.append(new_user)
    return new_user

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}
