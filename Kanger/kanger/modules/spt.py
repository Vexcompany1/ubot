import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Kanger import *

SUPPORT = []


async def support_callback(client, callback_query):
    await callback_query.message.edit("Processing...")
    await asyncio.sleep(0.5)
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    await callback_query.message.delete()
    SUPPORT.append(get.id)
    try:
        button = [
            [InlineKeyboardButton("Cancel", callback_data="mboh")]
        ]
        pesan = await bot.ask(
            user_id,
            f"<b>What do u Asking? {full_name}</b>\nPlease use formaly ask!!",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=20,
        )
    except:
        return
    buttons = [
        [
            InlineKeyboardButton("Answer", callback_data=f"jawab_pesan {user_id}"),
        ],
    ]
    hohuwir = [
        [
            InlineKeyboardButton("Ask Again", callback_data="support")
            ],
        [
                    InlineKeyboardButton("Back", callback_data="mboh")
            ],
            ]
    if get.id in SUPPORT:
        try:
            await bot.send_message(
                OWNER_ID,
                f"<b>From:</b> <a href=tg://user?id={callback_query.from_user.id}>{full_name}</a>\n<b>Msg:</b> {pesan.text}",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"<b>{full_name} Your ask has sent to owner\n\nText:</b> <code>{pesan.text}</code>",
                reply_markup=InlineKeyboardMarkup(hohuwir),
            )
            return await pesan.delete()
        except Exception as error:
            return await bot.send_message(user_id, error)


async def jawab_pesan_callback(client, callback_query):
    await callback_query.message.edit("Processing...")
    await asyncio.sleep(1)
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    user_ids = int(callback_query.data.split()[1])
    SUPPORT.append(get.id)
    await callback_query.message.delete()
    try:
        button = [
            [InlineKeyboardButton("Close", callback_data=f"batal {user_id}")]
        ]
        pesan = await bot.ask(
            user_id,
            f"<b>Sent our Answer, {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button)
        )
    except:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return
    buttons = [
        [
            InlineKeyboardButton("Answer", callback_data=f"jawab_pesan {user_id}"),
            ],
            ]
    if get.id in SUPPORT:
        try:
            if get.id == OWNER_ID:
                await bot.send_message(
                    user_ids,
                    f"From: Owner\n\nText: {pesan.text}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                SUPPORT.remove(get.id)
                await pesan.delete()
                await pesan.request.edit(
                    f"<b>Succesfully sent\n\nText:</b> <code>{pesan.text}</code>"
                    )
            else:
                await bot.send_message(
                    OWNER_ID,
                    f"From: {full_name}\n\nText: {pesan.text}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
                SUPPORT.remove(get.id)
                await pesan.delete()
                buttons = [
                    [
                InlineKeyboardButton("Answer Again", callback_data=f"jawab_pesan {user_id}"),
                ]
                ]
                await pesan.request.edit(
                    f"<b>{full_name} Your ask has sent to owner\n\nText:</b> <code>{pesan.text}</code>",
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as error:
            return await bot.send_message(user_id, error)


async def profil_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    try:
        get = await bot.get_users(user_id)
        first_name = f"{get.first_name}"
        last_name = f"{get.last_name}"
        full_name = f"{get.first_name} {get.last_name or ''}"
        username = f"{get.username}"
        msg = (
            f"<b>User: <a href=tg://user?id={get.id}>{full_name}</a></b>\n"
            f"<b>Id: </b><code>{get.id}</code>\n"
            f"<b>First Name:</b> {first_name}\n"
        )
        if last_name == "None":
            msg += ""
        else:
            msg += f"<b>Last Name:</b> {last_name}\n"
        if username == "None":
            msg += ""
        else:
            msg += f"<b>Username:</b> @{username}\n"
        msg += f"<b>Bot: {bot.me.mention}\n"
        buttons = [
            [
                InlineKeyboardButton(
                    f"{full_name}",
                    url=f"tg://openmessage?user_id={get.id}",
                )
            ]
        ]
        await callback_query.edit_message_text(
            msg, reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as why:
        await callback_query.edit_message_text(why)


async def batal_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    if user_id in SUPPORT:
        try:
            SUPPORT.remove(user_id)
            return await callback_query.message.delete()
        except:
            return await callback_query.message.delete()