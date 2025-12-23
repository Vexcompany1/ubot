import sys
from os import environ, execle
from io import BytesIO, StringIO


from Kanger import *


async def user_cek(client, message):
    memek = message.from_user.id
    if message.from_user.id not in await get_seles():
        return await message.reply(
            "Are u kidding me?"
        )
    count = 0
    user = ""
    for X in ubot._ubot:
        try:
            get_exp = await get_expired_date(X.me.id)
            try:
                exp = get_exp.strftime("%d-%m-%Y")
            except:
                exp = "Unlimited"
            count += 1
            user += f"""
kangerPeople {count}
Account: <a href="tg://user?id={X.me.id}">{X.me.first_name} {X.me.last_name or ''}</a>
Vaporize: <code>{exp}</code>
"""
        except:
            pass
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")
