import asyncio

from pyrogram.enums import UserStatus

from Kanger import *


async def invite_cmd(client, message):
    mg = await message.reply("<b>Invited User...</b>")
    if len(message.command) < 2:
        return await mg.edit("<b>Input Username!</b>")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            "<b>Input Username!</b>"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"<b>Successfully Added.</b>")