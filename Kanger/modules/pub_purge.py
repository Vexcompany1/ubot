from Kanger import *

__MODULE__ = "Purge"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}antipm</code>
• <b>Function:</b> Auto delete history chat from user if not contact | use: {PREFIX[0]}antipm on/off

• <b>Command:</b> <code>{PREFIX[0]}del</code> Reply
• <b>Function:</b> Just Delete

• <b>Command:</b> <code>{PREFIX[0]}purge</code> Reply
• <b>Function:</b> Just Purge

• <b>Command:</b> <code>{PREFIX[0]}purgeme</code> Count
• <b>Function:</b> Just Purge your own message
"""

@PY.UBOT("antipm")
async def _(client, message):
    await set_antipm(client, message)
    
@ubot.on_message(
    ~filters.me
    & ~filters.bot
    & filters.private
    & is_antipm
    )
async def _(client, message):
    await antipm_er(client, message)

@PY.UBOT("del")
async def _(client, message):
    await del_cmd(client, message)

@PY.UBOT("purgeme", FILTERS.GROUP)
async def _(client, message):
    await purgeme_cmd(client, message)

@PY.UBOT("purge")
async def _(client, message):
    await purge_cmd(client, message)
