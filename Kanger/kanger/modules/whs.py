from asyncio import gather
from os import remove

from pyrogram.enums import ChatType

from Kanger import *


async def info_cmd(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply(
            "<b>Need Reply or Username.</b>",
            quote=True
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<b>User Info:</b>

<b>ID:</b> <code>{user.id}</code>
<b>First:</b> {first_name}
<b>Last:</b> {last_name}
<b>Username:</b> {username}
<b>DC:</b> <code>{dc_id}</code>
<b>Bot?:</b> <code>{user.is_bot}</code>
<b>Scam?:</b> <code>{user.is_scam}</code>
<b>Restrict?:</b> <code>{user.is_restricted}</code>
<b>Verified?:</b> <code>{user.is_verified}</code>
<b>Premium?:</b> <code>{user.is_premium}</code>
<b>Bio:</b> {bio}
<b>Same Group:</b> {len(common)}
<b>Last Seen:</b> <code>{status}</code>
<b>Direct Link:</b> <a href=tg://user?id={user.id}>{fullname}</a>
"""
        await message.reply(
            out_str,
            quote=True,
            disable_web_page_preview=True
            )
    except Exception as e:
        return await message.reply(
            f"ERROR: {e}",
            quote=True
            )


async def cinfo_cmd(client, message):
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await message.reply(
                    f"Use at Group",
                    quote=True
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
<b>Chat Info:</b>

<b>ID:</b> <code>{chat.id}</code>
<b>Title:</b> {chat.title}
<b>Username:</b> {username}
<b>Type:</b> <code>{type}</code>
<b>DC:</b> <code>{dc_id}</code>
<b>Restrict Media:</b> <code>{chat.has_protected_content}</code>
<b>Member:</b> <code>{chat.members_count}</code>
<b>Desc:</b> <code>{description}</code>
"""
        await message.reply(
            out_str,
            quote=True,
            disable_web_page_preview=True
            )
    except Exception as e:
        return await message.reply(
            f"ERROR: `{e}`",
            quote=True
            )
