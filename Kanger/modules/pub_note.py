from Kanger import *

__MODULE__ = "Notes"
__HELP__ = f"""
• <b>Command:</b> <code>{PREFIX[0]}save</code> [name & reply]
• <b>Function:</b> Save notes, if need inline use type [example | exm_name:https://exp] and reply that!!

• <b>Command:</b> <code>{PREFIX[0]}inl</code> [name & reply]
• <b>Function:</b> Create inline button

• <b>Command:</b> <code>{PREFIX[0]}get</code> [name]
• <b>Function:</b> Get notes

• <b>Command:</b> <code>{PREFIX[0]}clear</code> [name]
• <b>Function:</b> Delete notes

• <b>Command:</b> <code>{PREFIX[0]}notes</code>
• <b>Function:</b> Show list notes
"""

@PY.UBOT("save")
async def _(client, message):
    await addnote_cmd(client, message)

@PY.UBOT("get")
async def _(client, message):
    await get_cmd(client, message)
    
@PY.UBOT("inl")
async def _(client, message):
    await cmd_button(client, message)

@PY.INLINE("^get_button")
@INLINE.QUERY
async def _(client, inline_query):
    await inline_button(client, inline_query)

@PY.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    await get_notes_button(client, inline_query)

@PY.UBOT("clear")
async def _(client, message):
    await delnote_cmd(client, message)

@PY.UBOT("notes")
async def _(client, message):
    await notes_cmd(client, message)

#Handler Logs
#@Client.on_message(
#    is_botlog,
#    filters.private
#    & filters.incoming
#    & ~filters.service
#    & ~filters.me
#    & ~filters.bot
#)
async def _(client, message):
    await pm_log(client, message)
    
#@Client.on_message(
#    is_botlog,
 #   filters.group
  #  & filters.mentioned
  #  & filters.incoming
  #  & ~filters.bot
  #  & ~filters.via_bot
#)
async def _(client, message):
    await log_tagged_messages(client, message)
    
#@PY.UBOT("resetlog")
async def _(client, message):
    await delete_log(client, message)

#@PY.UBOT("setlog")
async def _(client, message):
    await set_log(client, message)

#@PY.UBOT("startlog")
async def _(client, message):
    await mulai_log(client, message)

#@PY.UBOT("stoplog")
async def _(client, message):
    await berhenti_log(client, message)