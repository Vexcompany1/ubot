from Kanger import *
from uuid import uuid4


@PY.UBOT("help")
async def _(client, message):
    await help_cmd(client, message)


@PY.INLINE("^user_help")
#@INLINE.QUERY
async def _(client, inline_query):
    await menu_inline(client, inline_query)


@PY.CALLBACK("help_(.*?)")
#@INLINE.DATA
async def _(client, callback_query):
    try:
        await menu_callback(client, callback_query)
    except:
        pass
    
@PY.INLINE("^nothi")
#@INLINE.QUERY
async def _(client, inline_query):
    await nothing_here(client, inline_query)
