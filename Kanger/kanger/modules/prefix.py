from Kanger import *


async def setprefix(client, message):
    if len(message.command) < 2:
        return await message.reply(f"Input New Prefix.", quote=True)
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
            return await message.reply(f"<b>Prefix set to: {parsed_prefix}</b>", quote=True)
        except:
            return
