

import secureme
from pyrogram import filters
from DAXXMUSIC import app


@app.on_message(filters.command("encrypt"))
async def encyrpt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**❍ ᴇxᴀᴍᴘʟᴇ ➛ /encyrpt ɪɴᴅɪᴀ")
    m = message.text.split(' ',1)[1]
    try:
        Secure = secureme.encrypt(m)
        
        await message.reply_text(f"{Secure}")
        

    except Exception as e:
        await message.reply_text(f"Error {e}")

@app.on_message(filters.command("decrypt"))
async def decrypt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**❍ ᴇxᴀᴍᴘʟᴇ ➛ /decrypt ɴsɪɴғ")
    m = message.text.split(' ',1)[1]
    try:
        Decrypt = secureme.decrypt(m)
        
        await message.reply_text(f"{Decrypt}")
        

    except Exception as e:
        await message.reply_text(f"{e}")
