from Kanger import *

__MODULE__ = "Misc"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}limit</code>
• <b>Function:</b> Check limit spambot

• <b>Command:</b> <code>{PREFIX[0]}setname</code> Text
• <b>Function:</b> Change name

• <b>Command:</b> <code>{PREFIX[0]}setbio</code> Text
• <b>Function:</b> Change bio

• <b>Command:</b> <code>{PREFIX[0]}block</code> Reply
• <b>Function:</b> Block user

• <b>Command:</b> <code>{PREFIX[0]}unblock</code> Reply
• <b>Function:</b> Unblock user

• <b>Command:</b> <code>{PREFIX[0]}carbon</code> Text
• <b>Function:</b> Generate a Carbon

• <b>Command:</b> <code>{PREFIX[0]}setprefix</code> Code
• <b>Function:</b> Just change prefix

• <b>Command:</b> <code>{PREFIX[0]}copy</code> Link
• <b>Function:</b> Leech media from restrict Group/Channel

• <b>Command:</b> <code>{PREFIX[0]}tagall</code> Reply
• <b>Function:</b> Just tag all member

• <b>Command:</b> <code>{PREFIX[0]}abort</code>
• <b>Function:</b> Abort tagall

• <b>Command:</b> <code>{PREFIX[0]}afk</code>
• <b>Function:</b> Just afk

• <b>Command:</b> <code>{PREFIX[0]}unafk</code>
• <b>Function:</b> Just unafk

• <b>Command:</b> <code>{PREFIX[0]}startvc</code>
• <b>Function:</b> Start Video Chat at Group

• <b>Command:</b> <code>{PREFIX[0]}stopvc</code>
• <b>Function:</b> Stop Video Chat at Group
"""

@PY.UBOT("startvc")
async def _(client, message):
    await joinvc(client, message)
    
@PY.UBOT("stopvc")
async def _(client, message):
    await stop_vctools(client, message)

@PY.UBOT("afk")
async def _(client, message):
    await set_afk(client, message)
    
@PY.UBOT("unafk")
async def _(client, message):
    await no_afke(client, message)
    
    
@ubot.on_message(
    is_afk
    & filters.mentioned
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def _(client, message):
    await afk_er(client, message)
    
    
@ubot.on_message(filters.outgoing & filters.me & is_afk)
async def _(client, message):
    await now_afke(client, message)

@PY.UBOT("limit")
async def _(client, message):
    await limit_cmd(client, message)

@PY.UBOT("setbio")
async def _(client, message):
    await set_bio(client, message)


@PY.UBOT("setname")
async def _(client, message):
    await setname(client, message)


@PY.UBOT("block")
async def _(client, message):
    await block_user_func(client, message)

@PY.UBOT("unblock")
async def _(client, message):
    await unblock_user_func(client, message)
    
@PY.UBOT("carbon")
async def _(client, message):
    await carbon_func(client, message)

@PY.UBOT("setprefix")
@PY.UBOT("sp")
async def _(client, message):
    await setprefix(client, message)
    
@PY.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)
    
@PY.UBOT("copy")
async def _(client, message):
    await copy_ubot_msg(client, message)

@PY.UBOT("tagall|abort")
async def _(client, message):
    await tagall_batal_cmd(client, message)