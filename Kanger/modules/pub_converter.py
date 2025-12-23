from Kanger import *

__MODULE__ = "Converter"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}toimg</code> Reply
• <b>Function:</b> Convert to image

• <b>Command:</b> <code>{PREFIX[0]}tosticker</code> Reply
• <b>Function:</b> Convert to sticker

• <b>Command:</b> <code>{PREFIX[0]}togif</code> Reply
• <b>Function:</b> Convert to GIF

• <b>Command:</b> <code>{PREFIX[0]}toaudio</code> Reply
• <b>Function:</b> Convert to audio

• <b>Command:</b> <code>{PREFIX[0]}steal</code> Reply
• <b>Function:</b> Steal media
"""

@PY.UBOT("toimg")
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker")
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif")
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio")
async def _(client, message):
    await convert_audio(client, message)


#@PY.UBOT("efek")
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("steal")
async def _(client, message):
    await colong_cmn(client, message)

#@PY.UBOT("font")
async def _(client, message):
    await font_message(client, message)


@PY.INLINE("^get_font")
@INLINE.QUERY
async def _(client, inline_query):
    await font_inline(client, inline_query)


@PY.CALLBACK("^get")
@INLINE.DATA
async def _(client, callback_query):
    await font_callback(client, callback_query)


@PY.CALLBACK("^next")
@INLINE.DATA
async def _(client, callback_query):
    await font_next(client, callback_query)


@PY.CALLBACK("^prev")
@INLINE.DATA
async def _(client, callback_query):
    await font_prev(client, callback_query)
