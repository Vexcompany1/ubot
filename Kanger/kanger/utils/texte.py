from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Kanger import OWNER_ID, bot
from Kanger import *


class MSG:
    def EXPIRED_MSG_BOT(X):
        return f"""
<b>Annouchment</b>
<b>kanger:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>His account has vaporated!</b>
"""

    def START(message):
        if not message.from_user.id == OWNER_ID:
            msg = f"""<b>👋 Hi!, {message.from_user.first_name},

Welcome to {bot.me.mention}!
I can create Userbot instantly</b>
"""
        else:
            msg = f"""<b>👋 Hi!, {message.from_user.first_name},

Welcome to {bot.me.mention}!
I can create Userbot instantly</b>
"""
        return msg

    def ABORT_GEN(message):
        return """
<b>⚠️ Generate Aborted!!

To Generate again 
Press button above!!</b>
"""

    def CANCEL_GEN(message):
        return """
<b>⚠️ Generate Canceled!!

To Generate again 
Press button above!!</b>
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        try:
            anu = expired_date.strftime('%d-%m-%Y')
        except:
            anu = "Unlimited"
        return f"""
<b>Number:</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>kanger:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a>
<b>User ID:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b>DC ID:</b> <code>{ubot._ubot[int(count)].me.dc_id}</code>
<b>Phone:</b> <code>{ubot._ubot[int(count)].me.phone_number}</code>
<b>2Auth:</b> <code>{await get_two_factor(ubot._ubot[int(count)].me.id) or "None"}
<b>Vaporize in:</b> <code>{anu}</code>
"""

    def POLICY():
        return """
📌 Click below if you have agreed with the applicable requirements.

If your account is deactivated by the telegram, the owner of the bot is not responsible about that.
"""


async def sending_user(user_id):
    await bot.send_message(
        user_id,
        "Please re-create our bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Generate Userbot",
                        callback_data="bahan",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
