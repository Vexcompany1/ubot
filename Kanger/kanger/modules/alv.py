from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from Kanger import *


async def alive_cmd(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        #await message.delete()
    except Exception as ahtaht:
        await message.reply(f"<code>{ahtaht}</code>")


async def alive_query(client, inline_query):
    get_id = inline_query.query.split()
    inianu = await get_userbots()
    anunya = await get_seles()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            get_exp = await get_expired_date(my.me.id)
            try:
                exp = get_exp.strftime("%d-%m-%Y")
            except:
                exp = "Unlimited"
            if my.me.id == OWNER_ID:
                status = "Kanger Dominus"
            elif my.me.id in await get_seles():
                status = "Kanger Venditor"
            else:
                status = "Kanger Servus"
            nyugs = inline_query.from_user.id
            button = Button.alive(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            kontols = await check_antipm(nyugs)
            try:
                kurukuru = kontols["antipm"]
            except:
                kurukuru = "False"
            msg = f"""
<b>KangerUbot</b>
    Status: <code>{status}</code>
    Antipm: <code>{kurukuru}</code>
    Vaporize on: <code>{exp}</code>
<b>Network:</b>
    DC: <code>{my.me.dc_id}</code>
    Ping: <code>{ping}</code>"""
            if my.me.id == OWNER_ID:
                msg += f"""
<b>Stats:</b>
    User: <code>{len(inianu)}</code>
    Venditor: <code>{len(anunya)}</code>
    Online Since: <code>{uptime}</code>
"""
            else:
                msg += f"""
    Online Since: <code>{uptime}</code>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            text="Deploy", url="https://t.me/BotFather?start=setart"
                                            ),
                                            InlineKeyboardButton(
                                                text="Contact me", user_id=f"{nyugs}"
                                                ),
                                                ],
                                                ]),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


async def alive_close(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return await callback_query.answer(
            f"This Button Not For You {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )
