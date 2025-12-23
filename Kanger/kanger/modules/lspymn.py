from Kanger import *

async def ini_list_pay(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("DANA", callback_data="ini_dana"),
            ],
        [
            InlineKeyboardButton("JAGO", callback_data="ini_jago"),
            ],
        [
            InlineKeyboardButton("Back", callback_data="tuku_prem")]
            ]
    await callback_query.message.edit(
        "<b>Switch your payment method\n\nAfter pay please send invoice to owner to activate.</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
        )

async def ini_dana_pay(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("Back", callback_data="ini_list"),
            ],
            ]
    await callback_query.message.edit(
        "<b>DANA</b>\n\n<code>081912414328</code> H/N Mu**ad Da**id Fi**ah\n\nNote: After pay please send invoice to owner to activate.",
        reply_markup=InlineKeyboardMarkup(buttons),
        )

async def ini_jago_pay(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("Back", callback_data="ini_list"),
            ],
            ]
    await callback_query.message.edit(
        "<b>JAGO</b>\n\n<code>108769648096</code> H/N Mu**ad Da**id Fi**ah\n\nNote: After pay please send invoice to owner to activate.",
        reply_markup=InlineKeyboardMarkup(buttons),
        )