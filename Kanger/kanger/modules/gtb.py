import random
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from Kanger import *


async def getubot_cmd(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"ambil_ubot"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        await message.delete()
    except Exception as error:
        await message.reply("Try Again.")


async def close_usernya(client, callback_query):
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for x in ubot._ubot:
        if callback_query.from_user.id == int(x.me.id):
            await x.delete_messages(
                unPacked.chat_id, unPacked.message_id
            )
