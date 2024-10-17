import datetime
from fastapi import APIRouter,Body
from models import Expense

router=APIRouter()


@router.post("/expenses/")
async def create_expences(name:str=Body(...),amount:float=Body(...),category:str=Body(...),Date:datetime.date=Body(...)):
    return await Expense.create_expenses(name,amount,category,Date)




@router.get("/expenses/")
async def get_expences():
    return await Expense.get_expenses()



@router.get("/expenses/month/{year}/{month}/")
async def get_month_expences(year,month):
    return await Expense.get_month_expenses(year,month)


@router.get("/totals/")
async def get_totals():
    return await Expense.get_totals()