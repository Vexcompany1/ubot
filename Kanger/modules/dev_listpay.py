from Kanger import *

@PY.CALLBACK("ini_list")
async def _(client, callback_query):
    await ini_list_pay(client, callback_query)

@PY.CALLBACK("ini_jago")
async def _(client, callback_query):
    await ini_jago_pay(client, callback_query)

@PY.CALLBACK("ini_dana")
async def _(client, callback_query):
    await ini_dana_pay(client, callback_query)