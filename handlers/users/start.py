from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import admin
from keyboards.default.buttton import til_tanlash, kirish, locatsiya, bosh_menu_only
from loader import dp, bot
from utils.db_api.users_sql import Database_User
import asyncio
db = Database_User()


class RegState(StatesGroup):
    name = State()
    cardo_id = State()
    id_pass = State()
    birthday_date = State()
    phone_nomer = State()
    phone_nomer_add = State()
    loco = State()
    loco_text = State()
    passport_photo = State()
    prapiska_photo = State()
    
    
@dp.message_handler(text="sss")
async def fadfa(message: types.Message):
    await db.create()
    user1 = await db.select_all_users()
    for user in user1:
            print(user)
    
    

    
    

    



@dp.message_handler(text="🏠Bosh sahifa", state=[RegState.name, RegState.id_pass, RegState.birthday_date,
                                                RegState.phone_nomer, RegState.phone_nomer_add, RegState.loco,
                                                RegState.loco_text, RegState.passport_photo, RegState.prapiska_photo])
async def uzewrft(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu Alaykum Tuk Cargo botiga hush kelibsiz!", reply_markup=kirish)
    await state.finish()




@dp.message_handler(text="/start", state=[RegState.name, RegState.id_pass, RegState.birthday_date,
                                                RegState.phone_nomer, RegState.phone_nomer_add, RegState.loco,
                                                RegState.loco_text, RegState.passport_photo, RegState.prapiska_photo])
async def uzewrft(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu Alaykum Tuk Cargo botiga hush kelibsiz!", reply_markup=kirish)
    await state.finish()

@dp.message_handler(text="🏠Bosh sahifa")
async def uzewrfg(message: types.Message):
    await message.answer(f"Assalomu Alaykum Tuk Cargo botiga hush kelibsiz!", reply_markup=kirish)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"🇺🇿Tilni tanlang\n"
                         f"🇷🇺Выберите язык",
                         reply_markup=til_tanlash)


@dp.message_handler(text="🇺🇿 O'zbek")
async def uzstart(message: types.Message):
    await message.answer(f"Assalomu Alaykum Tuk Cargo botiga hush kelibsiz!", reply_markup=kirish)


@dp.message_handler(text="♻️Ro'yhatdan o'tish")
async def kirish_fun(message: types.Message):
    await message.answer(f"Ism Familyangizni kiriting: ", reply_markup=bosh_menu_only)
    await RegState.name.set()


@dp.message_handler(state=RegState.name)
async def name(message: types.Message, state: FSMContext):
    # photo = open("./data/idcard.png", "rb")
    await message.answer(f"Cardo ID raqamingizni kiriting: ")
    await state.update_data(
        {"name": message.text}
    )
    await RegState.cardo_id.set()



@dp.message_handler(state=RegState.cardo_id)
async def name(message: types.Message, state: FSMContext):
    photo = open("./data/idcard.png", "rb")
    await state.update_data(
        {"cargo_id": message.text}
    )
    await message.answer_photo(photo=photo, caption="ID card raqami yoki Passport raqamini kiriting:\n"
                                                    f"Masalan: <b>AB1231122</b> yoki <b>123456789012345</b>",
                               reply_markup=bosh_menu_only)
    await RegState.id_pass.set()


@dp.message_handler(lambda message: len(message.text) == 15 or len(message.text) == 9, state=RegState.id_pass)
async def id_passdfas(message: types.Message, state: FSMContext):
    await state.update_data(
        {"id_pass": message.text}
    )
    await message.answer(f"Tug'ilgan sanagizni kiriting:\n"
                         f"Masalan: <b>23/12/2000</b>")
    await RegState.birthday_date.set()


@dp.message_handler(state=RegState.id_pass)
async def id_passdfas(message: types.Message):
    await message.answer(f"To'g'ri shaklda kiriting (ID  raqami yoki Passport):\n"
                         f"Masalan: <b>AB1231122</b> yoki <b>123456789012345</b>")


# tugulgan sana
@dp.message_handler(lambda message: len(message.text) >= 8 or len(message.text) <= 10, state=RegState.birthday_date)
async def fsadfa(message: types.Message, state: FSMContext):
    await state.update_data(
        {"birthday_date": message.text}
    )
    await message.answer(f"Telefon raqamingizni kiriting:\n"
                         f"Masalan: <b>998990001122</b>")
    await RegState.phone_nomer.set()


@dp.message_handler(state=RegState.birthday_date)
async def id_pasas(message: types.Message):
    await message.answer(f"To'g'ri shaklda kiriting (Tug'ilgan sana):\n"
                         f"Masalan: <b>23/12/2000</b>")


# tefefon nomer
@dp.message_handler(lambda message: len(message.text) == 12, state=RegState.phone_nomer)
async def fswrera(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_nomer": message.text}
    )
    await message.answer(f"Qo'shimcha telefon raqamingizni kiriting:\n"
                         f"Masalan: <b>998993331122</b>")
    await RegState.phone_nomer_add.set()


@dp.message_handler(state=RegState.phone_nomer)
async def id_pasas(message: types.Message):
    await message.answer(f"To'g'ri shaklda kiriting (telefon raqami ):\n"
                         f"Masalan: <b>998990001122</b>")


# qoshimcha telfon nomer
@dp.message_handler(lambda message: len(message.text) == 12, state=RegState.phone_nomer_add)
async def fswrdsfa(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_nomer_add": message.text}
    )
    await message.answer(f"Yetkazib berish manzilini yuboring", reply_markup=locatsiya)
    await RegState.loco.set()


@dp.message_handler(state=RegState.phone_nomer_add)
async def id_pasdfsdfs(message: types.Message):
    await message.answer(f"To'g'ri shaklda kiriting (qo'shimcha telefon raqami ):\n"
                         f"Masalan: <b>998990001122</b>", reply_markup=bosh_menu_only)


# yetkazish manzili

@dp.message_handler(content_types='location', state=RegState.loco)
async def locofun(message: types.Message, state: FSMContext):
    await state.update_data(
        {"lat": message.location.latitude,
         'lon': message.location.longitude}
    )
    await message.answer(f"Manzilingizni yozib ham yuboring:\n"
                         f"Masalan: <b>Toshkent shahar Chilonzor tumani 17-kvartol 1-63</b>",
                         reply_markup=bosh_menu_only)
    await RegState.loco_text.set()


@dp.message_handler(state=RegState.loco)
async def locofun(message: types.Message, state: FSMContext):
    await message.answer(f"To'g'ri kiriting Manzilingiz locatsiyasini pasdagi tugma orqali yuboring")


@dp.message_handler(state=RegState.loco_text)
async def fadsfa(message: types.Message, state: FSMContext):
    await state.update_data(
        {"loco_text": message.text}
    )
    await message.answer(f"Passport fotosuratini yuboring:")
    await RegState.passport_photo.set()


@dp.message_handler(content_types='photo', state=RegState.passport_photo)
async def dafegas(message: types.Message, state: FSMContext):
    await state.update_data(
        {"file_path_1": message.photo[-1].file_id}
    )
    
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path

    destination = f'./data/rasm/{message.from_user.id}_1.jpg'
    await bot.download_file(file_path, destination)

    # await bot.download_file_by_id(file_path=message.photo[-1].file_id,
    #                               destination=f"./data/rasm/{message.from_user.id}_1.jpg")

    await message.answer(f"Passport prapiska varaqi suratini yuboring:")
    await RegState.prapiska_photo.set()


@dp.message_handler(content_types='photo', state=RegState.prapiska_photo)
async def daghfas(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path

    destination = f'./data/rasm/{message.from_user.id}_2.jpg'
    await bot.download_file(file_path, destination)
    
    # await bot.download_file_by_id(file_path=message.photo[-1].file_id,
    #                               destination=f"./data/rasm/{message.from_user.id}_2.jpg")
    data = await state.get_data()
    name = data.get("name")
    cargo_id = data.get("cargo_id")
    id_pass = data.get("id_pass")
    birthday_date = data.get("birthday_date")

    phone_nomer = data.get("phone_nomer")
    phone_nomer_add = data.get("phone_nomer_add")

    lat = data.get("lat")
    lon = data.get("lon")

    loco_text = data.get("loco_text")

    file_path_1 = data.get('file_path_1')
    file_path_2 = message.photo[-1].file_id

    # print(name)
    # print(id_pass)
    # print(birthday_date)
    # print(phone_nomer)
    # print(phone_nomer_add)
    # print(lat)
    # print(lon)
    # print(loco_text)
    await bot.send_message(chat_id=admin, text=f"🙋🏻‍♂Mijoz :    <b>{name}</b>\n"
                                               f"📝Cargo_id :    <b>{cargo_id}</b>\n"
                                               f"📝ID_pass :    <b>{id_pass}</b>\n"
                                               f"🍰Tug'ilgan sana :    <b>{birthday_date}</b>\n"
                                               f"📲Telefon raqami :    <b>+{phone_nomer}</b>\n"
                                               f"☎Qo'shimcha raqami :    <b>+{phone_nomer_add}</b>\n"
                                               f"📍Manzil :    <b>{loco_text}</b>\n")
    await bot.send_location(chat_id=admin, latitude=lat, longitude=lon)
    await bot.send_photo(chat_id=admin, photo=file_path_1)
    await bot.send_photo(chat_id=admin, photo=file_path_2)

    vaqt = str(strftime(f"%d/%m/%Y", gmtime()))
    try:
        await db.create()
        name = name + " " + cargo_id
        await db.add_user(user_id=str(message.from_user.id), id_pass=str(id_pass), name=str(name),
                          birthday_date=str(birthday_date), phone_nomer=str(phone_nomer),
                          phone_nomer_add=str(phone_nomer_add),
                          loco_lat=str(lat), loco_lon=str(lon), loco_text=str(loco_text),
                          passport_photo=str(file_path_1),
                          prapiska_photo=str(file_path_2), enter_date=str(vaqt))
        await db.disconnect()
    except:
        await bot.send_message(chat_id=7010118152, text=f"Xato start.py daghfas page 209")

    await message.answer(f"Ma'lumotlaringiz qabul qilindi.", reply_markup=kirish)
    await state.finish()
