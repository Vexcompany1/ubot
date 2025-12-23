from Kanger import *


@PY.BOT("add", FILTERS.GROUP)
@PY.UBOT("add")
async def _(client, message):
    await prem_user(client, message)

@PY.BOT("user")
async def _(client, message):
    await user_cek(client, message)

@PY.BOT("rm", FILTERS.OWNER)
@PY.UBOT("rm", FILTERS.ME_USER)
async def _(client, message):
    await unprem_user(client, message)

@PY.BOT("getadd", FILTERS.OWNER)
@PY.UBOT("getadd", FILTERS.ME_OWNER)
async def _(cliebt, message):
    await get_prem_user(client, message)

@PY.BOT("archon", FILTERS.OWNER)
@PY.UBOT("archon", FILTERS.ME_USER)
async def _(client, message):
    await seles_user(client, message)

@PY.BOT("rmarchon", FILTERS.OWNER)
@PY.UBOT("rmarchon", FILTERS.ME_USER)
async def _(client, message):
    await unseles_user(client, message)

@PY.BOT("getarchon", FILTERS.OWNER)
@PY.UBOT("getarchon", FILTERS.ME_OWNER)
async def _(client, message):
    await get_seles_user(client, message)

@PY.BOT("addxp", FILTERS.OWNER)
@PY.UBOT("addxp", FILTERS.ME_USER)
async def _(client, message):
    await expired_add(client, message)

@PY.BOT("inf", FILTERS.OWNER)
@PY.UBOT("inf", FILTERS.ME_USER)
async def _(client, message):
    await expired_cek(client, message)

@PY.BOT("unxp", FILTERS.OWNER)
@PY.UBOT("unxp", FILTERS.ME_OWNER)
async def _(client, message):
    await un_expired(client, message)

@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)

@PY.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)
