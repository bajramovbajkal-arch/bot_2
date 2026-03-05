import asyncio
from aiogram import Bot, Dispatcher
from aiogram. filters import CommandStart, Command
from aiogram . types import Message, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

import os
from dotenv import load_dotenv
load_dotenv()


token = os.getenv("token")

bot = Bot(token=token)
dp = Dispatcher()

mm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='botlar'),
        KeyboardButton(text='kanallar'),
        KeyboardButton(text='accawint') ]

    ],
    resize_keyboard=True
)
vv = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='adminge zvandaw'),KeyboardButton(text='chatqa jaziw'),KeyboardButton(text='artqa qaytiw')]
    ],
    resize_keyboard=True
)
chat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='admin',url='https://t.me/ssaburov1')]
    ]
)




jj = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-kanal', url='https://t.me/python_jobs'),
            InlineKeyboardButton(text='2-kanal', url='https://t.me/job_python'),
            InlineKeyboardButton(text='3-kanal', url='https://t.me/jumis1_nokis')
        ]
    ]
)
uu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-bot', url='https://t.me/mymanga_bot'),
            InlineKeyboardButton(text='2-bot', url='https://t.me/mangasubscriptionbot'),
            InlineKeyboardButton(text='3-bot', url='https://t.me/MangaManhwa_bot')
        ]
    ]
)
mp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1-accawint', url='https://t.me/ssaburov1'),
            InlineKeyboardButton(text='2-accawint', url='https://t.me/xajik17'),
            InlineKeyboardButton(text='3-accawint', url='https://t.me/muxash1')
        ]
    ]
)



@dp.message (CommandStart())
async def s(a:Message):
    await a.answer(f"salem {a.from_user.first_name}",reply_markup=mm)

@dp.message(Command('help'))
async def jardem(a:Message):
    await a.answer(f"qanday jardem kerek",reply_markup=vv)

@dp.message()
async def test(message: Message):
    text = message.text



    @dp.message()
    async def test(message: Message):
        # Admin ko'rishi uchun
        await bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

    if text == 'baylanis':
        await message.answer('adminge zvandaw', reply_markup=vv)

    elif text == 'adminge zvandaw':
        await message.answer('admin nomeri:' '+998 93-461-82-89')

    elif text == 'artqa qaytiw':
        await message.answer('siz artqa qayttiniz', reply_markup=mm)

    elif text == 'chatqa jaziw':
        await message.answer('admin chati',reply_markup=chat_menu)

    elif text == 'botlar':
        await message.answer('bizdin botlar', reply_markup=uu)

    elif text == 'kanallar':
        await message.answer('bizdin kanallar', reply_markup=jj)

    elif text == 'accawint':
        await message.answer('bizdin accawintlar', reply_markup=mp)

    else:
        await message.answer('onday essat joq')





async def main ():
    print('isledi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())