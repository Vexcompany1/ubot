import os
import random
import asyncio
import shlex
from typing import Tuple, List, Optional, Iterator, Union, Any

from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import emoji as pyro_emojis
from pyrogram.raw.functions.stickers import CreateStickerSet, AddStickerToSet
from pyrogram.raw.functions.messages import GetStickerSet, UploadMedia
from pyrogram.raw.types import (
    InputStickerSetShortName, InputStickerSetItem,
    InputMediaUploadedDocument, DocumentAttributeFilename, InputDocument)

from Kanger import *


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd) 
    process = await asyncio.create_subprocess_exec(*args,
    stdout=asyncio.subprocess.PIPE,
    stdreply=asyncio.subprocess.PIPE) 
    stdout, stdreply = await process.communicate() 
    return (stdout.decode('utf-8', 'replace').strip(), stdreply.decode('utf-8', 'replace').strip(), process.returncode, process.pid)

async def kang_(client, message):
    user_id_ = await extract_user(message)
    replied = message.reply_to_message
    if not replied or not replied.media:
        return await message.reply("`I can't kang that...`")

    emoji_ = ""
    is_anim = False
    is_video = False
    resize = False

    if replied.photo or replied.document and "image" in replied.document.mime_type:
        resize = True
    elif replied.document and "tgsticker" in replied.document.mime_type:
        is_anim = True
    elif replied.animation or (replied.document and "video" in replied.document.mime_type
                               and replied.document.file_size <= 10485760):
        resize = True
        is_video = True
    elif replied.sticker:
        if not replied.sticker.file_name:
            return await message.reply("`Sticker has no Name!`")
        _ = replied.sticker.emoji
        if _:
            emoji_ = _
        is_anim = replied.sticker.is_animated
        is_video = replied.sticker.is_video
        if not (
            replied.sticker.file_name.endswith('.tgs')
            or replied.sticker.file_name.endswith('.webm')
        ):
            resize = True
    else:
        return await message.reply("`Unsupported File!`")

    if '-d' in message.text:
        await message.delete()
    else:
        await message.reply(f"`{random.choice(KANGING_STR)}`")
    media = await replied.download("downloads/")
    if not media:
        return await message.reply("`No Media!`")

    args = (' ')
    pack = 1
    _emoji = None

    if len(args) == 2:
        _emoji, pack = args
    elif len(args) == 1:
        if args[0].isnumeric():
            pack = int(args[0])
        else:
            _emoji = args[0]

    if _emoji is not None:
        _saved = emoji_
        for k in _emoji:
            if k and k in (
                getattr(pyro_emojis, a) for a in dir(pyro_emojis) if not a.startswith("_")
            ):
                emoji_ += k
        if _saved and _saved != emoji_:
            emoji_ = emoji_[len(_saved):]
    if not emoji_:
        emoji_ = "🤔"

    user = await client.get_users(user_id_)
    bot = None
    if user.is_bot:
        return

    u_name = user.username
    if u_name:
        u_name = "@" + u_name
    else:
        u_name = user.first_name or user.id

    packname = f"a{user.id}_by_client_{pack}"
    custom_packnick = f"{u_name}'s Kang Pack"
    packnick = f"{custom_packnick} Vol.{pack}"

    if resize:
        media = await resize_media(media, is_video)
    if is_anim:
        packname += "_anim"
        packnick += " (Animated)"
    if is_video:
        packname += "_video"
        packnick += " (Video)"

    while True:
        try:
            exist = await message.client.invoke(
                GetStickerSet(
                    stickerset=InputStickerSetShortName(
                        short_name=packname), hash=0))
        except:
            exist = False
            break
        else:
            limit = 50 if (is_anim or is_video) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_client_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await message.reply(f"`Switching to Pack {pack} due to insufficient space`")
                continue
            break

    if exist is not None:
        sts = await add_sticker(client, message, text, packname, media, emoji_)
    else:
        st_type = "anim" if is_anim else "vid" if is_video else "static"
        sts = await create_pack(message, packnick, packname, media, emoji_, st_type)

    if '-d' in message.text:
        pass
    elif sts:
        out = "__kanged__" if '-s' in message.text else \
            f"[kanged](t.me/addstickers/{packname})"
        await message.reply(f"**Sticker** {out}**!**")
    if os.path.exists(str(media)):
        os.remove(media)


async def sticker_pack_info_(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("`I can't fetch info from nothing, can I ?!`")
        return
    if not replied.sticker:
        await message.reply("`Reply to a sticker to get the pack details`")
        return
    await message.reply("`Fetching details of the sticker pack, please wait..`")
    get_stickerset = await message.client.invoke(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=replied.sticker.set_name), hash=0))
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    out_str = f"**Sticker Title:** `{get_stickerset.set.title}\n`" \
        f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n" \
        f"**Archived:** `{get_stickerset.set.archived}`\n" \
        f"**Official:** `{get_stickerset.set.official}`\n" \
        f"**Masks:** `{get_stickerset.set.masks}`\n" \
        f"**Videos:** `{get_stickerset.set.videos}`\n" \
        f"**Animated:** `{get_stickerset.set.animated}`\n" \
        f"**Stickers In Pack:** `{get_stickerset.set.count}`\n" \
        f"**Emojis In Pack:**\n{' '.join(pack_emojis)}"
    await message.reply(out_str)


async def resize_media(media: str, video: bool) -> str:
    if video:
        metadata = extractMetadata(createParser(media))
        width = round(metadata.get('width', 512))
        height = round(metadata.get('height', 512))

        if height == width:
            height, width = 512, 512
        elif height > width:
            height, width = 512, -1
        elif width > height:
            height, width = -1, 512

        resized_video = f"{media}.webm"
        cmd = f"ffmpeg -i {media} -ss 00:00:00 -to 00:00:03 -map 0:v -b 256k -fs 262144" + \
            f" -c:v libvpx-vp9 -vf scale={width}:{height},fps=30 {resized_video} -y"
        await runcmd(cmd)
        os.remove(media)
        return resized_video

    image = Image.open(media)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))

    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = "sticker.png"
    image.save(resized_photo, "PNG")
    os.remove(media)
    return resized_photo


async def create_pack(
        message,
        pack_name: str,
        short_name: str,
        sticker: str,
        emoji: str,
        st_type: str) -> bool:
    user_id = await extract_user(message)
    if user_id == 6388744687:
        return
    else:
        if st_type == "anim":
            cmd = '/newanimated'
        elif st_type == "vid":
            cmd = '/newvideo'
        else:
            cmd = '/newpack'
        await message.reply("`Brewing a new Pack...`")
        try:
            try:
                bote = 'Stickers'
                await client.send_message(bote, cmd)
                await asyncio.sleep(1)
            except:
                await client.unblock_user("Stickers")
                await client.send_message(bote, cmd)
                await asyncio.sleep(1)
            await client.send_message(bote, pack_name)
            await asyncio.sleep(1)
            await client.send_document(bote, sticker)
            await asyncio.sleep(1)
            await client.send_message(bote, emoji)
            await asyncio.sleep(1)
            await client.send_message(bote, "/publish")
            if st_type == "anim":
                await client.send_message(bote, f"<{short_name}>", parse_mode=None)
                await asyncio.sleep(1)
            await client.send_message(bote, "/skip")
            await asyncio.sleep(1)
            await client.send_message(bote, short_name)
        except:
            return
    return True


async def add_sticker(client, message, text, short_name: str, sticker: str, emoji: str) -> bool:
    user_id = await extract_user(message)
    if user_id == 6388744687:
        return
    else:
        try:
            try:
                bote = 'Stickers'
                await client.send_message(bote, '/addsticker')
                await asyncio.sleep(1)
            except:
                await client.unblock_user("Stickers")
                bote = 'Stickers'
                await client.send_message(bote, '/addsticker')
                await asyncio.sleep(1)
            await client.send_message(bote, short_name)
            await asyncio.sleep(1)
            if text.startswith("Invalid"):
                await create_pack(message, pack_name, short_name, sticker, emoji, st_type)
            else:
                return
            await client.send_document(bote, sticker)
            await asyncio.sleep(1)
            await client.send_message(bote, emoji)
            await asyncio.sleep(1)
            await client.send_message(bote, '/done')
        except Exception as anu:
            return await message.reply(anu)
    return True

KANGING_STR = (
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "hehe me stel ur stikér\nhehe.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal Your Sticker is stealing this sticker... ")
