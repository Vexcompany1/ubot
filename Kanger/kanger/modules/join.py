from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Kanger import *


async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.join_chat(Man)
        await message.reply(f"Successfully joined to <b>{Man}</b>", quote=True)
    except Exception as ex:
        await message.reply(f"<code>{ex}</code>", quote=True)


async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.chat.id in BLACKLIST_CHAT:
        return await message.reply("This Command Not Allowed at Here.")
    try:
        await message.delete()
        await client.leave_chat(Man)
    except:
        return


async def kickmeall(client: Client, message: Message):
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await message.reply(
        f"Out from {done} Group \nCant Left from{er} Group",
        quote=True
    )


async def kickmeallch(client: Client, message: Message):
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await message.reply(
        f"Out from {done} Channel \nCant Left from{er} Channel",
        quote=True
    )
