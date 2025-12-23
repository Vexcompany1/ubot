from Kanger import *


@PY.UBOT("reboot", FILTERS.ME_OWNER)
async def _(client, message):
    await the_reboot(client, message)

@PY.CALLBACK("catconfig")
async def _(client, callback_query):
    await cb_vars_anu(client, callback_query)
    
@PY.UBOT("upgrade", FILTERS.ME_OWNER)
async def _(client, message):
    await the_update(client, message)

@PY.UBOT("stats", FILTERS.ME_OWNER)
async def _(client, message):
    await the_sysinfo(client, message)

@PY.UBOT("sh", FILTERS.ME_OWNER)
@PY.BOT("sh", FILTERS.OWNER)
async def _(client, message):
    await shell_cmd(client, message)

@PY.UBOT("eval", FILTERS.ME_OWNER)
@PY.BOT("eval", FILTERS.ME_OWNER)
async def _(client, message):
    await evalator_cmd(client, message)

@PY.UBOT("inspect")
async def _(client, message):
    await trash_cmd(client, message)

@PY.CALLBACK("cobaae")
async def _(client, callback_query):
    await server_neofetch(client, callback_query)