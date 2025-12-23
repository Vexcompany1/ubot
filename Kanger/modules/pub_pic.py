from Kanger import *

__MODULE__ = "Pic"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}removebg</code> Reply
• <b>Function:</b> Remove backgruond

• <b>Command:</b> <code>{PREFIX[0]}blur</code> Reply
• <b>Function:</b> Blured photo

• <b>Command:</b> <code>{PREFIX[0]}negative</code> Reply
• <b>Function:</b> Negatived photo

• <b>Command:</b> <code>{PREFIX[0]}mirror</code> Reply
• <b>Function:</b> Just mirroring pic
"""


@PY.UBOT("removebg")
async def _(client, message):
    await remove_background(client, message)


@PY.UBOT("blur")
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative")
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("mirror")
async def _(client, message):
    await miror_cmd(client, message)
