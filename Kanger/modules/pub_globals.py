from Kanger import *

__MODULE__ = "Global"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}gban</code> reply/tag, reason
• <b>Function:</b> Mass banned user from all group and channel (if you admin)

• <b>Command:</b> <code>{PREFIX[0]}ungban</code> 
• <b>Function:</b> Just mass unban user

• <b>Command:</b> <code>{PREFIX[0]}sgban</code> reply/tag, reason
• <b>Function:</b> Mass silent banned user from all group and channel (if you admin)

• <b>Command:</b> <code>{PREFIX[0]}sungban</code> 
• <b>Function:</b> Just mass silent unban user 

• <b>Command:</b> <code>{PREFIX[0]}gcast</code> [reply to a message or type something]
• <b>Function:</b> Send broadcast messages to all groups.

• <b>Command:</b> <code>{PREFIX[0]}gcastall</code> [reply to a message or type something]
• <b>Function:</b> Send broadcast messages to all including groups, users, channels (if admin).

• <b>Command:</b> <code>{PREFIX[0]}kickme</code>
• <b>Function:</b> Leave the current group.

• <b>Command:</b> <code>{PREFIX[0]}leaveallgc</code>
• <b>Function:</b> Leave all the groups you have joined. 

• <b>Command:</b> <code>{PREFIX[0]}leaveallch</code>
• <b>Function:</b> Leave all the channels you have joined. 

• <b>Command:</b> <code>{PREFIX[0]}join</code> [username]
• <b>Function:</b> Join group chat with username.
"""


@PY.UBOT("gban|ungban")
async def _(client, message):
    await global_banned(client, message)
    
@PY.UBOT("sgban|sungban")
async def _(client, message):
    await global_sbanned(client, message)
    
@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)

@PY.UBOT("gcastall")
async def _(client, message):
    await broadcast_users_cmd(client, message)

#@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)

@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)

@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)

@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
async def _(client, message):
    await leave(client, message)

@PY.UBOT("join")
async def _(client, message):
    await join(client, message)

@PY.UBOT("leaveallgc")
async def _(client, message):
    await kickmeall(client, message)

@PY.UBOT("leaveallch")
async def _(client, message):
    await kickmeallch(client, message)