from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import admin
from keyboards.default.buttton import til_tanlash, kirish_ru, locatsiya_ru, bosh_menu_only_ru
from loader import dp, bot
from utils.db_api.users_sql import Database_User

db = Database_User()


class RegState_ru(StatesGroup):
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


@dp.message_handler(text="🏠Главное меню", state=[RegState_ru.name, RegState_ru.id_pass, RegState_ru.birthday_date,
                                                 RegState_ru.phone_nomer, RegState_ru.phone_nomer_add, RegState_ru.loco,
                                                 RegState_ru.loco_text, RegState_ru.passport_photo,
                                                 RegState_ru.prapiska_photo])
async def uzewrft_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Здравствуйте и добро пожаловать в бот Tuk Cargo!", reply_markup=kirish_ru)
    await state.finish()




@dp.message_handler(text="/start", state=[RegState_ru.name, RegState_ru.id_pass, RegState_ru.birthday_date,
                                                 RegState_ru.phone_nomer, RegState_ru.phone_nomer_add, RegState_ru.loco,
                                                 RegState_ru.loco_text, RegState_ru.passport_photo,
                                                 RegState_ru.prapiska_photo])
async def uzewrft_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Здравствуйте и добро пожаловать в бот Tuk Cargo!", reply_markup=kirish_ru)
    await state.finish()

@dp.message_handler(text="🏠Главное меню")
async def uzewrfg_ru(message: types.Message):
    await message.answer(f"Здравствуйте и добро пожаловать в бот Tuk Cargo!", reply_markup=kirish_ru)





@dp.message_handler(text="🇷🇺Русский")
async def uzstart_ru(message: types.Message):
    await message.answer(f"Здравствуйте и добро пожаловать в бот Tuk Cargo!", reply_markup=kirish_ru)


@dp.message_handler(text="♻️Регистрация")
async def kirish_fun_ru(message: types.Message):
    await message.answer(f"Введите свое имя и фамилию: ", reply_markup=bosh_menu_only_ru)
    await RegState_ru.name.set()


@dp.message_handler(state=RegState_ru.name)
async def name_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"name": message.text}
    )
    await message.answer(f"Введите свой идентификационный номер Cardo: ")
    await RegState_ru.cardo_id.set()


@dp.message_handler(state=RegState_ru.cardo_id)
async def name_ru(message: types.Message, state: FSMContext):
    photo = open("./data/idcard.png", "rb")
    await state.update_data(
        {"cargo_id": message.text}
    )
    await message.answer_photo(photo=photo, caption="Введите номер удостоверения личности или номер паспорта:\n"
                                                    f"Например: <b>AB1231122</b> или <b>123456789012345</b>",
                               reply_markup=bosh_menu_only_ru)
    await RegState_ru.id_pass.set()


@dp.message_handler(lambda message: len(message.text) == 15 or len(message.text) == 9, state=RegState_ru.id_pass)
async def id_passdfas_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"id_pass": message.text}
    )
    await message.answer(f"введите вашу дату рождения:\n"
                         f"Например: <b>23/12/2000</b>")
    await RegState_ru.birthday_date.set()


@dp.message_handler(state=RegState_ru.id_pass)
async def id_passdfas_ru(message: types.Message):
    await message.answer(f"Введите правильную форму (номер удостоверения личности или паспорт):\n"
                         f"Например: <b>AB1231122</b> или <b>123456789012345</b>")


# tugulgan sana
@dp.message_handler(lambda message: len(message.text) >= 8 or len(message.text) <= 10, state=RegState_ru.birthday_date)
async def fsadfa_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"birthday_date": message.text}
    )
    await message.answer(f"Введите свой номер телефона:\n"
                         f"Например: <b>998990001122</b>")
    await RegState_ru.phone_nomer.set()


@dp.message_handler(state=RegState_ru.birthday_date)
async def id_pasas_ru(message: types.Message):
    await message.answer(f"Введите правильную форму (Дата рождения):\n"
                         f"Например: <b>23/12/2000</b>")


# tefefon nomer
@dp.message_handler(lambda message: len(message.text) == 12, state=RegState_ru.phone_nomer)
async def fswrera_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_nomer": message.text}
    )
    await message.answer(f"Введите дополнительный номер телефона:\n"
                         f"Например: <b>998993331122</b>")
    await RegState_ru.phone_nomer_add.set()


@dp.message_handler(state=RegState_ru.phone_nomer)
async def id_pasas_ru(message: types.Message):
    await message.answer(f"Введите правильную форму (номер телефона):\n"
                         f"Masalan: <b>998990001122</b>")


# qoshimcha telfon nomer
@dp.message_handler(lambda message: len(message.text) == 12, state=RegState_ru.phone_nomer_add)
async def fswrdsfa_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_nomer_add": message.text}
    )
    await message.answer(f"Отправьте адрес доставки", reply_markup=locatsiya_ru)
    await RegState_ru.loco.set()


@dp.message_handler(state=RegState_ru.phone_nomer_add)
async def id_pasdfsdfs_ru(message: types.Message):
    await message.answer(f"Введите правильную форму (дополнительная опция телефона):\n"
                         f"Например: <b>998990001122</b>", reply_markup=bosh_menu_only_ru)


# yetkazish manzili

@dp.message_handler(content_types='location', state=RegState_ru.loco)
async def locofun_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"lat": message.location.latitude,
         'lon': message.location.longitude}
    )
    await message.answer(f"Пожалуйста, пришлите адрес доставки:\n"
                         f"Например: <b>Чиланзорский район, город Ташкент, 17-квартал 1-63</b>",
                         reply_markup=bosh_menu_only_ru)
    await RegState_ru.loco_text.set()


@dp.message_handler(state=RegState_ru.loco)
async def locofun_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Введите правильно. Отправьте свой адрес, используя кнопку ниже.")


@dp.message_handler(state=RegState_ru.loco_text)
async def fadsfa_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"loco_text": message.text}
    )
    await message.answer(f"Отправить фото паспорта:")
    await RegState_ru.passport_photo.set()


@dp.message_handler(content_types='photo', state=RegState_ru.passport_photo)
async def dafegas_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"file_path_1": message.photo[-1].file_id}
    )

    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path

    destination = f'./data/rasm/{message.from_user.id}_1.jpg'
    await bot.download_file(file_path, destination)

    # await bot.download_file_by_id(file_path=message.photo[-1].file_id, destination=f"./data/rasm/{message.from_user.id}_1.jpg")

    await message.answer(f"Отправьте фото обложки паспорта:")
    await RegState_ru.prapiska_photo.set()


@dp.message_handler(content_types='photo', state=RegState_ru.prapiska_photo)
async def daghfas_ru(message: types.Message, state: FSMContext):
    # await bot.download_file_by_id(file_path=message.photo[-1].file_id, destination=f"./data/rasm/{message.from_user.id}_2.jpg")

    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path

    destination = f'./data/rasm/{message.from_user.id}_2.jpg'
    await bot.download_file(file_path, destination)

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
        await bot.send_message(chat_id=7010118152, text=f"Xato start_ru.py daghfas_ru page 220")

    await message.answer(f"Ваша информация получена.", reply_markup=kirish_ru)
    await state.finish()
