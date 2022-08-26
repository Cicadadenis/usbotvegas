from telethon import TelegramClient, events, utils

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
import io
import secrets
from PIL import Image,  ImageDraw, ImageFont
import secrets
from aiogram import types, Bot, Dispatcher
from aiogram import executor
from aiogram.dispatcher import FSMContext
from telethon.extensions import markdown
from telethon.tl.types import MessageEntityBold, MessageEntityItalic, MessageEntityTextUrl
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
import random, time
from aiogram.dispatcher.filters import ChatTypeFilter
from datetime import datetime, timedelta
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from telethon import Button
import webbrowser
import sqlite3
api_id = 1325339
api_hash = "b826075fd7ea762e6b9f853146d47995"
client = TelegramClient('anon', api_id, api_hash)

con = sqlite3.connect('cicada.db')
cur = con.cursor()
tt = datetime.now()

try:
    cur.execute('''CREATE TABLE cicada
               (name text, us_id text, tt text)''')


    con.commit()
    print('\n\n\n\n     Создание БД')
except:
    print('\n\n     Старт Бота')
    pass

def add_us(name, us_id, tt):
    cur.execute(
            f"""INSERT INTO cicada VALUES('{name}', '{us_id}', '{tt}')""")
    con.commit()  

def whe_us(us_id):
    
    cur.execute(
            f"""SELECT us_id FROM cicada WHERE '{us_id}' """)
    try:
        rows = cur.fetchall()[0][0]
        return True
    
    except:
        return False
class cicada(StatesGroup):
    sms = State()
    size = State()


ps = []
@client.on(events.NewMessage())
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    try:
       if whe_us(us_id=us_id) == False:
            if len(ff) == 7:
                if ff == ps[0]:
                    add_us(name=name, us_id=us_id, tt=tt)
                else:
                    await client.send_message(entity=us_id, message="<b>Неверный Пароль !!!</b>", parse_mode="HTML")
    except:pass
    password = secrets.token_urlsafe(5)
    ps.clear()
    ps.append(password)
    if whe_us(us_id=us_id) == False:
        font = ImageFont.truetype("Carnivale.ttf", int(40))
        W, H = (300,200)
        msg = password
        im = Image.new("RGBA",(W,H),"yellow")
        draw = ImageDraw.Draw(im)
        w, h = draw.textsize(msg)
        draw.text(((W-w)/3,(H-h)/3), msg, font=font,fill="black", align ="left")
        im.save("hello.png", "PNG")
        cap = "Введите код с картинки 👆\n➖➖➖➖➖➖➖➖➖\nЧтобы вернуться в меню и начать<\nOтправьте 👉 /start"
        with io.open("hello.png", 'rb') as file:
            await client.send_file(entity=us_id, file=file, caption=cap)
    if whe_us(us_id=us_id) == True:

        result = (f"        <b>🔱🔱🔱    Привет      {name}     🔱🔱🔱\n\n"
                  f"        <b>💥   Вас Приветствует VEGAS  💥</b>\n"
                  f"        <b>‼️    Вот  Наши  Контакты     ‼️</b>\n"
                  f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
                  f"        <a href='http://t.me/VEGAS_24_Prod'><b>👉 Оператор продаж</b></a>\n"
                  f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
                  f"        <a href='http://t.me/GAF01_bot'><b>👉 Бот авто прода</b></a>\n"
                  f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                  f"        <a href='http://t.me/vegas_teh'><b>👉 Техподдержка</b></a>\n"
                  f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                  f"        <a href='http://vegaswork.cc'><b>👉 Наша визитка</b></a>\n"
                  f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
                  f"        <a href='http://omwork.cc'><b>👉 Сайт работы</b></a>\n")
        veg = open("vegas.jpg", 'rb').read()
        await client.send_file(entity=us_id, file=veg, caption=f"<b>{result}</b>", parse_mode="HTML")

client.start()
client.run_until_disconnected()