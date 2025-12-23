import asyncio
from gc import get_objects


from Kanger import *


async def copy_ubot_msg(client, message):
    Tm = await message.reply("Processing...")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> Link</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id)
            await Tm.delete()
        except:
            try:
                raw_input
            except Except as anunya:
                await Tm.edit(anunya)
    else:
        await Tm.edit("Link Invalid!")