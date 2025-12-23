from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from Kanger import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} Month",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "Get Profile", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "Unaccept Payment", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if not message.from_user.id == OWNER_ID:
            button = [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/KangerSupport"
                    ),
                    InlineKeyboardButton("Channel", url="https://t.me/Kanger"),
                ],
                [
                    InlineKeyboardButton("Get Started", callback_data="mboh")
                    ],
            ]
        else:
            button = [
                [
                    InlineKeyboardButton("Get Started", callback_data="mboh"),
                    ],
                [
                    InlineKeyboardButton("kanger People", callback_data="next_ub 1"),
                    ],
                [
                    InlineKeyboardButton("Show Vars", callback_data="catconfig"),
                    ],
                [
                    InlineKeyboardButton("Reboot", callback_data="restart"),
                    ],
                [
                    InlineKeyboardButton("Upgrade", callback_data="gitpull"),
                    ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [InlineKeyboardButton("Owner", user_id=OWNER_ID)],
            [InlineKeyboardButton("Back", callback_data="mboh")],
        ]
        return button
      
    def userbot(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Clear from celestia",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Vaporize",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton("Prev", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("Home", callback_data=f"home {user_id}"),
                InlineKeyboardButton("Next", callback_data=f"next_ub {int(count)}"),
            ],
        ]
        return button

    def ambil_akun(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Clear From Celestia",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Vaporize",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton("Next", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("Prev", callback_data=f"next_ub {int(count)}"),
            ],  
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"@{bot.me.username} You haven't ordered",
                                input_message_content=InputTextMessageContent(
                                    f"Order first to use this bot"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"Order first to use this bot",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("Errors")

        return wrapper


async def create_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    msg = []
    if "|" not in m.text.split(None, 1)[1]:
        for X in m.text.split(None, 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
            msg.append(X_parts[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = " ".join(msg)
    else:
        for X in m.text.split("|", 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
        buttons.add(*keyboard)
        text = m.text.split("|", 1)[0].split(None, 1)[1]

    return buttons, text


async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = m.text.split("|", 1)
    for X in split_text[1].split():
        button_data = X.split(":", 1)
        button_label = button_data[0].replace("_", " ")
        button_url = button_data[1]
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0].split(None, 1)[1]
    return buttons, text_button


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("|", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button
