from Kanger import *

__MODULE__ = "Blacklist"
__HELP__ = f"""
• <b>Command:</b> <code>addbl</code>
• <b>Function:</b> Adding a group to the blacklist.

• <b>Command:</b> <code>rmbl</code>
• <b>Function:</b> Remove group from blacklist.

• <b>Command:</b> <code>rmallbl</code>
• <b>Function:</b> Removes all groups from the blacklist.

• <b>Command:</b> <code>lsbl</code>
• <b>Function:</b> Displays a list of groups that are on the blacklist.
"""


@PY.UBOT("addbl", FILTERS.ME_GROUP)
async def _(client, message):
    await add_blaclist(client, message)


@PY.UBOT("rmbl", FILTERS.ME_GROUP)
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rmallbl")
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("lsbl")
async def _(client, message):
    await get_blacklist(client, message)
