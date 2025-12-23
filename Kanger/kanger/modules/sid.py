from pyrogram.enums import ChatType

from Kanger import *


async def id_cmd(client, message):
    if len(message.command) < 2:
        chat_type = message.chat.type
        if chat_type == ChatType.PRIVATE:
            user_id = message.chat.id
            await message.reply_text(
                f"<code>{user_id}</code>",
                quote=True
            )
        elif chat_type == ChatType.CHANNEL:
            await message.reply(
                f"Channel: <code>{message.sender_chat.id}</code>",
            )
        elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            _id = ""
            _id += f"Me: <code>{message.from_user.id}</code>\nGroup: <code>{message.chat.id}</code>\n"
            if message.reply_to_message:
                _id += f"<b>Reply:</b> <code>{message.reply_to_message.from_user.id}</code>\n"
                file_info = get_file_id(message.reply_to_message)
                if file_info:
                    _id += f"<b>File:</b> <code>{file_info.file_id}</code>"
            m = message.reply_to_message or message
            return await m.reply_text(_id)
    try:
        chat_id = message.text.split()[1]
        get = await client.get_chat(chat_id)
        name = f"{get.title}"
        if name == "None":
            get = await client.get_users(chat_id)
            name = f"{get.first_name} {get.last_name or ''}"
        msg = f"<b>{name}:</b> <code>{get.id}</code>"
        return await message.reply(msg)
    except:
        return
