from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

from model import Base, Users, UsersRead, UsersCreate, Posts, PostCreate, PostRead

#following prior code from final example given to us
app = FastAPI()

app.add_middleware(
  CORSMiddleware, 
  allow_origins=["*"], 
  allow_credentials=True, 
  allow_methods=["*"],
  allow_headers=["*"],
)

SQLALCHEMY_DB_URL = "sqlite:///./data.db"
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
  db = SessionLocal()
  try:
#returns the same db every time
    yield db
  finally:
    db.close()

#the return method is a foreach loop but backwards
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
  users_list = db.query(Users).all()
  return [{"id": u.id, "name": u.name, "email": u.email, "password": u.password, "username": u.username} for u in users_list]

@app.get("/users_count")
async def get_user_count(db: Session = Depends(get_db)):
    return db.query(Users).count()

@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
  post_list = db.query(Posts).all()
  return [{"id": p.id, "post": p.post} for p in post_list]

@app.get("/posts_count")
async def get_post_count(db: Session = Depends(get_db)):
    return db.query(Posts).count()

@app.get("/users/{id}")
async def get_user_with_id(id: int, db: Session = Depends(get_db)):
  user = db.query(Users).filter(Users.id == id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="User does not yet exist")
  return user   
    

@app.get("/posts/{id}")
async def get_post_with_id(id: int, db: Session = Depends(get_db)):
  post = db.query(Posts).filter(Posts.id == id).first()
  if post is None:
    raise HTTPException(status_code=404, detail="Post does not yet exist")
  return post

@app.post("/users")
async def create_user(user: Users, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == user.id).first() is not None:
    raise HTTPException(status_code=400, detail="User already exists, try again.")
  #else if
  new_user = Users(id=user.id, name=user.name, email=user.email, username=user.username, password=user.password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@app.post("/posts")
async def create_post(post: Posts, db: Session = Depends(get_db)):
  if db.query(Posts).filter(Posts.id == post.id).first() is not None:
    raise HTTPException(status_code=400, detail="Post already exists, try again.")
  #else if
  new_post = Posts(id=post.id, post=post.name)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

@app.put("/users/{id}")
async def updating_user(id: int, user: UsersCreate, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
    raise HTTPException(status_code=404, detail="User not created")
  db.query(Users).filter(Users.id == id).update({Users.name: user.name, Users.name: user.name, Users.email: user.email, Users.password: user.password, Users.username: user.username})
  db.commit()
  return db.query(Users).filter(Users.id == id).first()

@app.put("/posts/{id}")
async def updating_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
  if db.query(Posts).filter(Posts.id == id).first() is None:
    raise HTTPException(status_code=404, detail="post was not created")
  db.query(Posts).filter(Posts.id == id).update({Posts.post: post.post})
  db.commit()
  return db.query(Posts).filter(Posts.id == id).first()

@app.patch("/users/{id}/name")
async def updating_user_name(id: int, name: str, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
    raise HTTPException(status_code=404, detail="User;s name was not updated")
  db.query(Users).filter(Users.id == id).update({Users.name: name})
  db.commit()
  return db.query(Users).filter(Users.id == id).first()

@app.patch("/users/{id}/email")
async def updating_user_email(id: int, email: str, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
    raise HTTPException(status_code=404, detail="email was not updated")
  db.query(Users).filter(Users.id == id).update({Users.email: email})
  db.commit()
  return db.query(Users).filter(Users.id == id).first()

@app.patch("/users/{id}/username")
async def updating_user_username(id: int, username: str, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
    raise HTTPException(status_code=404, detail="Username was not updated")
  db.query(Users).filter(Users.id == id).update({Users.username: username})
  db.commit()
  return db.query(Users).filter(Users.id == id).first()

@app.patch("/users/{id}/password")
async def updating_user_password(id: int,  password: str,  db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
    raise HTTPException(status_code=404, detail="password was not updated")
  db.query(Users).filter(Users.id == id).update({Users.password: password})
  db.commit()
  return db.query(Users).filter(Users.id == id).first()

@app.patch("/posts/{id}/post")
async def updating_post_post(id: int, post: str, db: Session = Depends(get_db)):
  if db.query(Posts).filter(Posts.id == id).first() is None:
    raise HTTPException(status_code=404, detail="post was not updated")
  db.query(Posts).filter(Posts.id == id).update({Posts.post: post})
  db.commit()
  return db.query(Posts).filter(Posts.id == id).first()

@app.delete("/users/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
  if db.query(Users).filter(Users.id == id).first() is None:
      raise HTTPException(status_code=404, detail="user not found")
  db.query(Users).filter(Users.id == id).delete()
  db.commit()
  return {"message": "User deleted"}

@app.delete("/posts/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)):
  if db.query(Posts).filter(Posts.id == id).first() is None:
      raise HTTPException(status_code=404, detail="post not found")
  db.query(Posts).filter(Posts.id == id).delete()
  db.commit()
  return {"message": "Post deleted"}





