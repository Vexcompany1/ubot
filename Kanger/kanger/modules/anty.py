from asyncio import sleep
from pyrogram import *
from pyrogram.types import *
from pyrogram.raw.functions.messages import DeleteHistory

from Kanger import *

async def is_antipm_(f, client, message):
    user_id = client.me.id
    antipm_c = await check_antipm(user_id)
    if antipm_c:
        return bool(True)
    else:
        return bool(False)

is_antipm = filters.create(func=is_antipm_, name="is_antipm_")

async def set_antipm(client, message):
    try:
        if message.command[1] == "on":
            user_id = client.me.id
            anukus = datetime.now()
            await go_antipm(user_id)
            await message.reply(
                f"<b>Anti-PM activated!!</b>",
                quote=True
                )
        elif message.command[1] == "off":
            user_id = client.me.id
            await no_antipmk(user_id)
            await message.reply(
                f"<b>Anti-PM deactived!!</b>",
                quote=True
                )
        else:
            kontols = await check_antipm(client.me.id)
            try:
                kurukuru = kontols["antipm"]
            except:
                kurukuru = "False"
            await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)
    except:
        kontols = await check_antipm(client.me.id)
        try:
            kurukuru = kontols["antipm"]
        except:
            kurukuru = "False"
        await message.reply(f"<b>Anti-PM status:</b> <code>{kurukuru}</code>\n<b>To Activate use</b> <code>antipm on/off</code>", quote=True)

async def antipm_er(client, message):
    anuku = await client.resolve_peer(message.chat.id)
    if message.from_user.is_contact is True:
        return
    if message.from_user.is_support is True:
        return
    if message.from_user.id == OWNER_ID:
        return
    await client.invoke(DeleteHistory(peer=anuku, max_id=0, revoke=True))