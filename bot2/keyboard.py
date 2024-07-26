from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

loccon = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Location', request_location=True
                    ),
     KeyboardButton(text='Contact', request_contact=True
                    ), ],
    [KeyboardButton(text='Back'),]
], resize_keyboard=True)

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='Phone'
    ),
        KeyboardButton(
            text='PC'
        ), ],
    [KeyboardButton(
        text='Laptop'
    ), ],

], resize_keyboard=True)

phonemenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='Redmi',
    ),
        KeyboardButton(
            text='Samsung',
        ), ],
    [KeyboardButton(text='Iphone'), KeyboardButton(text='Back')],
], resize_keyboard=True)

laptopmenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='HP',
    ),
        KeyboardButton(
            text='Acer',
        ), ],
    [KeyboardButton(text='Asus'), KeyboardButton(text='Back')],
], resize_keyboard=True)

pcmenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
        text='PC HP',
    ),]
], resize_keyboard=True)
