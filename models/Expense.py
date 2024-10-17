from db import Database

db=Database()

async def create_expenses(name,amount,category,date):
    try:
        async with db.pool.acquire() as conn:
            async with conn.transaction():
                e=await conn.fetch("insert into expenses (exp_id,name,amount,date)values ((select expense_id from expenses_cat where category=$3),$1,$2,$4)returning exp_id as id;",name,amount,category,date)
                
                exp={"expense_id":e[0]["id"],"name":name,"amount":amount,"category":category,}
                return exp

    except Exception as e:
        print(e)


async def get_expenses():
    try:
        async with db.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetch("select  * from expenses")
                
                


    except Exception as e:
        print(e)



async def get_month_expenses(year,month):
    try:
        async with db.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetch("select  * from expenses where extract (year from date)=$1 or extract (month from date)=$2")
                
                


    except Exception as e:
        print(e)


async def get_totals():
    try:
        async with db.pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetch("select (select sum(amount) as total_salary from expenses where exp_id in(select expense_id from expenses_cat where category='salary')),(select sum(amount)as total_expenses from expenses where exp_id in(select expense_id from expenses_cat where category!='salary'))")
                
                


    except Exception as e:
        print(e)