import asyncio
from random import shuffle

tagallgcid = []


async def tagall_batal_cmd(client, message):
    if message.command[0] == "tagall":
        if message.chat.id in tagallgcid:
            return
        tagallgcid.append(message.chat.id)
        text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
        users = [
            member.user.mention
            async for member in message.chat.get_members()
            if not (member.user.is_bot or member.user.is_deleted)
        ]
        shuffle(users)
        m = message.reply_to_message or message
        for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
            if message.chat.id not in tagallgcid:
                break
            await asyncio.sleep(1.5)
            await m.reply_text(
                ", ".join(output) + "\n\n" + text, quote=bool(message.reply_to_message)
            )
        try:
            tagallgcid.remove(message.chat.id)
        except Exception:
            pass
    elif message.command[0] == "abort":
        if message.chat.id not in tagallgcid:
            return await message.reply_text(
                "Tagall is Not Activate."
            )
        try:
            tagallgcid.remove(message.chat.id)
        except Exception:
            pass
        await message.reply_text("Successfully Canceled!")
