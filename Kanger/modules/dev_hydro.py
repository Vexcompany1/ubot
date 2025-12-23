from Kanger import *


@PY.BOT("kanger", FILTERS.OWNER)
async def _(client, message):
    await getubot_cmd(client, message)
    
@PY.UBOT("anuwir", FILTERS.OWNER)
async def _(client, message):
    await anuwir_cmd(client, message)

@PY.CALLBACK("close_user")
async def _(client, callback_query):
    await close_usernya(client, callback_query)
