from aiogram import F, Router, Bot
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import keyboard

router = Router()
note10 = FSInputFile('10.jpg')
note11 = FSInputFile('11.jpg')
note12 = FSInputFile('12.jpg')
note13 = FSInputFile('13.jpg')
note13c = FSInputFile('13C.jpg')
notea3 = FSInputFile('A3.jpg')
notea2 = FSInputFile('A2.jpg')
note12pro = FSInputFile('12pro+.jpg')
pad = FSInputFile('pad.jpg')
padse = FSInputFile('pad se.jpg')

# -----------------------------------

fold6 = FSInputFile('Z-Fold-6.jpg')
flip6 = FSInputFile('flip6.jpg')
flip5 = FSInputFile('z flip5.jpg')
s24ultra = FSInputFile('s24 ultra.jpg')
s24 = FSInputFile('s24.jpg')
s23ultra = FSInputFile('s23-ultra.jpg')
s23plus = FSInputFile('S23+.jpg')
a55 = FSInputFile('A55.jpg')
tabultra = FSInputFile('tab s9 ultra.jpg')
tabsplus = FSInputFile('tab s9+.jpg')

# ---------------------------------------------

promax15 = FSInputFile('15 pro max.jpg')
pro15 = FSInputFile('15 pro.jpg')
promax14 = FSInputFile('14 pro max.jpg')
pro14 = FSInputFile('14 pro.jpg')
promax13 = FSInputFile('13 pro max.jpg')
pro13 = FSInputFile('13 pro.jpg')
promax12 = FSInputFile('12 pro max.jpg')
pro12 = FSInputFile('12 pro.jpg')
ipadpro = FSInputFile('ipad pro.jpg')
ipadair = FSInputFile('ipad air 5.jpg')

# ---------------------------------------------------

elitebook = FSInputFile('dragonfly.jpg')
langwaki = FSInputFile('langwaki.jpg')
zbook = FSInputFile('zbook.jpg')
pavilion15 = FSInputFile('pavilion15.jpg')
pavilion13 = FSInputFile('pavilionaero13.jpg')
pavilion = FSInputFile('pavilion.jpg')
envy = FSInputFile('envy.jpg')
omen = FSInputFile('omen.jpg')
spectre = FSInputFile('spectre.jpg')
victus = FSInputFile('victus.jpg')

# ------------------------------------------


swift14ai = FSInputFile('swift 14 ai.jpg')
swiftx14 = FSInputFile('swift x 14.jpg')
swiftgo16 = FSInputFile('swift go 16.jpg')
nitro16intel = FSInputFile('nitro 16 intel.jpg')
nitro14amd = FSInputFile('nitro 14 amd.jpg')
aspirevero16 = FSInputFile('Aspire-Vero-16.jpg')
aspire3amd = FSInputFile('aspire 3 amd.jpg')
predator = FSInputFile('predator 14.jpg')
travelmate = FSInputFile('travelmate.jpg')
porche = FSInputFile('porche design.jpg')

# ------------------------------------------------


vivobook = FSInputFile('vivobook pro.jpg')
m515 = FSInputFile('asusm515.jpg')
zenbookpro = FSInputFile('zenbook pro.jpg')
zenbooks = FSInputFile('zebook s.jpg.jpg')
expert = FSInputFile('expertbook premium.jpg')
chromeenter = FSInputFile('chromebook enterprise.jpg')
chromeflip = FSInputFile('chromebook flip.jpg')
rogzephyrus = FSInputFile('zephyrus.jpg')
rogstix = FSInputFile('stix.jpg')
myasus = FSInputFile('my asus.jpg')

# --------------------------------------------


envydesktop = FSInputFile('pc hp envy.jpg')
slimdesktop = FSInputFile('pc hp slim.jpg')
omen45l = FSInputFile('pc hp omen 45l.jpg')
victus15l = FSInputFile('pc hp victus.jpg')
paviliondesktop = FSInputFile('HP-PAVILION pc.jpg')
omen25l = FSInputFile('pc hp omen 25l.jpg')
omen40l = FSInputFile('pc hp omen 40l.jpg')
elitetower = FSInputFile('pc hp elitetower 600.jpg')
dualhp = FSInputFile('dual hp.jpg')
hpseries = FSInputFile('pc hp series 27 inch.jpg')


@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer('Choose product:', reply_markup=keyboard.keyboard)


@router.message(F.text == 'Phone')
async def phone(message: Message):
    await message.answer('Choose phone:', reply_markup=keyboard.phonemenu)


@router.message(F.text == 'Laptop')
async def phone(message: Message):
    await message.answer('Choose laptop:', reply_markup=keyboard.laptopmenu)


@router.message(F.text == 'PC')
async def phone(message: Message):
    await message.answer('Choose PC:', reply_markup=keyboard.pcmenu)


# --------------------------------------------------------
@router.message(F.text == 'Redmi')
async def redmi(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='r1'),
         InlineKeyboardButton(text='2', callback_data='r2'),
         InlineKeyboardButton(text='3', callback_data='r3'),
         InlineKeyboardButton(text='4', callback_data='r4'),
         InlineKeyboardButton(text='5', callback_data='r5'), ],
        [InlineKeyboardButton(text='6', callback_data='r6'),
         InlineKeyboardButton(text='7', callback_data='r7'),
         InlineKeyboardButton(text='8', callback_data='r8'),
         InlineKeyboardButton(text='9', callback_data='r9'),
         InlineKeyboardButton(text='10', callback_data='r10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. Redmi note 10\n2. Redmi note 11\n3. Redmi note 12\n4. Redmi note 13\n5. Redmi note 13C\n6. Redmi note 12 Pro+\n7. Redmi A3\n8. Redmi A2\n9. Redmi Pad\n10. Redmi Pad SE',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'r1')
async def r1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 10\nIt will cost you: $340\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note10, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r2')
async def r2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 11\nIt will cost you: $270\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note11, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r3')
async def r3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 12\nIt will cost you: $180\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note12, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r4')
async def r4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 13\nIt will cost you: $230\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note13, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r5')
async def r5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 13C\nIt will cost you: $200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note13c, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r6')
async def r6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Note 12 Pro+\nIt will cost you: $250\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=note12pro, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r7')
async def r7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi A3\nIt will cost you: $140\nThe photo:', chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=notea3, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r8')
async def r8(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi A2\nIt will cost you: $150\nThe photo:', chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=notea2, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r9')
async def r9(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Pad\nIt will cost you: $210\nThe photo:', chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pad, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'r10')
async def r10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Redmi Pad SE\nIt will cost you: $280\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=padse, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


# ----------------------------------------------------------------


@router.message(F.text == 'Samsung')
async def samsung(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='s1'),
         InlineKeyboardButton(text='2', callback_data='s2'),
         InlineKeyboardButton(text='3', callback_data='s3'),
         InlineKeyboardButton(text='4', callback_data='s4'),
         InlineKeyboardButton(text='5', callback_data='s5'), ],
        [InlineKeyboardButton(text='6', callback_data='s6'),
         InlineKeyboardButton(text='7', callback_data='s7'),
         InlineKeyboardButton(text='8', callback_data='s8'),
         InlineKeyboardButton(text='9', callback_data='s9'),
         InlineKeyboardButton(text='10', callback_data='s10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. Galaxy Z Fold6\n2. Galaxy Z Flip6\n3. Galaxy Z Flip5\n4. Galaxy S24 Ultra\n5. Galaxy S24\n6. Galaxy S23 Ultra\n7. Galaxy S23+\n8. Galaxy A55\n9. Galaxy Tab S9 Ultra\n10. Galaxy Tab S9+',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 's1')
async def s1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy Z Fold6\nIt will cost you: $2200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=fold6, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's2')
async def s2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy Z Flip6\nIt will cost you: $1300\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=flip6, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's3')
async def s3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy Z Flip5\nIt will cost you: $630\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=flip5, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's4')
async def s4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy S24 Ultra\nIt will cost you: $1300\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=s24ultra, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's5')
async def s5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy S24\nIt will cost you: $470\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=s24, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's6')
async def s6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy S23 Ultra\nIt will cost you: $120\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=s23ultra, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's7')
async def s7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy S23+\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=s23plus, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's8')
async def s8(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy A55\nIt will cost you: $420\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=a55, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's9')
async def s9(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy Tab S9 Ultra\nIt will cost you: $1420\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=tabultra, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 's10')
async def s10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Galaxy Tab S9+\nIt will cost you: $880\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=tabsplus, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


# --------------------------------------------------------------


@router.message(F.text == 'Iphone')
async def iphone(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='i1'),
         InlineKeyboardButton(text='2', callback_data='i2'),
         InlineKeyboardButton(text='3', callback_data='i3'),
         InlineKeyboardButton(text='4', callback_data='i4'),
         InlineKeyboardButton(text='5', callback_data='i5'), ],
        [InlineKeyboardButton(text='6', callback_data='i6'),
         InlineKeyboardButton(text='7', callback_data='i7'),
         InlineKeyboardButton(text='8', callback_data='i8'),
         InlineKeyboardButton(text='9', callback_data='i9'),
         InlineKeyboardButton(text='10', callback_data='i10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. Iphone 15 Pro Max\n2. Iphone 15 Pro\n3. Iphone 14 Pro Max\n4. Iphone 14 Pro\n5. Iphone 13 Pro Max\n6. Iphone 13 Pro\n7. Iphone 12 Pro Max\n8. Iphone 12 Pro\n9. Apple Ipad Pro\n10. Apple Ipad Air 5',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'i1')
async def i1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 15 Pro Max\nIt will cost you: $1500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=promax15, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i2')
async def i2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 15 Pro\nIt will cost you: $1500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pro15, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i3')
async def i3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 14 Pro Max\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=promax14, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i4')
async def i4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 14 Pro\nIt will cost you: $900\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pro14, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i5')
async def i5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 13 Pro Max\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=promax13, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i6')
async def i6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 13 Pro\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pro13, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i7')
async def i7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 12 Pro Max\nIt will cost you: $750\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=promax12, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i8')
async def s10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Iphone 12 Pro\nIt will cost you: $700\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pro12, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i9')
async def s10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Apple Ipad Pro\nIt will cost you: $100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=ipadpro, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'i10')
async def i10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Apple Ipad Air 5\nIt will cost you: $600\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=ipadair, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


# ---------------------------------------------------

@router.message(F.text == 'HP')
async def hp(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='h1'),
         InlineKeyboardButton(text='2', callback_data='h2'),
         InlineKeyboardButton(text='3', callback_data='h3'),
         InlineKeyboardButton(text='4', callback_data='h4'),
         InlineKeyboardButton(text='5', callback_data='h5'), ],
        [InlineKeyboardButton(text='6', callback_data='h6'),
         InlineKeyboardButton(text='7', callback_data='h7'),
         InlineKeyboardButton(text='8', callback_data='h8'),
         InlineKeyboardButton(text='9', callback_data='h9'),
         InlineKeyboardButton(text='10', callback_data='h10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. HP Elitebook 1030 Dragonfly\n2. HP Langwaki 15S\n3. HP ZBook Firefly 15\n4. HP Pavilion\n5. HP Pavilion Aero 13\n6. HP Pavilion 15\n7. HP ENVY\n8. HP Omen\n9. HP Spectre\n10. HP Victus',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'h1')
async def h1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Elitebook 1030 Dragonfly\nIt will cost you: $1900\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=elitebook, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h2')
async def h2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Langwaki 15S\nIt will cost you: $400\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=langwaki, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h3')
async def h3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP ZBook Firefly 15\nIt will cost you: $800\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=zbook, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h4')
async def h4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Pavilion\nIt will cost you: $450\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pavilion, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h5')
async def h5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Pavilion Aero 13\nIt will cost you: $800\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pavilion13, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h6')
async def h6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Pavilion 15\nIt will cost you: $520\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=pavilion15, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h7')
async def h7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP ENVY\nIt will cost you: $650\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=envy, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h8')
async def h8(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Omen\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=omen, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h9')
async def h9(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Spectre\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=spectre, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'h10')
async def h10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Victus\nIt will cost you: $800\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=victus, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


# -----------------------------------------------------------------------------


@router.message(F.text == 'Acer')
async def acer(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='a1'),
         InlineKeyboardButton(text='2', callback_data='a2'),
         InlineKeyboardButton(text='3', callback_data='a3'),
         InlineKeyboardButton(text='4', callback_data='a4'),
         InlineKeyboardButton(text='5', callback_data='a5'), ],
        [InlineKeyboardButton(text='6', callback_data='a6'),
         InlineKeyboardButton(text='7', callback_data='a7'),
         InlineKeyboardButton(text='8', callback_data='a8'),
         InlineKeyboardButton(text='9', callback_data='a9'),
         InlineKeyboardButton(text='10', callback_data='a10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. Acer Swift 14 AI\n2. Acer Swift X 14\n3. Acer Swift Go 16\n4. Acer Nitro 16 Intel\n5. Acer Nitro 14 AMD\n6. Acer Aspire Vero 16\n7. Acer Aspire 3 AMD\n8. Acer Predator HELIOS NEO 14\n9. Acer TravelMate P4 14 AMD\n10. Acer Book RS Porche',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'a1')
async def a1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Swift 14 AI\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=swift14ai, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a2')
async def a2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Swift X 14\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=swiftx14, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a3')
async def a3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Swift Go 16\nIt will cost you: $1200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=swiftgo16, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a4')
async def a4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Nitro 16 Intel\nIt will cost you: $1200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=nitro16intel, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a5')
async def a5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Nitro 14 AMD\nIt will cost you: $1300\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=nitro14amd, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a6')
async def a6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Aspire Vero 16\nIt will cost you: $850\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=aspirevero16, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a7')
async def a7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Aspire 3 AMD\nIt will cost you: $450\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=aspire3amd, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a8')
async def a8(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Predator HELIOS NEO 14\nIt will cost you: $1500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=predator, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a9')
async def a9(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer TravelMate P4 14 AMD\nIt will cost you: $1200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=travelmate, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'a10')
async def a10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Acer Book RS Porche\nIt will cost you: $2500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=porche, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


# -----------------------------------------------------------


@router.message(F.text == 'Asus')
async def asus(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='as1'),
         InlineKeyboardButton(text='2', callback_data='as2'),
         InlineKeyboardButton(text='3', callback_data='as3'),
         InlineKeyboardButton(text='4', callback_data='as4'),
         InlineKeyboardButton(text='5', callback_data='as5'), ],
        [InlineKeyboardButton(text='6', callback_data='as6'),
         InlineKeyboardButton(text='7', callback_data='as7'),
         InlineKeyboardButton(text='8', callback_data='as8'),
         InlineKeyboardButton(text='9', callback_data='as9'),
         InlineKeyboardButton(text='10', callback_data='as10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. Asus VivoBook pro 15\n2. Asus M5 15\n3. Asus ZenBook pro\n4. Asus ZenBook S\n5. Asus ExpertBook premium\n6. Asus ChromeBook Enterprise\n7. Asus ChromeBook Enterprise Flip\n8. ROG Zephyrus Gaming\n9. ROG Stix Gaming\n10. My Asus',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'as1')
async def as1(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus VivoBook pro 15\nIt will cost you: $1700\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=vivobook, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as2')
async def as2(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus M5 15\nIt will cost you: $270\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=m515, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as3')
async def as3(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ZenBook Pro\nIt will cost you: $1100\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=zenbookpro, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as4')
async def as4(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ZenBook S\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=zenbooks, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as5')
async def as5(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ExpertBook Premium\nIt will cost you: $700\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=expert, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as6')
async def as6(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ChromeBook Enterprise\nIt will cost you: $700\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=chromeenter, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as7')
async def as7(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ChromeBook Enterprise Flip\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=chromeflip, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as8')
async def as8(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus ROG Zephyrus Gaming\nIt will cost you: $1500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=rogzephyrus, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as9')
async def as9(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Asus Stix Gaming\nIt will cost you: $1500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=rogstix, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver it to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'as10')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: My Asus\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=myasus, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


# ----------------------------------------------------------------------------


@router.message(F.text == 'PC HP')
async def pchp(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='pc1'),
         InlineKeyboardButton(text='2', callback_data='pc2'),
         InlineKeyboardButton(text='3', callback_data='pc3'),
         InlineKeyboardButton(text='4', callback_data='pc4'),
         InlineKeyboardButton(text='5', callback_data='pc5'), ],
        [InlineKeyboardButton(text='6', callback_data='pc6'),
         InlineKeyboardButton(text='7', callback_data='pc7'),
         InlineKeyboardButton(text='8', callback_data='pc8'),
         InlineKeyboardButton(text='9', callback_data='pc9'),
         InlineKeyboardButton(text='10', callback_data='pc10'), ],
    ], resize_keyboard=True)
    await message.answer(
        'Choose model:\n1. HP Envy Desktop\n2. HP Slim Desktop\n3. Omen 45L Gaming Desktop\n4. Victus 15L Gaming Desktop\n5. HP Pavilion Desktop\n6. Omen 25L Desktop\n7. Omen 40L Desktop\n8. HP Elitetower 600\n9. Dual HP Monitor Dumble\n10. HP Series FHD Monitor',
        reply_markup=markup)


@router.callback_query(lambda c: c.data == 'pc1')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Envy Desktop\nIt will cost you: $500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=envydesktop, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc2')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Slim Desktop\nIt will cost you: $550\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=slimdesktop, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc3')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Omen 45L Gaming Desktop\nIt will cost you: $2000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=omen45l, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc4')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Victus 15L Gaming Desktop\nIt will cost you: $500\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=victus15l, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc5')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP Pavilion Desktop\nIt will cost you: $450\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=paviliondesktop, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc6')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Omen 25L Desktop\nIt will cost you: $1000\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=omen25l, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc7')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Omen 40L Desktop\nIt will cost you: $1700\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=omen40l, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc8')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HP EliteTower 600\nIt will cost you: $770\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=elitetower, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


@router.callback_query(lambda c: c.data == 'pc9')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: Dual HP Monitor Dmble\nIt will cost you: $190\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=dualhp, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)

        
@router.callback_query(lambda c: c.data == 'pc10')
async def as10(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_message(text='You chose: HHP Series FHD Monitor\nIt will cost you: $200\nThe photo:',
                           chat_id=call.from_user.id)
    await bot.send_photo(chat_id=call.from_user.id, photo=hpseries, reply_markup=keyboard.loccon)
    await bot.send_message(text='Share your location and phone number,so we can deliver i t to you!',
                           chat_id=call.from_user.id)


# @router.message(F.text == 'PC Acer')
# async def pcacer(message: Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='1', callback_data='pca1'),
#          InlineKeyboardButton(text='2', callback_data='pca2'),
#          InlineKeyboardButton(text='3', callback_data='pca3'),
#          InlineKeyboardButton(text='4', callback_data='pca4'),
#          InlineKeyboardButton(text='5', callback_data='pca5'), ],
#         [InlineKeyboardButton(text='6', callback_data='pca6'),
#          InlineKeyboardButton(text='7', callback_data='pca7'),
#          InlineKeyboardButton(text='8', callback_data='pca8'),
#          InlineKeyboardButton(text='9', callback_data='pca9'),
#          InlineKeyboardButton(text='10', callback_data='pca10'), ],
#     ], resize_keyboard=True)
#     await message.answer('1,2,3,4,5,6,7,8,9,10', reply_markup=markup)
#
#
# @router.message(F.text == 'PC Asus')
# async def pcasus(message: Message):
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='1', callback_data='pcas1'),
#          InlineKeyboardButton(text='2', callback_data='pcas2'),
#          InlineKeyboardButton(text='3', callback_data='pcas3'),
#          InlineKeyboardButton(text='4', callback_data='pcas4'),
#          InlineKeyboardButton(text='5', callback_data='pcas5'), ],
#         [InlineKeyboardButton(text='6', callback_data='pcas6'),
#          InlineKeyboardButton(text='7', callback_data='pcas7'),
#          InlineKeyboardButton(text='8', callback_data='pcas8'),
#          InlineKeyboardButton(text='9', callback_data='pcas9'),
#          InlineKeyboardButton(text='10', callback_data='pcas10'), ],
#     ], resize_keyboard=True)
#     await message.answer('1,2,3,4,5,6,7,8,9,10', reply_markup=markup)


@router.message(F.text == 'Back')
async def back(message: Message):
    await message.answer('Choose product:', reply_markup=keyboard.keyboard)


@router.message(F.text == 'Location')
async def location(message: Message):
    await message.answer('Thank you for choosing us\nYour product will be delivered in 3 days!')


@router.message(F.text == 'Contact')
async def contact(message: Message):
    await message.answer('Thank you for sharing your contact, our administration will call you in 5 minutes!')
