from Kanger import *

__MODULE__ = "Fun"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}mms</code> Text
• <b>Function:</b> Make memes from pic/sticker

• <b>Command:</b> <code>{PREFIX[0]}mmf</code> Reply
• <b>Function:</b> Write pic/sticker with text

• <b>Command:</b> <code>{PREFIX[0]}spam</code> Text
• <b>Function:</b> Spam || {PREFIX[0]}spam count, text/reply

• <b>Command:</b> <code>{PREFIX[0]}dspam</code> Reply
• <b>Function:</b> Delay spam || {PREFIX[0]}dspam count, delay, text/reply

• <b>Command:</b> <code>{PREFIX[0]}q</code> Reply
• <b>Function:</b> Create quote sticker

• <b>Command:</b> <code>{PREFIX[0]}sg</code> reply
• <b>Function:</b> Chect history name and username

• <b>Command:</b> <code>{PREFIX[0]}whisper</code> Reply and Text
• <b>Function:</b> Whisper to user

• <b>Command:</b> <code>{PREFIX[0]}mdl</code> Link
• <b>Function:</b> Download media from Facebook, Instagram, etc.

• <b>Command:</b> <code>{PREFIX[0]}tgph</code> Reply media
• <b>Function:</b> Upload to telegraph

• <b>Command:</b> <code>{PREFIX[0]}ytdla</code> Text
• <b>Function:</b> Download youtube audio

• <b>Command:</b> <code>{PREFIX[0]}ytdlv</code> Text
• <b>Function:</b> Download youtube video
"""

#@PY.UBOT("kang")
async def _(client, message):
    await kang_(client, message)
    
#@PY.UBOT("strinfo")
async def _(client, message):
    await sticker_pack_info_(client, message)
    
@PY.UBOT("mms|memes")
async def _(client, message):
    await memes_cmd(client, message)
    
@PY.UBOT("mmf|memify")
async def _(client, message):
    await memify_cmd(client, message)
    
@PY.UBOT("q")
async def _(client, message):
    await quotly_cmd(client, message)
    
@PY.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message)
    
@PY.UBOT("whisper")
async def _(client, message):
    await msg_cmd(client, message)

@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
    
@PY.UBOT("mdl")
async def _(client, message):
    await sosmed_cmd(client, message)
    
@PY.UBOT("spam|dspam")
async def _(client, message):
    if message.command[0] == "spam":
        await spam_cmd(client, message)
    if message.command[0] == "dspam":
        await dspam_cmd(client, message)


#@PY.UBOT("ocr")
async def _(client, message):
    await read_cmd(client, message)
    
@PY.UBOT("tiny")
async def _(client, message):
    await tiny_cmd(client, message)

@PY.UBOT("tgph")
async def _(client, message):
    await tg_cmd(client, message)
    
@PY.UBOT("ytdlv")
async def _(client, message):
    await vsong_cmd(client, message)

@PY.UBOT("ytdla")
async def _(client, message):
    await song_cmd(client, message)
    