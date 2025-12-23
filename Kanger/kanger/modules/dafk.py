from datetime import datetime
from asyncio import sleep
from pyrogram import *
from pyrogram.types import *

from Kanger import *

async def is_afk_(f, client, message):
    user_id = client.me.id
    af_k_c = await check_afk(user_id)
    if af_k_c:
        return bool(True)
    else:
        return bool(False)

is_afk = filters.create(func=is_afk_, name="is_afk_")

async def set_afk(client, message):
    if len(message.command) == 1:
        return await message.edit("<b>AFK reason</b>")
    user_id = client.me.id
    msge = None
    msge = get_arg(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    await go_afk(user_id, afk_start, msge)
    await message.reply(
        f"<b>AFK</b>: <code>{msge}</code>",
        quote=True
        )


async def afk_er(client, message):
    user_id = client.me.id
    try:
        if not message.from_user:
            return
        if message.from_user.id == user_id:
            return
        lol = await check_afk(user_id)
        reason = lol["reason"]
        if reason == "":
            reason = None
        back_alivee = datetime.now()
        afk_start = lol["time"]
        afk_end = back_alivee.replace(microsecond=0)
        total_afk_time = str((afk_end - afk_start))
        await message.reply(
            f"<b>is Offline,</b> <code>{reason}</code>",
            quote=True
            )
    except:
        return
    
async def no_afke(client, message):
    user_id = client.me.id
    lol = await check_afk(user_id)
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(
        f"<b>No longer AFK.</b>\n<b>AFK For: </b><code>{total_afk_time}</code>",
        quote=True
        )
    await no_afk(user_id)
    
async def now_afke(client, message):
    try:
        await message.delete()
        await client.send_message(message.chat.id, "<i>You is afk</i>")
    except:
        return