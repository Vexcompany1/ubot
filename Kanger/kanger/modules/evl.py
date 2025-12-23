import asyncio
import os
import platform
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from subprocess import Popen, PIPE, TimeoutExpired
from time import perf_counter
from meval import meval

import psutil

from Kanger import *

async def cb_vars_anu(client, callback_query):
    user_id = callback_query.from_user.id
    cmd_text = "cat Kanger/config.py"
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )
    text = f"<code>Vars Bot:</code>\n\n"
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "Timeout expired!"
    
    if stdout:
        text += f"<code>{stdout}</code>"
    if stderr:
        text += f"<code>{stderr}</code>"
    
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"home {user_id}")],
        ]
    await callback_query.edit_message_text(
        f"{text}",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        )
    cmd_obj.kill()
    
    
    
async def cb_restart(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"home {user_id}")],
        ]
    await callback_query.edit_message_text(
        f"""
<b>Restarting....</b>
<b>Slow and calm.</b>
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        )
    os.execl(sys.executable, sys.executable, "-m", "Kanger")
  
  
async def cb_gitpull(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"home {user_id}")],
        ]
    await callback_query.edit_message_text(
        f"""
<b>Updating......</b>
<b>Slow and calm.</b>
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        )
    os.system("git pull")
    os.execl(sys.executable, sys.executable, "-m", "Kanger")

async def the_reboot(client, message):
    await message.delete()
    os.execl(sys.executable, sys.executable, "-m", "Kanger")
    
async def the_update(client, message):
    await message.delete()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, "-m", "Kanger")

async def shell_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "Input text!",
            quote=True
            )
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "<b>Kanger#</b>" if os.getuid() == 0 else "<b>Kanger$</b>"
    text = f"{char} <code>{cmd_text}</code>\n\n"

    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "Timeout expired!"
    else:
        stop_time = perf_counter()
        if len(stdout) > 4096:
            anuk = await message.reply(
                "Oversize, sending file...",
                quote=True
                )
            file = open("output.txt", "w+")
            file.write(stdout)
            file.close()
            await client.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.id,
                )
            await anuk.delete()
            os.remove("output.txt")
        else:
            text += f"<code>{stdout}</code>"
        if stderr:
            text += f"<code>{stderr}</code>"
    await message.reply(
        text,
        quote=True
        )
    cmd_obj.kill()


async def evalator_cmd(client, message):
    if not get_arg(message):
        return await message.reply("<b>Need Text!</b>",
        quote=True
        )
    code = message.text.split(maxsplit=1)[1]
    eval_vars = {
        "client": client,
        "message": message,
        "replied": message.reply_to_message,
    }
    try:
        output = await meval(code, globals(), **eval_vars)
        output = str(output)
        result = f"<pre language=python>{code}</pre>" \
                 "\n\nOutput:\n" \
                 f"<code>{output}</code>" 
        if len(result) > 4096:
            with open(
                "output.txt",
                "w",
                encoding="utf-8"
            ) as output_file:
                output_file.write(output)
            await message.reply_document("output.txt")
            os.remove("output.txt")
        else:
            await message.reply(
                result,
                quote=True
                )
    
    except Exception as e:
        await message.reply(
            f"<code>{code}</code>" \
            "\n\n" \
            f"<code>{e}</code>")
    


async def trash_cmd(client, message):
    if message.reply_to_message:
        msg_id = message.reply_to_message.id
    else:
        msg_id = message.id
    try:
        msgs = await client.get_messages(message.chat.id, msg_id)
        if len(str(msgs)) > 4096:
            with BytesIO(str.encode(str(msgs))) as out_file:
                out_file.name = "inspect.txt"
                return await message.reply_document(document=out_file)
        else:
            return await message.reply(msgs)
    except Exception as error:
        return await message.reply(str(error))