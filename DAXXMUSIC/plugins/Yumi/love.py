from pyrogram import Client, filters
import random
from DAXXMUSIC import app
from pyorogram.types import InputMediaPhoto
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


NIMI = [
    "https://telegra.ph/file/81918529691fc0f74f5c1.jpg",
    "https://telegra.ph/file/d4b9114c757c1106c7432.jpg",
    "https://telegra.ph/file/8486107891675afb52233.jpg",
    "https://telegra.ph/file/bb37b6698a7b87dab1d86.jpg",
    "https://telegra.ph/file/bb37b6698a7b87dab1d86.jpg",
    "https://graph.org/file/942223799764b95b6028a.jpg",
    "https://telegra.ph/file/592324136be542c2c9363.jpg",
    "https://graph.org/file/ecd6670f7c9bde85b7378.jpg",
    "https://telegra.ph/file/209d55403838bfd6498a5.jpg",
    "https://telegra.ph/file/63004f4d786ac26da3a99.jpg",
    "https://telegra.ph/file/f4791391e4e70e89a0640.jpg",
    "https://telegra.ph/file/e5deebed1ae6b627818a3.jpg",
    "https://telegra.ph/file/b66a6b8895f70f9643319.jpg",
    "https://telegra.ph/file/c7818276d9c25b175d60e.jpg",
    "https://telegra.ph/file/bf7707c8b3c2db8243948.jpg",
    "https://telegra.ph/file/72e95777972186c14d978.jpg",
    "https://graph.org/file/5c57cc6fff4ea7190e855.jpg",
    "https://graph.org/file/6c2d0467bcafb7752d112.jpg",
    "https://telegra.ph/file/7d52113479ecc4450817a.jpg",
]
        

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "❅ ʟᴏᴠᴇ ɪs ɪɴ ᴛʜᴇ ᴀɪʀ ʙᴜᴛ ɴᴇᴇᴅs ᴀ ʟɪᴛᴛʟᴇ sᴘᴀʀᴋ.",
            "❅ ᴀ ɢᴏᴏᴅ sᴛᴀʀᴛ ʙᴜᴛ ᴛʜᴇʀᴇ's ʀᴏᴏᴍ ᴛᴏ ɢʀᴏᴡ.",
            "❅ ɪᴛ's ᴊᴜsᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ sᴏᴍᴇᴛʜɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "❅ ᴀ sᴛʀᴏɴɢ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ɪs ᴛʜᴇʀᴇ. ᴋᴇᴇᴘ ɴᴜʀᴛᴜʀɪɴɢ ɪᴛ.",
            "❅ ʏᴏᴜ'ʜᴠ ɢᴏᴛ ᴀ ɢᴏᴏᴅ ᴄʜᴀɴᴄᴇ. ᴡᴏʀᴋ ᴏɴ ɪᴛ.",
            "❅ ʟᴏᴠᴇ ɪs ʙʟᴏssᴏᴍɪɴɢ, ᴋᴇᴇᴘ ɢᴏɪɴɢ."
        ])
    else:
        return random.choice([
            "❅ ᴡᴏᴡ ! ɪᴛ's ᴀ ᴍᴀᴛᴄʜ ᴍᴀᴅᴇ ɪɴ ʜᴇᴀᴠᴇɴ!",
            "❅ ᴘᴇʀғᴇᴄᴛ ᴍᴀᴛᴄʜ ! ᴄʜᴇʀɪsʜ ᴛʜɪs ʙᴏɴᴅ.",
            "❅ ᴅᴇsᴛɪɴᴇᴅ ᴛᴏ ʙᴇ ᴛᴏɢᴇᴛʜᴇʀ. ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!"
        ])

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("lov", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"❅ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟᴏᴠᴇ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ ⏤͟͟͞͞★ \n\n❅ {name1} ♥️ + {name2} ♥️ = {love_percentage}%\n\n{love_message}"
    else:
        response = "✦ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛᴡᴏ ɴᴀᴍᴇs ᴀғᴛᴇʀ /lov ᴄᴏᴍᴍᴀɴᴅ."
    app.send_photo(photo=random.choice(NIMI), response, reply_markup=InlineKeyboardMarkup(EVAA),)

