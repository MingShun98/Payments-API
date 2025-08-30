from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Optional

from app.db.db import get_db
from app.db.models import *
from app.schemas import *

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("",response_model=TodoRead,status_code=status.HTTP_201_CREATED) # Create
def create_todo(body: TodoCreate, db: Session = Depends(get_db)):
    try:
        # (Optional) enforce business rule example:
        # if db.query(models.Todo).filter_by(title=body.title).first():
        #     raise HTTPException(status_code=409, detail="DUPLICATE_TITLE")
        todo = Todo(title=body.title, done=body.done)
        db.add(todo)
        db.commit()
        db.refresh(todo)
    except Exception:
        db.rollback()
        raise
    # Optional Location header
    # Response(headers={"Location": f"/api/v1/todos/{todo.id}"})

    return todo  # FastAPI will serialize using TodoRead

# Read: List with optional filters and pagination
@router.get("", response_model=list[TodoRead], status_code=status.HTTP_200_OK)
def list_todos(done:bool , db: Session = Depends(get_db)):
    try: 
        q = db.query(Todo)
         
        if done is not None: 
            q = q.filter(Todo.done == done) 
        
        return q.order_by(Todo.id).all() 
    except Exception: 
        db.rollback()
        raise
    return  

@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="TODO_NOT_FOUND")
    return todo

# UPDATE: full replace (PUT) or partial (PATCH)
@router.put("/{todo_id}", response_model=TodoCreate, status_code=status.HTTP_200_OK)
def put_todo(todo_id: int, body:TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(Todo).get(todo_id)
    if not todo: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='TODO_NOT_FOUND')
    todo.title = body.title
    todo.done = body.done
    db.commit() 
    db.refresh(todo)
    return todo

@router.patch("/{todo_id}", response_model=TodoRead, status_code=status.HTTP_200_OK)
def patch_todo(todo_id: int, body: TodoUpdate, db: Session = Depends(get_db)): 
    todo = db.query(Todo).get(todo_id)
    if not todo: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='TODO_NOT_FOUND')
    if body.title is not None: 
        todo.title = body.title
    if body.done is not None: 
        todo.done = body.done
    db.commit() 
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}", response_model=TodoRead, status_code=status.HTTP_200_OK)
def delete_todo(todo_id: int, body: TodoRead, db: Session = Depends(get_db)): 
    todo = db.query(Todo).get(todo_id)
    if not todo: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='TODO_NOT_FOUND')
    db.delete(todo)
    db.commit()
    return None


@router.get("/health/db")
def check_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))   # 👈 wrap with text()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}