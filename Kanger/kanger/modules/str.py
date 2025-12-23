import asyncio
from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Kanger import *


async def menjawir(client, message):
    try:
        await message.react(emoji="🗿")
    except:
        return


async def send_msg_to_owner(client, message):
    if message.from_user.id == OWNER_ID:
        return
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "Profile", callback_data=f"profil {message.from_user.id}"
                ),
        ]
        ]
        await client.send_message(
            OWNER_ID,
            f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a> Has started your bot",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def ping_cmd(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    await message.reply(
        f"<emoji id=6037295585067802696>🏓</emoji><code>{str(delta_ping)}ms</code>",
        quote=True
        )


async def start_cmd(client, message):
    await send_msg_to_owner(client, message)
    try:
        if len(message.command) < 2:
            buttons = Button.start(message)
            msg = MSG.START(message)
            await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
        if message.command[1] == "setart":
            buttons = Button.start(message)
            msg = MSG.START(message)
            await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
        else:
            return
    except:
        return

async def get_setarted(client, callback_query):
    user_id = callback_query.from_user.id
    user_doang = callback_query.from_user
    if user_id not in ubot._get_my_id:
        setatusnya = "Not Activated"
    else:
        setatusnya = "Activated"
    get_exp = await get_expired_date(user_id)
    try:
        modar = get_exp.strftime("%d-%m-%Y")
    except:
        modar = "-"
    buttons = [
            [
                InlineKeyboardButton("Server Status", callback_data="cobaae"),
                InlineKeyboardButton("-", callback_data="ukli"),
                ],
            [
                InlineKeyboardButton("Ask Owner", callback_data="support"),
                InlineKeyboardButton("Buy Token", callback_data="tuku_prem"),
                ],
            [
                InlineKeyboardButton("Generate Userbot", callback_data="bahan"),
                ],
            [
                InlineKeyboardButton("Back", callback_data=f"home {user_id}"),
                ],
                ]
    await callback_query.edit_message_text(
        f"""
<b>Manager KangerBot</b>

<b>ID:</b> <code>{user_doang.id}</code>
<b>DC ID:</b> {user_doang.dc_id}
<b>Name:</b> <a href='tg://user?id={user_doang.id}'>{user_doang.first_name} {user_doang.last_name or " "}</a>
<b>Username:</b> @{user_doang.username}
<b>Status:</b> {setatusnya}
<b>Vaporize:</b> {modar}

This bot maintenance by @Kanger
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
            )
