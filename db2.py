
#used this tutorial to help get db setup"
#https://www.sqlitetutorial.net/sqlite-python/creating-database/

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import sqlite3
from sqlite3 import Error
from main import Base, Users, UsersCreate

#defining function called create connection
#connects to a database that is specified by the 
#db_file variable input
async def create_connection(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as err:
    print(err)
  finally:
    if conn:
      conn.close()

async def create_user(user: Users):
  db_file = r"C:\Users\melan\Documents\serverside\final\database\data.db"
  conn = await create_connection(db_file)
  try:
    #cursor will execute the sql queries
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (Name, Email, Password, Username) VALUES (?, ?, ?, ?)",
                  (user.Name, user.Email, user.Password, user.Username))
    conn.commit()
    return user
  finally:
    if conn:
      conn.close()



#use r at the beginning of string to signal 
#use of raw string
if __name__ == '__main__':
  create_connection(r"C:\Users\melan\Documents\serverside\final\database\data.db")
