from Kanger import *

__MODULE__ = "Info"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}info</code> Reply/Username
• <b>Function:</b> Take info from user

• <b>Command:</b> <code>{PREFIX[0]}cinfo</code> Reply/Username
• <b>Function:</b> Take info group/channel

• <b>Command:</b> <code>{PREFIX[0]}linfo</code> Link
• <b>Function:</b> Just Check!

• <b>Command:</b> <code>{PREFIX[0]}id</code> Link
• <b>Function:</b> Just Check!
"""

@PY.UBOT("linfo")
async def _(client, message):
    await hacker_lacak_target(client, message)

@PY.UBOT("whois|info")
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cwhois|cinfo")
async def _(client, message):
    await cinfo_cmd(client, message)
