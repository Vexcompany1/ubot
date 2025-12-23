from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from Kanger import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    if message.from_user.id not in await get_seles():
        return await message.reply(
            "Are u Kidding?"
        )
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply(f"<b>Input Int</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await message.reply(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        return await message.reply("Already...")
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        await message.reply(
            f"Access granted to {get_id} for {get_bulan} Month\n\nCreate Userbot at @{bot.me.username}"
        )
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Profile",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "Profile", callback_data=f"profil {get_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await message.reply("An Error Occured")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            "<b>Need Reply.</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await message.reply("<b>Not Found.</b>")
    removed = await remove_prem(user.id)
    if removed:
        await message.reply(f"<b>Successfully Removed</b>")
    else:
        await message.reply("An Error Occuired")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"Number {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply("User Not Found.")
    else:
        await message.reply(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blaclist(client, message):
    chat_id = message.chat.id
    blacklist = await get_chat(client.me.id)
    if chat_id in blacklist:
        return await message.reply("Already at Blacklist")
    add_blacklist = await add_chat(client.me.id, chat_id)
    if add_blacklist:
        await message.reply(f"Successfully added to Blacklist")
    else:
        await message.reply("An Error Occuired.")


async def del_blacklist(client, message):
    try:
        if not get_arg(message):
            chat_id = message.chat.id
        else:
            chat_id = int(message.command[1])
        blacklist = await get_chat(client.me.id)
        if chat_id not in blacklist:
            return await message.reply("Not in Blacklist")
        del_blacklist = await remove_chat(client.me.id, chat_id)
        if del_blacklist:
            await message.reply(f"{chat_id} Successfully Purged from Blacklist")
        else:
            await message.reply("An Error Occuired.")
    except Exception as error:
        await message.reply(error)


async def get_blacklist(client, message):
    msg = f"<b>List Blacklist {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await message.reply("<b>Your Blacklist is Empty.</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await message.reply("<b>All Blacklist Has Been Purged.</b>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            "<b>Reply User/Username.</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await message.reply("Already in Archon list.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await message.reply(f"<b>{user.mention} Promoted to Archon.</b>")
    else:
        await message.reply("An Error Occuired.")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            "<b>Reply user/username.</n>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await message.reply(error)
    try:
        delreseller = await get_seles()
    except Exception as error:
        await message.reply("<b>Purged from Archon.</b>")
    if user.id not in delreseller:
        return await message.reply("Not Found.")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await message.reply("Successfully purged from Archon.")
    else:
        await message.reply("An Error Occuired")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"~ {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply("User Not Found.")
    else:
        await message.reply(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply("<b>Need Input!</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await message.reply(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await message.reply(f"Account {get_id} Has Activated for {get_day} Days.")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("User Not Found.")
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply("Not Activated.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"Account {user_id} Active for {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Remaining {remaining_days} Days."
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("<b>User Not Found.</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await message.reply("<b>Expired has purged.</b>")
