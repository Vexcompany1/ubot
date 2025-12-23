import re

from pyrogram.types import *

from Kanger import *


async def help_cmd(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
            #await message.delete()
        except Exception as error:
            await message.reply("Try Again")
    else:
        module = get_arg(message)
        if get_arg(message) in HELP_COMMANDS:
            await message.edit(
                HELP_COMMANDS[get_arg(message)].__HELP__,
            )
        else:
            await message.edit(
                f"<b>No Module Named <code>{module}</code></b>"
            )


async def menu_inline(client, inline_query):
    msg = f"""
<b>Command & Help</b>"""
    await client.answer_inline_query(
        inline_query.id,
        cache_time=60,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, HELP_COMMANDS, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


async def menu_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    top_text = f"""
<b>Command & Help</b>"""
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = HELP_COMMANDS[module].__HELP__
        button = [[InlineKeyboardButton("Back", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )

async def nothing_here(_, inline_query: InlineQuery):
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="About KangerBot",
            input_message_content=InputTextMessageContent("""
👾<b>KangerBot</b>

Simple userbot telegram based in pyrogram.
• Send messages to all groups/users simultaneously
• Set a scheduled/reminder message
• Manage and moderate the group
• Respond to orders
...And many more!
"""
            ),
            url="https://t.me/Kangerbot",
            description="Click this to see",
            thumb_url="https://telegra.ph//file/3838aa50510fd5020c2b3.jpg",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Deploy kangerBot",
                            url="https://t.me/Kangerbot?start"
                        ),
                        InlineKeyboardButton(
                            "Update Channel",
                            url="https://t.me/Kanger"
                        )
                    ]
                ]
            )
        )
    ]