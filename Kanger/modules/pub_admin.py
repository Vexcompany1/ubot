from Kanger import *

__MODULE__ = "Admin"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}promote</code> reply
• <b>Function:</b> Promote member to admin.

• <b>Command:</b> <code>{PREFIX[0]}fullpromote</code> reply
• <b>Function:</b> Fullpromote member to admin.

• <b>Command:</b> <code>{PREFIX[0]}demote</code> reply
• <b>Function:</b> Demote users from admin.

• <b>Command:</b> <code>{PREFIX[0]}mute</code> [reply/username]
• <b>Function:</b> Mute users in chat.

• <b>Command:</b> <code>{PREFIX[0]}unmute</code> [reply/username]
• <b>Function:</b> Unmute user.

• <b>Command:</b> <code>{PREFIX[0]}ban</code> [reply/username]
• <b>Function:</b> Block users.

• <b>Command:</b> <code>{PREFIX[0]}unban</code> [reply/username]
• <b>Function:</b> Unblock users.

• <b>Command:</b> <code>{PREFIX[0]}kick</code> [reply/username]
• <b>Function:</b> Kicks a user from the group.

• <b>Command:</b> <code>{PREFIX[0]}smute</code> [reply/username]
• <b>Function:</b> Silent Mute users in chat.

• <b>Command:</b> <code>{PREFIX[0]}sunmute</code> [reply/username]
• <b>Function:</b> Silent Unmute user.

• <b>Command:</b> <code>{PREFIX[0]}sban</code> [reply/username]
• <b>Function:</b> Silent Ban users.

• <b>Command:</b> <code>{PREFIX[0]}sunban</code> [reply/username]
• <b>Function:</b> Silent Unblock users.

• <b>Command:</b> <code>{PREFIX[0]}skick</code> [reply/username]
• <b>Function:</b> Silent Kicks a user from the group.

• <b>Command:</b> <code>{PREFIX[0]}staff</code>
• <b>Function:</b> Check admin

• <b>Command:</b> <code>{PREFIX[0]}invite</code> username
• <b>Function:</b> Invite member
"""


@PY.UBOT("kick|ban|mute|unmute|unban")
async def _(client, message):
    await admin_bannen(client, message)
    
@PY.UBOT("skick|sban|smute|sunmute|sunban")
async def _(client, message):
    await admin_sbannen(client, message)
    
@PY.UBOT("staff", FILTERS.ME_GROUP)
async def _(client, message):
    await staff_cmd(client, message)

@PY.UBOT("zombies", FILTERS.ME_GROUP)
async def _(client, message):
    await zombies_cmd(client, message)

@PY.UBOT("invite", FILTERS.ME_GROUP)
async def _(client, message):
    await invite_cmd(client, message)
    
@PY.UBOT("demote", FILTERS.ME_GROUP)
async def _(client, message):
    await demote_command(client, message)
    
@PY.UBOT("promote", FILTERS.ME_GROUP)
async def _(client, message):
    await promote_command(client, message)
    
@PY.UBOT("fullpromote", FILTERS.ME_GROUP)
async def _(client, message):
    await fullpromote_command(client, message)
