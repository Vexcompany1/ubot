import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from Kanger import *



async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("Processing...")
    if not user_id:
        return await tex.edit("Need Reply Chat or Username.")
    if user_id == client.me.id:
        return await tex.edit("Are u kidding me?")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>{umention} Has Unblocked!</b>")


async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("Processing...")
    if not user_id:
        return await tex.edit(f"Need Reply or Username.")
    if user_id == client.me.id:
        return await tex.edit("Are u kidding me?")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>{umention} Has Blocked!")


async def setname(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply("Input Text!")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await message.reply(
                f"<b>Name Changed to</b> <code>{name}</code>"
            )
        except:
            return
    else:
        return await message.reply("Input Text!")


async def set_bio(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply("Input Text!")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await message.reply(f"<b>Bio Changed to</b> <code>{bio}</code>")
        except:
            return
    else:
        return await message.reply("Need Input!")
