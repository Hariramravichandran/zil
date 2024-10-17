import asyncpg


class Database():
    pool=None
    @classmethod
    async def init_db(cls):
        cls.pool=await asyncpg.create_pool("postgresql://postgres:1527@localhost/sample")


    async def close_db(cls):
        await cls.pool.close()