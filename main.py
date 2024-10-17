from fastapi import FastAPI
from db import Database
from api import Expense

db=Database()

app=FastAPI()



app.include_router(Expense.router ,tags=["Expense"])


@app.on_event("startup")
async def startup():
    await db.init_db()
    print("connection open")


@app.on_event("shutdown")
async def shutdown():
    await db.close_db()
    print("connection close")