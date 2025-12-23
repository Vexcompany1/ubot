import asyncio
import random

from pyrogram.raw.functions.messages import DeleteHistory

from Kanger import *


async def sg_cmd(client, message):
    try:
        anu = message.reply_to_message
        user_id = anu.from_user.id
        bot = "@SangMata_BOT"
        await client.unblock_user(bot)
        txt = await client.send_message(bot, user_id)
        await asyncio.sleep(3)
        await txt.delete()
        async for name in client.search_messages(bot, limit=2):
            if not name.text:
                await message.reply(
                    f"SangMata Not Respond!", quote=True
                )
            else:
                await message.reply(name.text, quote=True)
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except:
        return await message.reply("<b>Need Reply!!</b>")
