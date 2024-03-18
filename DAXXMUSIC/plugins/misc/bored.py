from pyrogram import Client, filters
import requests
from DAXXMUSIC import app

# URL for the Bored API
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


# Function to handle /bored command
@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            # Send the activity to the user who triggered the command
            await message.reply(f"✦ 𝗙𝗘𝗘𝗟𝗜𝗡𝗚𝗦 𝗕𝗢𝗥𝗘𝗗 ⁉️ 𝗛𝗢𝗪 𝗔𝗕𝗢𝗨𝗧 ⏤͟͟͞͞★\n\n\n {activity} \n\n\n✦ 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 ➠ [๛ɴ ʏ ᴋ ᴀ ᴀ ♡゙](htps://t.me/Nykaaxbot)")
        else:
            await message.reply("✦ ɴᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("✦ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")
