import importlib
import random
from datetime import datetime, timedelta

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from Kanger import *


async def login_cmd(client, message):
    info = await message.reply("<b>Processing...</b>", quote=True)
    if len(message.command) < 3:
        return await info.edit(
            f"<b>Input Day and String.</b>"
        )
    try:
        ub = Ubot(
            name=f"ubot_{random.randrange(999999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
            device_model=DEVICE_MODEL,
        )
        await ub.start()
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"Kanger.modules.{mod}"))
        now = datetime.now(timezone("Asia/Jakarta"))
        expire_date = now + timedelta(days=int(message.command[1]))
        await set_expired_date(ub.me.id, expire_date)
        await add_ubot(
            user_id=int(ub.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
            device_model=DEVICE_MODEL,
        )
        buttons = [
            [
                InlineKeyboardButton(
                    "Check Vaporize Timeout",
                    callback_data=f"cek_masa_aktif {ub.me.id}",
                )
            ],
        ]
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
<b>Kanger Activated!</b>
<b>kanger:</b> <a href=tg://user?id={ub.me.id}>{ub.me.first_name} {ub.me.last_name or ''}</a>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
        return await info.edit(
            f"<b>Successfully Login to: <a href='tg://user?id={ub.me.id}'>{ub.me.first_name} {ub.me.last_name or ''}</a></b>"
        )
    except Exception as error:
        return await info.edit(f"<code>{error}</code>")


async def restart_cmd(client, message):
    user_id = message.from_user.id
    if user_id not in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("Activate", url="https://t.me/KangerBot?start=setart")],
            ]
        return await message.reply(
            f"<b>Sorry you not activated:\n\nName: {message.from_user.first_name}\nID: {user_id}</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
            )
    else:
        anu = await message.reply(
        f"<b>Restarting KangerBot for:\n\nName: {message.from_user.first_name}\nID: {user_id}\n\nWait any second!!</b>",
        )
        
    for X in ubot._ubot:
        if user_id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"Kanger.modules.{mod}")
                            )
                        buttons = [
                            [InlineKeyboardButton("Check Vaporize", callback_data=f"cek_masa_aktif {user_id}")],
                            ]
                    except:
                        return
                    await anu.edit(
                            f"<b>Restarting Successfully!!\n\nName: {message.from_user.first_name}\nID: {user_id}</b>",
                            disable_web_page_preview=True,
                            reply_markup=InlineKeyboardMarkup(buttons),
                            )
