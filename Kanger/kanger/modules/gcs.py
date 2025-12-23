import asyncio
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait

from Kanger import *


def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg


async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats
    

async def broadcast_group_cmd(client, message):
    msg = await message.reply("Processing...", quote=True)
    send = get_message(message)
    if not send:
        return await msg.edit("Input Text or Reply!")

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)
    blsk = BLACKLIST_CHAT

    done = 0
    undone = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        if chat_id in blsk:
            continue
        

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
                await msg.edit(f"<b>Processing...\n\nSend: {done} Group.\nUnsend: {undone} Group.</b>")
            else:
                await asyncio.sleep(2)
                await client.send_message(chat_id, send)
                await msg.edit(f"<b>Processing...\n\nSend: {done} Group.\nUnsend: {undone} Group.</b>")
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
                await msg.edit(f"<b>Processing...\n\nSend: {done} Group.\nUnsend: {undone} Group.</b>")
            else:
                await asyncio.sleep(2)
                await client.send_message(chat_id, send)
                await msg.edit(f"<b>Processing...\n\nSend: {done} Group.\nUnsend: {undone} Group.</b>")
            done += 1
        except Exception:
            undone += 1
            pass

    return await msg.edit(f"<b>Succesfully.\n\nSent: {done} Group.\nUnsent: {undone} Group.</b>")


async def broadcast_users_cmd(client, message):
    msg = await message.reply("Processing...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("Input Text or Reply!")

    chats = await get_broadcast_id(client, "users")

    done = 0
    for chat_id in chats:
        if chat_id == client.me.id:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>Sent to {sent} users</b>")


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        if not client.me.id == bot.me.id:
            if message.reply_to_message.reply_markup:
                try:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
                    tm = await message.reply(f"Sent to {chat_id}")
                    await asyncio.sleep(5)
                    await message.delete()
                    await tm.delete()
                except Exception as error:
                    await message.reply(error)
        else:
            try:
                await message.reply_to_message.copy(chat_id)
                tm = await message.reply(f"Sent to {chat_id}")
                await asyncio.sleep(3)
                await message.delete()
                await tm.delete()
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("Input Text or Reply")
        chat_id = message.text.split(None, 2)[1]
        chat_text = message.text.split(None, 2)[2]
        try:
            await client.send_message(chat_id, chat_text)
            tm = await message.reply(f"Sent to {chat_id}")
            await asyncio.sleep(3)
            await message.delete()
            await tm.delete()
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            )
        ],
    )
