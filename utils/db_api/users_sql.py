from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database_User:

    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
        except Exception as e:
            print(f"Error creating connection pool: {e}")

    async def disconnect(self):

        try:
            if self.pool:
                await self.pool.close()
        except Exception as e:
            print(f"Error closing connection pool: {e}")

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id varchar(255),
            id_pass varchar(255),
            name varchar(255),
            birthday_date varchar(255),
            phone_nomer varchar(255),
            phone_nomer_add varchar(255),
            loco_lat varchar(255),
            loco_lon varchar(255),
            loco_text varchar(255),
            passport_photo varchar(255),
            prapiska_photo varchar(255),
            enter_date varchar(255)
            );
"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id: str = None, id_pass: str = None, name: str = None, birthday_date: str = None,
                       phone_nomer: str = None, phone_nomer_add: str = None, loco_lat: str = None, loco_lon: str = None,
                       loco_text: str = None, passport_photo: str = None, prapiska_photo: str = None, enter_date: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, id_pass, name,  birthday_date, phone_nomer, phone_nomer_add, loco_lat, loco_lon, 
        loco_text, passport_photo, prapiska_photo, enter_date ) 
        VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12 ) returning *
        """
        return await self.execute(sql, user_id, id_pass, name, birthday_date, phone_nomer, phone_nomer_add, loco_lat,
                                  loco_lon, loco_text, passport_photo, prapiska_photo, enter_date, fetchrow=True)





    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        return await self.execute("SELECT COUNT(*) FROM Users", fetchval=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
        
        

