#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os
from pythonping import ping
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
from random import randint, choice
from requests import get
from io import BytesIO

nex_id=986023905
drax_id=994434215
crab_id=5101138428
just_id=831781432

a = ["Разраб", "Админ", "DEVELOPER",]

def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
        )
    else:
        if hint:
            hint_text = f"\n\n<b>Hint: {hint}</b>"
        else:
            hint_text = ""
        return (
            f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
        )


def with_reply(func):
    async def wrapped(client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped


okda = ping('8.8.8.8', size=40, count=10)
print("PING:" + str(okda.rtt_avg_ms))
m = '''
████████
██
██
██████
██
██
██'''

h = "╔┓┏╦━━╦┓╔┓╔━━╗ ║┗┛║┗━╣┃║┃║╯╰║ ║┏┓║┏━╣┗╣┗╣╰╯║ ╚┛┗╩━━╩━╩━╩━━╝"



fuckk = '''
╱▔▔▔╲┈┈┈┈┈╱▔▔▔╲
▏╰┈╮┈╲╲┈╱╱┈╭┈╯▕
╲╮┈╰┈╮╲▉╱╭┈╯┈╭╱
▕╰┈╮┈╰╮▉╭╯┈╭┈╯▏
┈╲▂╰┈┈╱▉╲┈┈╯▂╱
┈┈╱▔▔▔╭▊╮▔▔▔╲
┈┈▏╭┈┈╯▊╰┈┈╮▕
┈▕╭╯┈┈╱▋╲┈┈╰╮▏
┈┈╲▂▂╱┈┈┈╲▂▂╱
'''

d = ''' 
████╗███╗█╗█╗
█╔══╝█╔█║█║█║
████╗███║███║
█╔═█║█╔█║█╔█║
████║█║█║█║█║
╚═══╝╚╝╚╝╚╝╚╝'''


app = Client('StarZed', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')

app.start()

app.stop()
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print('''   v1.0
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃       Made by StarZed          ┃
      ┃  Telegram: @starzedscripts ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

''')
print("После ввода задержки напишите в любой телеграм чат команду /help для просмотра команд!")
print("\n МЫ НЕ НЕСЕМ ОТВЕТСВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

global number
number = 0

while cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool == 1:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool == 2:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))

while cool < 0:
    print("ОЧЕНЬ БЫСТРО........")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))


@app.on_message(filters.command("bombs", prefixes = ".") & filters.me)
async def bombs(app, message):
    global number
    number = number + 1
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("<b>@starzedscripts</b>")


@app.on_message(filters.command("snow", prefixes=".") & filters.me)
async def betaloves(_, msg):
    global number
    number = number + 1
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️





⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    





⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️




⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️



⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️


⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit(f'''☁️☁️☁️☁️☁️☁️☁️☁️
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️    
❄️     ❄️    ❄️     ❄️    ❄️
    ❄️     ❄️    ❄️     ❄️
❄️     ❄️    ❄️     ❄️    ❄️    
    ❄️     ❄️    ❄️     ❄️

⛄️⛄️⛄️⛄️⛄️⛄️⛄️⛄️

''')  
    await asyncio.sleep(2)
    await msg.edit("<b>⭐️ @starzedscripts</b>")



@app.on_message(filters.command("hello", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    global number
    number = number + 1
    current = ""
    for chunk in list(h):
        current += chunk
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.25)
    await asyncio.sleep(2)
    await msg.edit("<b>⭐️ @starzedscripts</b>")


@app.on_message(filters.command("F", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    global number
    number = number + 1
    current = ""
    for chunk in list(m):
        current += chunk
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.25)
    await asyncio.sleep(2)
    await msg.edit("<b>⭐️ @starzedscripts</b>")

@app.on_message(filters.command("ban", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    global number
    number = number + 1
    current = ""
    for chunk in list(d):
        current += chunk
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.15)
    await asyncio.sleep(2)
    await msg.edit("<b>⭐️ @starzedscripts</b>")

@app.on_message(filters.command("bf", prefixes=".") & filters.me)
async def betaloves(_ ,msg):
    global number
    number = number + 1
    current = ""
    for chunk in list(fuckk):
        current += chunk
        if not chunk.strip():
            continue
        await msg.edit(current)
        await asyncio.sleep(.10)
    await asyncio.sleep(2)
    await msg.edit("<b>⭐️ @starzedscripts</b>")

@app.on_message(filters.command("timer", prefixes=".") & filters.me)
async def timer(_,msg):
    global number
    number = number + 1
    score = int(msg.text.split()[1])
    while score > 0:
        score -=1
        await msg.edit(f'''<b>{score}</b>''')
        await sleep(1)
    await msg.edit("<b>⭐️ @starzedscripts</b>")
        

        
@app.on_message(filters.command("amogus", prefixes=".") & filters.me)
async def amogus(app, message):
    global number
    number = number + 1
    clrs = {'red': 1, 'lime': 2, 'green': 3, 'blue': 4, 'cyan': 5, 'brown': 6, 'purple': 7, 'pink': 8, 'orange': 9, 'yellow': 10, 'white': 11, 'black': 12}
    clr = randint(1,12)
    text = " ".join(message.command[1:])

    await message.edit("<b>amgus, tun tun tun tun tun tun tun tudududn tun tun...</b>")
    url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
    font = ImageFont.truetype(BytesIO(get(url+"bold.ttf").content), 60)
    imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
    w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=2)
    text = Image.new("RGBA", (w+30, h+30))
    ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
    w = imposter.width + text.width + 10
    h = max(imposter.height, text.height)
    image = Image.new("RGBA", (w, h))
    image.paste(imposter, (0, h-imposter.height), imposter)
    image.paste(text, (w-text.width, 0), text)
    image.thumbnail((512, 512))
    output = BytesIO()
    output.name = "imposter.webp"
    image.save(output)
    output.seek(0)
    await message.delete()
    await app.send_sticker(message.chat.id, output)

def format_exc(e: Exception, hint: str = None):
    traceback.print_exc()
    if isinstance(e, errors.RPCError):
        return (
            f"<b>Telegram API error!</b>\n"
            f"<code>[{e.CODE} {e.ID or e.NAME}] - {e.MESSAGE}</code>"
        )
    else:
        if hint:
            hint_text = f"\n\n<b>Hint: {hint}</b>"
        else:
            hint_text = ""
        return (
            f"<b>Error!</b>\n" f"<code>{e.__class__.__name__}: {e}</code>" + hint_text
        )


def with_reply(func):
    async def wrapped(client, message: types.Message):
        if not message.reply_to_message:
            await message.edit("<b>Reply to message is required</b>")
        else:
            return await func(client, message)

    return wrapped




            



@app.on_message(filters.command("gifspam", prefixes=".") & filters.me)
def sendgif(app, message):
    global number
    number = number + 1
    for _ in range(int(message.command[1])):
        sleep(0.01)
        app.send_document(message.chat.id, "https://tenor.com/view/spam-toon-toonio-%D1%82%D1%83%D0%BD%D0%B8%D0%BE-pomidorkin-gif-24712213")

@app.on_message(filters.command("dead", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.dead ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                msg.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 💚')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')

textded = '''
<b> Я дед инсайд </b>
<b> Мне 9 лет </b>
<b> И я хочу в Психокидс </b>
'''


@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def valentine(client, message):
    text = f"<b>💊 Поиск запрещённых препаратов.. </b>"
    await message.edit(str(text))
    await asyncio.sleep(2)
    kilogramm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    text2 = f"<b>🚬 Найдено {random.choice(kilogramm)} кг шпекса</b>"
    await message.edit(str(text2))
    await asyncio.sleep(3)
    text3 = f"<b>🌿⚗️ Оформляем вкид</b>"
    await message.edit(str(text3))
    await asyncio.sleep(5)
    drugsss = [f'<b>😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты</b>',
               f'<b>🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид</b>',
               f'<b>😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз</b>',
               f'<b>😌 Вы оформили вкид, Вам понравилось</b>']
    drug = random.choice(drugsss)
    await message.edit(drug)
    await asyncio.sleep(5)
    await message.edit("⭐ @starzedscripts ")

@app.on_message(filters.command("mum", prefixes=".") & filters.me)
async def mum(client, message):
    mamka = [f'<b>❌ Мамаша не найдена</b>',f'<b> ✅ МАМАША НАЙДЕНА</b>' ]
    text = "<b>🔍 Поиск твоей мамки начался...</b>"
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    text2 = "<b>🔍 Ищем твою мамашу на Авито... </b>"
    await message.edit(str(text2))
    await asyncio.sleep(1)
    text3 = random.choice(mamka)
    await message.edit(str(text3))
    await asyncio.sleep(3.0)
    text4 = "<b>🔍 Поиск твоей мамаши на свалке... </b>"
    await message.edit(str(text4))
    await asyncio.sleep(3.0)
    text5 = random.choice(mamka)
    await message.edit(str(text5))
    await asyncio.sleep(5.0)
    text6 = "⭐ @starzedscripts "
    await message.edit(str(text6))

@app.on_message(filters.command("xuy", prefixes=".") & filters.me)
async def valentine(app, message):
    await message.edit(f'''<b>🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆</b>''')


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def valentine(_, msg):
    global number
    number = number + 1
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "█"
    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)






textded1 = '''
<b>спокойной ночи зайка 💚</b>
<b>спокойной ночи солнышко 💛</b>
<b>спокойной ночи котёнок ❤</b>️
<b>спокойной ночи цветочек 💙</b>
<b>спокойной ночи ангелочек 💜</b>
<b>спокойной ночи принцесса 💓</b>
<b>спокойной ночи красотка 💕</b>
<b>спокойной ночи милашка 💖</b>
<b>спокойной ночи симпатяжка 💗</b>
<b>спокойной ночи бусинка 💘</b>
<b>❤я❤</b>️
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''


@app.on_message(filters.command("compli", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = comp.split("\n")
    e = True
    etime = int(msg.text.split('.compli ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')


@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.night ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
    random_number = str(random.randint(0, int(msg.command[1])))
    msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'
    
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
    global number
    number = number + 1
    app.send_message(message.chat.id,f'<b>Ты гуль?</b>')
    sleep(2)
    app.send_message(message.chat.id,f'<i>Я тоже</i>')
    sleep(5)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)

    if(end_message != ''):
        app.send_message(message.chat.id, end_message)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, message):
    spams = " ".join(message.command[2:])
    global number
    number = number + 1
    for _ in range(int(message.command[1])):
        sleep(0.01)
        app.send_message(message.chat.id, spams)

@app.on_message(filters.command("spamstick", prefixes=".") & filters.me)
def spam(app, message):
    number = number + 1
    for _ in range(int(message.command[1])):
        sleep(0.01)
        app.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEEDZiI8ZlrkTWVAVlsaJ1yfd63euS2AACMgwAAgqBoEs52ePcv8NaIiME")

@app.on_message(filters.command("help", prefixes="/") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''
📙<b> Команды:</b> \n<b> - https://telegra.ph/Aktualnye-komandy-02-26</b> \n

💎 <b>Приобрести PREMIUM анимацию: </b>\n <b>- https://telegra.ph/Priobresti-Vip-status-03-02</b> \n                             

''', disable_web_page_preview=True)




@app.on_message(filters.command("profile", prefixes="/") & filters.me)
def help(app, message): 
    if message.from_user.id in {nex_id, just_id, crab_id, drax_id}:
        app.send_message(message.chat.id, f'''
💾<b> Профиль:
</b> <b> Пользователь:</b><code> {message.from_user.first_name}</code>
<i><b> PREMIUM </b>- {random.choice(a)}</i>
<b> Chat_ID: </b><code> {message.chat.id}</code>
<b> User_ID: </b><code> {message.from_user.id}</code>
<b>Ping:</b> 📶 <code>{str(okda.rtt_avg_ms)}Ms</code>
<b>Анимаций по старту:</b> <code>{number}</code>\n </b>''')
    else:
        app.send_message(message.chat.id,f'''
💾<b> Профиль:
</b> <b> Пользователь:</b><code> {message.from_user.first_name}</code>
<i><b> PREMIUM </b>- Отсутсвует</i>
<b> Chat_ID: </b><code> {message.chat.id}</code>
<b> User_ID: </b><code> {message.from_user.id}</code>
<b>Ping:</b> 📶 <code>{str(okda.rtt_avg_ms)}Ms</code>
<b> Анимаций по старту:</b> <code>{number}</code>\n </b>''')



@app.on_message(filters.command("maslo", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>я</b>")  # red
        sleep(time)
        msg.edit(f"<b>я люблю</b>")  # orange
        sleep(time)
        msg.edit(f"<b>я люблю когда</b>")  # orange
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые</b>")  # red
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики</b>")  # orange
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  # red
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  # orange
        sleep(5)
        global number
        number = number + 1
        msg.edit(f'<b> @starzedscripts </b>')
        msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("football", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")  # red
        sleep(2)
        msg.edit(f"<b>⏳ Подготовка к игре.</b>")  # orange
        sleep(2)
        msg.edit(f"<b>⌛ Подготовка к игре..</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⏳ Подготовка к игре...</b>")  # red
        sleep(time)
        msg.edit(f"<b>⚽ Удар.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⚽ Удар..</b>")  # red
        sleep(time)
        msg.edit(f"<b>⚽ Удар...</b>")  # orange
        sleep(time)
        msg.edit(random.choice(foot))
        sleep(5)
        global number
        number = number + 1
        msg.edit(f'<b> @starzedscripts </b>')
        msg.edit(f'<b>⭐ @starzedscripts </b>')

foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]

@app.on_message(filters.command("kill", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
        sleep(3)
        msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
        sleep(2)
        msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
        sleep(time)
        msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
        sleep(time)
        msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
        sleep(time)
        msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Поиск.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Поиск..</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Поиск...</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Поиск.</b>")  # orange
        sleep(time)
        msg.edit(f"<b>👀 Поиск..</b>")
        sleep(time)
        msg.edit(f"<b>👀 Поиск...</b>")
        sleep(time)
        msg.edit(random.choice(kill))
        sleep(5)
        global number
        number = number + 1
        msg.edit(f'<b> @starzedscripts </b>')
        msg.edit(f'<b>⭐ @starzedscripts </b>')

kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]



@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = jopa.split("\n")
    e = True
    etime = int(msg.text.split('.jopa ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("love", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = love.split("\n")
    e = True
    etime = int(msg.text.split('.love', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("zxc", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = zxc.split("\n")
    e = True
    etime = int(msg.text.split('.zxc', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts</b>')

@app.on_message(filters.command("ziga", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = ziga.split("\n\n")
    e = True
    etime = int(msg.text.split('.ziga', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
                msg.edit(f'{i}')
                sleep(time)
            except:
                pass
    global number
    number = number + 1
    msg.edit(f'<b> @starzedscripts </b>')
    msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("like", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''      
🟦''')  # red
        sleep(0.001)
        msg.edit(f'''
🟦🟦''')  # red
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(5)
        global number
        number = number + 1
        msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
🟥''')  # red
        sleep(0.001)
        msg.edit(f'''
🟥🟥''')  # red
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(1)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(4)
        global number
        number = number + 1
        msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("loves", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')  # red
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨❤️❤️✨✨
✨✨✨✨✨✨''')  # red
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️✨✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨
✨❤️❤️❤️❤️✨
✨❤️✨✨❤️✨
✨❤️❤️❤️❤️✨
✨✨✨❤️❤️✨
✨✨❤️✨❤️✨
✨❤️✨✨❤️✨
✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨❤️❤️✨❤️❤️✨✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️✨
✨✨❤️❤️❤️❤️❤️✨✨
✨✨✨❤️❤️❤️✨✨✨
✨✨✨✨❤️✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💚💚✨💚💚✨✨
✨💚💚💚💚💚💚💚✨
✨💚💚💚💚💚💚💚✨
✨✨💚💚💚💚💚✨✨
✨✨✨💚💚💚✨✨✨
✨✨✨✨💚✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💙💙✨💙💙✨✨
✨💙💙💙💙💙💙💙✨
✨💙💙💙💙💙💙💙✨
✨✨💙💙💙💙💙✨✨
✨✨✨💙💙💙✨✨✨
✨✨✨✨💙✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💜💜✨💜💜✨✨
✨💜💜💜💜💜💜💜✨
✨💜💜💜💜💜💜💜✨
✨✨💜💜💜💜💜✨✨
✨✨✨💜💜💜✨✨✨
✨✨✨✨💜✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🤍🤍✨🤍🤍✨✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨🤍🤍🤍🤍🤍🤍🤍✨
✨✨🤍🤍🤍🤍🤍✨✨
✨✨✨🤍🤍🤍✨✨✨
✨✨✨✨🤍✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🖤🖤✨🖤🖤✨✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨🖤🖤🖤🖤🖤🖤🖤✨
✨✨🖤🖤🖤🖤🖤✨✨
✨✨✨🖤🖤🖤✨✨✨
✨✨✨✨🖤✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨💛💛✨💛💛✨✨
✨💛💛💛💛💛💛💛✨
✨💛💛💛💛💛💛💛✨
✨✨💛💛💛💛💛✨✨
✨✨✨💛💛💛✨✨✨
✨✨✨✨💛✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(time)
        msg.edit(f'''
✨✨✨✨✨✨✨✨✨
✨✨🧡🧡✨🧡🧡✨✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨🧡🧡🧡🧡🧡🧡🧡✨
✨✨🧡🧡🧡🧡🧡✨✨
✨✨✨🧡🧡🧡✨✨✨
✨✨✨✨🧡✨✨✨✨
✨✨✨✨✨✨✨✨✨''')
        sleep(3)
        global number
        number = number + 1
        msg.edit(f'<b>⭐ @starzedscripts </b>')

@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # red
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # orange
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # yellow
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # green
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # blue
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # purple
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  # black
        sleep(1)
        global number
        number = number + 1
        msg.edit(f'<b> @starzedscripts </b>')
        msg.edit(f'<b>⭐ @starzedscripts </b>')


@app.on_message(filters.command("toxic", prefixes=".") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гнидопаскудная хуемандовина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>хуй тебе в глотку через анальный проход</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гандон с гонореей...</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>сортирующего яйца в пизде кастрированной кобылы</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебун хуеголовый, пидрасня ебаная. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Залупоголовая блядоящерица. .</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядская промудохуина! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебаквакнутый распиздаеб... </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Промудохуепиздамразоблядское злоепиздие </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямудевшая хуеблядина четырестохуйная</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>вестипёздная мразотоблядская шлюхасосалка. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>блядь шмара козельуебок сдохни </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
     ''')
    sleep(0.5)
    global number
    number = number + 1
    app.send_message(message.chat.id, f'''
     <b>⭐️ @starzedscripts</b>
     ''')

jopa = '''
           <b>ВЗЛОМ ЖОПЫ</b> 
           <b><i>Loading...</i></b> 
    10%  █▒▒▒▒▒▒▒▒▒▒▒▒
    30%  ███▒▒▒▒▒▒▒▒▒▒    
    50%  █████▒▒▒▒▒▒▒▒
    66%  ██████▒▒▒▒▒▒▒
    79%  ████████▒▒▒▒▒
    84%  █████████▒▒▒▒
    89%  ██████████▒▒▒
    95%  ████████████▒
    99%  █████████████
    100% █████████████
    <b> ВАША ЖОПА ВЗЛОМАНА </b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
    <b><i>Создатель: "Прощайте"</i></b>
'''
zxc = '''
<b>- All my friends are toxic, all ambitionless 💚</b>

<b>- All my friends are toxic, all ambitionless 💜</b>

<b>- All my friends are toxic, all ambitionless 💛</b>

<b>- So rude and always negative 🤍</b>

<b>- So rude and always negative 💚</b>

<b>- So rude and always negative 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💔</b>

<b>- I need new friends, but it's not  that quick and easy 💛</b>

<b>- I need new friends, but it's not  that quick and easy 💚</b>

<b>- Oh, I'm drowning, let me breathe 💜</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

<b>- Oh, I'm drowning, let me breathe 💛</b>

'''


love = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
<b>Загрузка любви...</b>
❤️🤍🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️🤍🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️🤍🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️🤍🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️🤍🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️🤍🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️🤍🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️🤍🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️🤍
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>
<b>Я люблю тебя ❤️‍🔥</b>

'''

comp = '''
<b>Крошечные напоминания того, что ты...</b> 

<b>Самая удивительная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая красивая</b> ✨

<b>Самая успешная</b> ✨

<b>Самая заботливая</b> ✨

<b>Самая милая</b> ✨

<b>Самая прекрасная</b> ✨

<b>Самая умная</b> ✨

<b>Самая шикарная</b> ✨

<b>Самая обалденная ✨</b>

<b>Самая очаровашка</b> ✨

<b>Самая любимая</b> ✨

<b>Самая весёлая</b> ✨

<b>Самая нежная</b> ✨

<b>Самая яркая</b> ✨

<b>Самая прелестная</b> ✨

<b>Самая приятная</b> ✨

<b>Самая сладкая</b> ✨

<b>Самая дивная</b> ✨

<b>Самая ангельская</b> ✨

<b>Самая добрая</b> ✨

<b>Самая бесподобная</b> ✨

<b>Самая волшебная</b> ✨

<b>Самая лучшая</b> ✨

<b>Самая крутышка</b> ✨

<b>Самая аромтная</b> ✨

<b>Самая единственная</b> ✨

<b>Самая искренняя</b> ✨

<b>Самая ласковая</b> ✨

<b>Самая романтичная</b> ✨

<b>Самая великолепная</b> ✨

<b>Самая внимательная</b> ✨

<b>Самая страстная</b> ✨

<b>Самая игривая</b> ✨

<b>Самая стройная</b> ✨

<b>Самая безумная</b> ✨

<b>Самая симпатичная</b> ✨

<b>Самая изящная </b> ✨

<b>Самая талантливая ✨</b>

<b>Самая элегантная ✨</b>

<b>Самая чуткая ✨</b>

<b>Самая отзывчивая ✨</b>

<b>Самая уникальная ✨</b>

<b>Самая смелая ✨</b>

<b>Самая уверенная ✨</b>

<b>Самая особенная ✨</b>

<b>Самая изумительная ✨</b>

<b>Самая настоящая ✨</b>

<b>Самая обаятельная ✨</b>

<b>Самая пушистая ✨</b>

<b>Самая кокетливая ✨</b>

<b>Самая теплая ✨</b>

<b>Самая энергичная ✨</b>

<b>Самая неотразимая ✨</b>

<b>Самая неописуемая ✨</b>

<b>Самая грациозная ✨</b>

<b>Самая сказочная ✨</b>

<b>Самая желанная ✨</b>

<b>Самая изысканная ✨</b>

<b>Самая мечтательная ✨</b>

<b>Самая безупречная ✨</b>

<b>Самая совершеная ✨</b>

<b>Самая честная ✨</b>

<b>Самая улыбчивая ✨</b>

<b>Самая ненаглядная ✨</b>

<b>Самая женственная ✨</b>

<b>Самая цветущая ✨</b>

<b>Самая гармоничная ✨</b>

<b>Самая отрадная ✨</b>
'''

ziga = '''
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🧡🧡🧡🧡🤍🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🤍🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🤍🤍🧡🤍🤍🤍🤍
🤍🧡🤍🤍🧡🤍🤍🧡🤍
🤍🧡🧡🤍🧡🧡🧡🧡🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💛💛💛💛🤍💛💛🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍🤍🤍🤍💛🤍🤍💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛🤍🤍💛🤍🤍🤍🤍
🤍💛🤍🤍💛🤍🤍💛🤍
🤍💛💛🤍💛💛💛💛🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💚💚💚💚🤍💚💚🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍🤍🤍🤍💚🤍🤍💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚🤍🤍💚🤍🤍🤍🤍
🤍💚🤍🤍💚🤍🤍💚🤍
🤍💚💚🤍💚💚💚💚🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💙💙💙💙🤍💙💙🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍🤍🤍🤍💙🤍🤍💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙🤍🤍💙🤍🤍🤍🤍
🤍💙🤍🤍💙🤍🤍💙🤍
🤍💙💙🤍💙💙💙💙🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍💜💜💜💜🤍💜💜🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍🤍🤍🤍💜🤍🤍💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜🤍🤍💜🤍🤍🤍🤍
🤍💜🤍🤍💜🤍🤍💜🤍
🤍💜💜🤍💜💜💜💜🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍❤️❤️❤️❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍

🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
'''




end_message = '<b> ⭐ @starzedscripts </b>'
app.run()
