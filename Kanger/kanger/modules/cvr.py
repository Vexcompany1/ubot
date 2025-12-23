import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from Kanger import *

async def convert_photo(client, message):
    try:
        file_io = await dl_pic(client, message.reply_to_message)
        file_io.name = "sticker.png"
        await client.send_photo(
            message.chat.id,
            file_io,
            reply_to_message_id=message.id,
        )
    except:
        return


async def convert_sticker(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply_text("Reply To Photos")
        sticker = await client.download_media(
            message.reply_to_message.photo.file_id,
            f"sticker_{message.from_user.id}.webp",
        )
        await message.reply_sticker(sticker)
        os.remove(sticker)
    except:
        return


async def convert_gif(client, message):
    if not message.reply_to_message.sticker:
        return await message.reply("<b>Reply To Stickers...</b>")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except:
        return


async def convert_audio(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("<b>Reply To Videos</b>")
    if replied.media == MessageMediaType.VIDEO:
        file = await client.download_media(
            message=replied,
            file_name=f"toaudio_{replied.id}",
        )
        out_file = f"{file}.mp3"
        try:
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(file)
        except:
            return
    else:
        return await message.reply("<b>Reply To Videos.</b>")

async def colong_cmn(client, message):
    dia = message.reply_to_message
    if not dia:
        return await message.delete()
    anjing = dia.caption or ""
    if dia.photo:
        await message.delete()
        anu = await client.download_media(dia)
        await client.send_photo(client.me.id, anu, anjing)
        os.remove(anu)
    if dia.video:
        await message.delete()
        anu = await client.download_media(dia)
        await client.send_video(client.me.id, anu, anjing)
        os.remove(anu)
    if dia.audio:
        await message.delete()
        anu = await client.download_media(dia)
        await client.send_audio(client.me.id, anu, anjing)
        os.remove(anu)
    if dia.voice:
        await message.delete()
        anu = await client.download_media(dia)
        await client.send_voice(client.me.id, anu, anjing)
        os.remove(anu)
    if dia.document:
        await message.delete()
        anu = await client.download_media(dia)
        await client.send_document(client.me.id, anu, anjing)
        os.remove(anu)
    else:
        return