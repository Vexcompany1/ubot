from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from Kanger import *

async def get_group_call(client, message) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    return False
    
async def joinvc(client, message):
    chat_id = message.chat.id
    if (
        group_call := (await get_group_call(client, message))
    ):
        return await message.reply("Video chat is active before...")
    try:
        await client.invoke(
            CreateGroupCall(
            peer=(await client.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999),
            )
        )
        await message.reply(f"<b>Successfully started</b>")
    except Exception as eek:
        return await message.reply(f"<code>{eek}</code>")


async def stop_vctools(client, message):
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message))
    ):
        return await message.reply("Video chat not found...")
    try:
        await client.invoke(DiscardGroupCall(call=group_call))
        await message.reply(
        f"<b>Successfully ended</b>"
        )
    except Exception as anu:
        return await message.reply(f"<code>{anu}</code>")