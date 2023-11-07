from fastapi import APIRouter, Depends, status
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)



@router.post("/", response_model=UserDisplay, status_code=status.HTTP_200_OK)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)



@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)



@router.get("/{id}", response_model=UserDisplay, status_code=status.HTTP_200_OK)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_one_users(db, id=id)


@router.get('/username/{usrname}', response_model=List[UserDisplay], status_code=status.HTTP_200_OK)
def get_usr_by_name(usrname: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_usrname(db, usrname=usrname)



@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db=db, request=request, id=id)



@router.get('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db=db, id=id)
