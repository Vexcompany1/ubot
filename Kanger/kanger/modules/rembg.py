import os
from datetime import datetime
from removebg import RemoveBg

from Kanger import *

IMG_PATH = "downloads/" + "dl_image.jpg"

async def remove_background(client, message):
    if RMBG_API is None:
        await message.reply(
            "Get the API from <a href='https://www.remove.bg/b/background-removal-api'>HERE "
            "</a> & add it to Heroku Config Vars <code>REMOVE_BG_API_KEY</code>",
            disable_web_page_preview=True
            )
        return
    replied = message.reply_to_message
    if (replied and replied.media
            and (replied.photo
                 or (replied.document and "image" in replied.document.mime_type))):
        if os.path.exists(IMG_PATH):
            os.remove(IMG_PATH)
        await client.download_media(message=replied, file_name=IMG_PATH)
        anu = await message.reply("Removing Background Now...")
        # Cooking Image
        try:
            rmbg = RemoveBg(RMBG_API, "removebg_error.log")
            rmbg.remove_background_from_img_file(IMG_PATH)
            rbg_img_path = IMG_PATH + "_no_bg.png"
            await client.send_document(
                chat_id=message.chat.id,
                document=rbg_img_path,
                disable_notification=True,
                )
            await anu.delete()
        except Exception as eds:  # pylint: disable=broad-except
            await anu.edit(f"Something went wrong!\n\n<code>{eds}</code>")
            return
    else:
        await message.reply("Reply to a photo to remove background!")
