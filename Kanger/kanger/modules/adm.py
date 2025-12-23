import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from pyrogram.errors import (
    UserAdminInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameInvalid,
    RPCError,
)

from Kanger import *

cause = " "
async def demote_command(client, message):
    if message.reply_to_message:
        if message.reply_to_message.from_user:
            try:
                await client.promote_chat_member(
                    message.chat.id,
                    message.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        is_anonymous=False,
                        can_manage_chat=False,
                        can_change_info=False,
                        can_post_messages=False,
                        can_edit_messages=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ),
                )
                await eor(message, "<b>Demoted!!</b>")
            except Exception as e:
                await eor(message, format_exc(e))
        else:
            await eor(message, "<b>Need Reply!!</b>")
    else:
        await eor(message, "<b>Need Reply!!</b>")

async def promote_command(client, message):
    if message.reply_to_message:
        if message.reply_to_message.from_user:
            try:
                await client.promote_chat_member(
                    message.chat.id,
                    message.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_promote_members=False,
                        can_change_info=False,
                    ),
                )
                await eor(message, "<b>Promoted!!</b>")
            except Exception as e:
                await eor(message, format_exc(e))
        else:
            await eor(message, "<b>Need Reply!!</b>")
    else:
        await eor(message, "<b>Need Reply!!</b>")


async def fullpromote_command(client, message):
    if message.reply_to_message:
        if message.reply_to_message.from_user:
            try:
                await client.promote_chat_member(
                    message.chat.id,
                    message.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_promote_members=True,
                        can_change_info=True,
                    ),
                )
                await eor(message, "<b>Promoted!!</b>")
            except Exception as e:
                await eor(message, format_exc(e))
        else:
            await eor(message, "<b>Need Reply!!</b>")
    else:
        await eor(message, "<b>Need Reply!!</b>")


async def admin_bannen(client, message):
    if message.command[0] == "kick":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await eor(message, "User Not Found.")
        if user_id == (await client.get_me()).id:
            return await eor(
                message,
                "I Cant Kick Myself."
            )
        if user_id == OWNER_ID:
            return await eor(message, "I Cant Kick This User")
        if user_id in (await list_admins(message)):
            return await eor(
                message,
                "Eitsss..."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await eor(message, error)
        msg = f"{mention} <b>Successfully Kicked!!</b>"
        if reason:
            msg += f"\n<b>Reason:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await eor(message, msg)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await eor(message, error)
    elif message.command[0] == "ban":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await eor(message, "User Not Found.")
        if user_id == (await client.get_me()).id:
            return await eor(
                message,
                "I Cant Ban Myself."
            )
        if user_id == OWNER_ID:
            return await eor(message, "I Cant Ban This user")
        if user_id in (await list_admins(message)):
            return await eor(
                message,
                "Eitsss..."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await eor(message, error)
        msg = (
            f"{mention}<b> Successfully Banned!!</b>"
        )
        if reason:
            msg += f"\n<b>Reason:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await eor(message, msg)
        except Exception as error:
            await eor(message, error)
    elif message.command[0] == "mute":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await eor(message, "User Not Found.")
        if user_id == (await client.get_me()).id:
            return await eor(
                message,
                "I Cant Mute Myself."
            )
        if user_id == OWNER_ID:
            return await eor(message, "I Cant Mute This User")
        if user_id in (await list_admins(message)):
            return await eor(
                message,
                "Eitsss..."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await eor(message, error)
        msg = f"{mention} <b>Successfully Muted!!"
        if reason:
            msg += f"\n<b>Reason:</b> {reason}"
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await eor(message, msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await eor(message, "User Not Found.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await eor(message, error)
        try:
            await message.chat.unban_member(user_id)
            await eor(message, f"<b>{mention} Successfully Unmuted.</b>")
        except Exception as error:
            await eor(message, error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await eor(message, "User Not Found.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await eor(message, error)
        try:
            await message.chat.unban_member(user_id)
            await eor(message, f"<b>{mention} Successfully Unbanned.</b>")
        except Exception as error:
            await eor(message, error)
            
            
async def admin_sbannen(client, message):
    if message.command[0] == "skick":
        user_id = await extract_user(message)
        await message.delete()
        if not user_id:
            return
        if user_id == (await client.get_me()).id:
            return
        if user_id == OWNER_ID:
            return
        if user_id in (await list_admins(message)):
            return
        try:
            await message.chat.ban_member(user_id)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except:
            return
    elif message.command[0] == "sban":
        user_id = await extract_user(message)
        await message.delete()
        if not user_id:
            return 
        if user_id == (await client.get_me()).id:
            return
        if user_id == OWNER_ID:
            return
        if user_id in (await list_admins(message)):
            return
        try:
            await message.chat.ban_member(user_id)
        except:
            return
    elif message.command[0] == "smute":
        user_id = await extract_user(message)
        await message.delete()
        if not user_id:
            return
        if user_id == (await client.get_me()).id:
            return
        if user_id == OWNER_ID:
            return
        if user_id in (await list_admins(message)):
            return
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
        except:
            return
    elif message.command[0] == "sunmute":
        user_id = await extract_user(message)
        await message.delete()
        if not user_id:
            return
        try:
            await message.chat.unban_member(user_id)
        except:
            return
    elif message.command[0] == "sunban":
        user_id = await extract_user(message)
        await message.delete()
        if not user_id:
            return
        try:
            await message.chat.unban_member(user_id)
        except:
            return


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>Processing...</b>")
    if not user_id:
        return await Tm.edit("<b>User Not Found.</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    if message.command[0] == "gban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == OWNER_ID:
                    return await Tm.edit(
                        "Are u Kidding?"
                    )
                elif not user.id == OWNER_ID:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await Tm.edit(
                        f"""
<b>Global Banned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)
                        await asyncio.sleep(2)
                    except:
                        failed += 1
                        await Tm.edit(
                        f"""
<b>Global Banned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)
                        await asyncio.sleep(2)
        return await Tm.edit(
            f"""
<b>Global Banned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)

    elif message.command[0] == "ungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await Tm.edit(
                        f"""
<b>Global Banned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)
                    await asyncio.sleep(2)
                except:
                    failed += 1
                    await Tm.edit(
                        f"""
<b>Global Banned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)
                    await asyncio.sleep(2)
        return await Tm.edit(
            f"""
<b>Global Unbanned</b>
<b>Success: {done}</b>
<b>Abort: {failed}</b>
<b>User:<a href='tg://user?id={user.id}'> {user.first_name} {user.last_name or ""}</a></b>
"""
)
                    
async def global_sbanned(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.react("👎")
    try:
        user = await client.get_users(user_id)
    except:
        return await message.react("👎")
    try:
        if message.command[0] == "sgban":
            async for dialog in client.get_dialogs():
                chat_type = dialog.chat.type
                if chat_type in [
                    ChatType.GROUP,
                    ChatType.SUPERGROUP,
                    ChatType.CHANNEL,
                ]:
                    chat_id = dialog.chat.id
                    if user.id == OWNER_ID:
                        return
                    elif not user.id == OWNER_ID:
                        try:
                            await client.ban_chat_member(chat_id, user.id)
                            await asyncio.sleep(0.1)
                        except:
                            await asyncio.sleep(0.1)
            return await message.react("👍")
        elif message.command[0] == "sungban":
            async for dialog in client.get_dialogs():
                chat_type = dialog.chat.type
                if chat_type in [
                    ChatType.GROUP,
                    ChatType.SUPERGROUP,
                    ChatType.CHANNEL,
                ]:
                    chat_id = dialog.chat.id
                    try:
                        await client.unban_chat_member(chat_id, user.id)
                        await asyncio.sleep(0.1)
                    except:
                        await asyncio.sleep(0.1)
            return await message.react("👍")
    except:
        await message.react("👎")