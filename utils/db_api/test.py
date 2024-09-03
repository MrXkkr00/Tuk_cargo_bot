import asyncio

from utils.db_api.users_sql import Database_User


async def test():
    db = Database_User()
    await db.create()
    # await db.create_table_users()

    # users = await db.select_all_Tavarlar()
    # print(users)
    # await db.add_Tavar(user_id="23131", t_turi="330", t_soni="2", t_nomer="4", t_narxi="40000")
    # await db.add_Tavar(user_id="23131", t_turi="800", t_soni="2", t_nomer="4", t_narxi="80000")
    # users = await db.select_all_Tavarlar()
    user1 = await db.select_all_users()
    for user in user1:
        print(user)


    # await db.delete_Tavar(user_id="23131")
    # users = await db.select_all_Tavarlar()
    # print(users)


asyncio.run(test())

#
# soat = "10-11"
# print(soat[:2])
# print(soat[2])
# print(soat[3:5])
