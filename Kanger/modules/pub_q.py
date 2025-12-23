from Kanger import *


@PY.UBOT("genqr")
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("readqr")
async def _(client, message):
    await qr_read_cmd(client, message)
