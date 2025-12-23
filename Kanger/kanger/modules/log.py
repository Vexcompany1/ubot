import asyncio
from pyrogram import Client, filters

from Kanger import *

async def is_botlog_(f, client, message):
    user_id = client.me.id
    debotlog = await status_botlog(user_id)
    if debotlog:
        return bool(True)
    else:
        return bool(False)

is_botlog = filters.create(func=is_botlog_, name="is_botlog_")

async def pm_log(client, message):
    user_id = client.me.id
    botlog_chat_id = await get_botlog(user_id)
    user = message.from_user.id
    biji = message.from_user.first_name
    sempak = message.text
    await client.send_message(
        botlog_chat_id,
        f"<b><u>Logs Chat</u></b>\n<b>From:</b> {biji}\n<b>Message:</b> <code>{sempak}</code>\n "
    )

async def log_tagged_messages(client, message):
    message.chat.id
    user_id = client.me.id
    botlog_chat_id = await get_botlog(user_id)
    knl = f"<b><u>Logs Tag</u></b>\n<b>From: </b>{message.from_user.mention}"
    knl += f"\n<b>Group: </b>{message.chat.title}"
    knl += f"\n<a href = '{message.link}'>Check Message</a>"
    knl += f"\n<b>Message: </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        botlog_chat_id,
        knl,
        disable_web_page_preview=True,
    )

async def set_log(client, message):
    botlog_chat_id = message.chat.id
    user_id = client.me.id
    chat = await client.get_chat(botlog_chat_id)
    if chat.type == "private":
        return await message.reply("Logs not valid.")
    await set_botlog(user_id, botlog_chat_id)
    await message.reply("Logs updated!")
    
async def delete_log(client, message):
    user_id = client.me.id
    try:
        await delete_botlog(user_id)
    except:
        return await message.reply("Logs is not set before!")
    await message.reply("Log has purged!")
    
async def mulai_log(client, message):
    user_id = client.me.id
    await start_botlog(user_id)
    await message.reply(
        "<b>Logger has been started!</b>",
        quote=True
        )

async def berhenti_log(client, message):
    user_id = client.me.id
    await stop_botlog(user_id)
    await message.reply(
        "<b>Logger has been stopped!</b>",
        quote=True
        )