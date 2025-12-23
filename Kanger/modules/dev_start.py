from .. import *

@PY.UBOT("ping")
@PY.UBOT("p")
async def _(client, message):
    await ping_cmd(client, message)

@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
 
@PY.CALLBACK("mboh")
async def _(client, callback_query):
    await get_setarted(client, callback_query)
  
@PY.BOT("login", FILTERS.OWNER)
async def _(client, message):
    await login_cmd(client, message)
    
@PY.UBOT("lhowir", FILTERS.OWNER)
async def _(client, message):
    await menjawir(client, message)

@PY.BOT("reload", FILTERS.PRIVATE)
@PY.BOT("reload", FILTERS.GROUP)
async def _(client, message):
    await restart_cmd(client, message)