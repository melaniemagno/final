from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


Base = declarative_base()

class Users(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=False)
  name = Column(String)
  email = Column(String)
  password = Column(String)
  username = Column(String)

  def __repr__(self):
    return f"<Users(user_id={self.id}, name='{self.name}', email='{self.email}', username='{self.username}', password='{self.password}')>"

class Posts(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True, autoincrement=False)
  post = Column(String)

  def __repr__(self):
    return f"<Posts(post_id={self.id}, post='{self.name}')>"

class UsersCreate(BaseModel):
  id: int
  name: str
  email: str
  password: str
  username: str

class UsersRead(UsersCreate):
  class Config:
    orm_mode = True

class PostCreate(BaseModel):
  id: int
  Post: str

class PostRead(PostCreate):
  class Config:
    orm_mode = True