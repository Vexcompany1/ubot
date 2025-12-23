from gc import get_objects
from io import BytesIO

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from Kanger import *


async def addnote_cmd(client, message):
    note_name = get_arg(message)
    reply = message.reply_to_message
    if reply and note_name:
        if await get_note(client.me.id, note_name):
            return await message.reply(f"{note_name} Already Exist!", quote=True)
        copy = await client.copy_message(client.me.id, message.chat.id, reply.id)
        await save_note(client.me.id, note_name, copy.id)
        await copy.reply(
            f"Dont Remove!",
            quote=True
        )
        await message.reply("Notes Saved!", quote=True)
    else:
        return await message.reply(
            "Need Reply and Name Notes.",
            quote=True
        )


async def get_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("What do u need?", quote=True)
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"{note_name} is Not Exist.", quote=True)
    note_id = await client.get_messages(client.me.id, note)
    if note_id.text:
        if "|" in note_id.text:
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {id(message)}"
                )
                msg = message.reply_to_message or message
                await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
                #await message.delete()
            except Exception as error:
                return await message.reply("Invalid Inline Format", quote=True)
        else:
            msg = message.reply_to_message or message
            await client.copy_message(
                message.chat.id,
                client.me.id,
                note,
                reply_to_message_id=msg.id,
            )
    else:
        msg = message.reply_to_message or message
        await client.copy_message(
            message.chat.id,
            client.me.id,
            note,
            reply_to_message_id=msg.id,
        )


async def get_notes_button(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    get_note_id = await get_note(m._client.me.id, m.text.split()[1])
    note_id = await m._client.get_messages(m._client.me.id, get_note_id)
    buttons, text_button = await notes_create_button(note_id.text)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get notes!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text_button),
                )
            )
        ],
    )


async def delnote_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("What do u purged?", quote=True)
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"{note_name} is Not Exist.", quote=True)
    await rm_note(client.me.id, note_name)
    await message.reply(f"{note_name} Purged!", quote=True)
    await client.delete_messages(client.me.id, [int(note), int(note) + 1])


async def notes_cmd(client, message):
    msg = f"List Notes of {client.me.first_name} {client.me.last_name or ''}\n\n"
    list = await all_notes(client.me.id)
    if list == "None":
        msg += "Empty!!"
    else:
        for notes in list:
            msg += f"~{notes}\n"
    if int(len(str(msg))) > 4096:
        with BytesIO(str.encode(str(msg))) as out_file:
            out_file.name = "notes.txt"
            await message.reply_document(
                document=out_file,
                quote=True
            )
    await message.reply(
        msg,
        quote=True
        )
