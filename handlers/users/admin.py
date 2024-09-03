import os
from time import strftime, gmtime

import xlsxwriter
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from data.config import admin
from keyboards.default.buttton import til_tanlash, kirish, locatsiya, bosh_menu_only, admin_keyboard
from loader import dp, bot
from utils.db_api.users_sql import Database_User

db = Database_User()


class User_idState(StatesGroup):
    user_id = State()


@dp.message_handler(text="/admin", user_id=admin)
async def admin_fun(message: types.Message):
    await message.answer(f"salom", reply_markup=admin_keyboard)


@dp.message_handler(text="/drop", user_id=7010118152)
async def admsadasfun(message: types.Message):
    await message.answer(f"Drop")
    await db.create()
    await db.drop_users()
    await db.create_table_users()
    await db.disconnect()


@dp.message_handler(text="/admin", user_id=7010118152)
async def admin_fun(message: types.Message):
    await message.answer(f"salom", reply_markup=admin_keyboard)


@dp.message_handler(text="/admin", user_id=984568970)
async def admin_fun(message: types.Message):
    await message.answer(f"salom", reply_markup=admin_keyboard)


#
@dp.message_handler(text="🔢Hisobot")
async def hisobdastion(message: types.Message):
    workbook = xlsxwriter.Workbook(f'data/Exel.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "User_id")
    worksheet.write('B1', "F.I.Sh")
    worksheet.write('C1', "Cargo_id")
    worksheet.write('D1', "Passport raqam")
    worksheet.write('E1', "Tug'ilgan kun")
    worksheet.write('F1', "Telefon nomer")
    worksheet.write('G1', "Qo'shimcha raqam")
    worksheet.write('H1', "Manzil")
    worksheet.write('I1', "Sana")
    son = 0
    try:
        await db.create()
        son = await db.count_users()


        for n in range(2, son + 2):
            user = await db.select_user(id=n - 1)
            name = user[3]
            cargo_id = name.split(' ')
            worksheet.write(f'A{n}', (user[1]))
            worksheet.write(f'B{n}', (user[3]))
            worksheet.write(f'C{n}', (cargo_id[-1]))
            worksheet.write(f'D{n}', (user[2]))
            worksheet.write(f'E{n}', (user[4]))
            worksheet.write(f'F{n}', (user[5]))
            worksheet.write(f'G{n}', (user[6]))
            worksheet.write(f'H{n}', (user[9]))
            worksheet.write(f'I{n}', (user[12]))
        await db.disconnect()
    except:
        await bot.send_message(chat_id=7010118152, text=f"Xato admin.py hisobdastion page 55")

    workbook.close()
    with open(f"data/Exel.xlsx", "rb") as photo_file:
        await bot.send_document(chat_id=message.from_user.id, document=photo_file)
    await message.answer(f"Hisobot jo'natildi")

    # await message.answer()


# @dp.message_handler(content_types=["photo"])
# async def hisobot_ffdsfon(message: types.Message):
# #     # Create the directory if it does not exist
# #
# #     # directory = "./data/rasm/"
# #     # if not os.path.exists(directory):
# #     #     os.makedirs(directory)
# #     file_info = await bot.get_file(message.photo[-1].file_id)
#     await bot.download_file_by_id(file_id=message.photo[-1].file_id, destination=f"./data/rasm/{message.from_user.id}_2.jpg")
# #     file_id = open(f"./data/rasm/{message.from_user.id}_1.jpg", "rb")
# #
# #     await message.answer_photo(photo=file_id)


@dp.message_handler(text="➡id kiritish")
async def hisobot_function(message: types.Message):
    await message.answer(f"Mijoz user id raqamini kiriting:", reply_markup=ReplyKeyboardRemove())
    await User_idState.user_id.set()


@dp.message_handler(state=User_idState.user_id)
async def fdaffasd(message: types.Message, state: FSMContext):
    user_id = message.text
    user = []
    try:
        await db.create()
        user = await db.select_user(user_id=str(user_id))
        await db.disconnect()
    except:
        await bot.send_message(chat_id=7010118152, text=f"Xato admin.py fdaffasd page 44")

    try:
        if not user is [] and not user is None:
            # print(user)
            lat = user[7]
            lon = user[8]
            file_id1 = open(f"./data/rasm/{user_id}_1.jpg", "rb")
            file_id2 = open(f"./data/rasm/{user_id}_2.jpg", "rb")
            # file_id1 = user[10]
            # file_id2 = user[11]

            await message.answer_location(latitude=lat, longitude=lon)
            await message.answer_photo(photo=file_id1)
            await message.answer_photo(photo=file_id2, reply_markup=admin_keyboard)
            file_id1.close()
            file_id2.close()

        else:
            await message.answer(f"Bu id raqam mavjud emas.\n"
                                 f"Tekshirib qaytadan kiriting.", reply_markup=admin_keyboard)

        await state.finish()

    except:
        await message.answer(f"Iltimos malumotlarni qayta yuklang botda xatolik")
        await state.finish()
