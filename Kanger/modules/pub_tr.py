from Kanger import *

#__MODULE__ = "Translator"
#__HELP__ = 
f"""
• <b>Command:</b> <code>{PREFIX[0]}tts</code> Text
• <b>Function:</b> Text to speech

• <b>Command:</b> <code>{PREFIX[0]}tr</code> Reply or Text
• <b>Function:</b> Translate

• <b>Command:</b> <code>{PREFIX[0]}setlang</code>
• <b>Function:</b> Change Language
"""


#@PY.UBOT("tts")
async def _(client, message):
    await tts_cmd(client, message)


#@PY.UBOT("tr|tl")
async def _(client, message):
    await tr_cmd(client, message)


#@PY.UBOT("setlang")
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
