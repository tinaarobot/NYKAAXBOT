

import requests

from DAXXMUSIC import app
from pyrogram import filters


@app.on_message(filters.command("loveshayri"))

async def love_shayri(b,m):
    "dont remove this line \n credit  |n github : noob-mukesh"
    love = requests.get("https://mukesh-api.vercel.app/loveshayri").json()["results"]    
    await m.reply_text(love)
          
@app.on_message(filters.command("hateshayri"))
async def hate_shayri(b,m):
    "dont remove this line \n credit  |n github : noob-mukesh"
    hate= requests.get("https://mukesh-api.vercel.app/hateshayri").json()["results"]    
    await m.reply_text(hate)          
mod_name="sʜᴀʏʀɪ"
