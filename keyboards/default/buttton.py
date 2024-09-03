from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bosh_menu_only = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Bosh sahifa")
        ]
    ], resize_keyboard=True
)

bosh_menu_only_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)

til_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek"),
            KeyboardButton(text="🇷🇺Русский")
        ],

    ], resize_keyboard=True
)

kirish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♻️Ro'yhatdan o'tish")
        ]
    ], resize_keyboard=True
)


kirish_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♻️Регистрация")
        ]
    ], resize_keyboard=True
)



locatsiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Joylashuvni yuborish",
                           request_location=True)
        ],
        [
            KeyboardButton(text="🏠Bosh sahifa")
        ]
    ], resize_keyboard=True
)


locatsiya_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Отправить местоположение",
                           request_location=True)
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)


admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔢Hisobot"),
            KeyboardButton(text="➡id kiritish")
        ]
    ], resize_keyboard=True
)
