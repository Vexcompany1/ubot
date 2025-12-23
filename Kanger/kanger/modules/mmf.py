import asyncio
import os

from Kanger import *


async def memify_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply("Need Reply to Media!")
    reply_message = message.reply_to_message
    if not reply_message.media:
        return await message.reply("Need Reply to Media!")
    file = await client.download_media(reply_message)
    Tm = await message.reply("Processing...")
    text = get_arg(message)
    if len(text) < 1:
        return await Tm.edit(f"Input Text!")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(meme)
