import asyncio

from pyrogram import idle
from pyrogram.errors import RPCError

from Kanger import *


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
    except asyncio.TimeoutError:
        print(f"Restarting ({user_id})")
        for X in ubot._ubot:
            if user_id == X.me.id:
                for _ubot_ in await get_userbots():
                    if X.me.id == int(_ubot_["name"]):
                        try:
                            ubot._ubot.remove(X)
                            UB = Ubot(**_ubot_)
                            await UB.start()
                            for mod in loadModule():
                                importlib.reload(
                                    importlib.import_module(f"Kanger.modules.{mod}")
                                )
                        except:
                            return
    except RPCError:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await rem_pref(user_id)
        await rem_expired_date(user_id)
        await bot.send_message(user_id, "Your userbot has removed session!!")
        buttons = [
            [
                InlineKeyboardButton("Check User", user_id=f"{user_id}")
                ],
                ]
        await bot.send_message(LOGS_MAKER_UBOT, f"<a href=tg://openmessage?user_id={user_id}>kanger Client</a> Has Removed Session!", reply_markup=InlineKeyboardMarkup(buttons))
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"{user_id} Successfully removed")


async def test():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())


async def main():
    await test()
    try:
        await loadPlugins()
        await expiredUserbots()
        if "test" not in sys.argv:
            await bot.idle()
    except KeyboardInterrupt:
        logger.warning("BOT STOP....")
    finally:
        await bot.stop()
        
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
    
