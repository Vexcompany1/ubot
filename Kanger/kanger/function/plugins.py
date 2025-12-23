from importlib import import_module
from platform import python_version

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Kanger import bot, ubot
from Kanger.config import OWNER_ID, DUMP_LOGS
from Kanger.kanger.utils import PY
from Kanger.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"Kanger.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDS[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    print(f"Successfully Activated!!")
    TM = await bot.send_message(
        DUMP_LOGS,
        f"""
<b>Bot Activated!</b>

<b>Total Modules: {len(HELP_COMMANDS)}</b>
<b>Python Version: {python_version()}</b>
<b>Pyrogram Version: {__version__}</b>

<b>Kanger Total: {len(ubot._ubot)}</b>
"""
)
    

@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
