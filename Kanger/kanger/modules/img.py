import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from Kanger import *

async def blur_cmd(client, message):
    ureply = message.reply_to_message
    if not ureply:
        return await message.reply("Need Reply to Image.")
    yinsxd = await client.download_media(ureply, "./downloads/")
    if yinsxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", yinsxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(yinsxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(yinsxd)


async def negative_cmd(client, message):
    ureply = message.reply_to_message
    if not ureply:
        return await message.reply("Meed Reply to Image.")
    ayiinxd = await client.download_media(ureply, "./downloads/")
    if ayiinxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiinxd)


async def miror_cmd(client, message):
    ureply = message.reply_to_message
    if not ureply:
        return await kentu.edit("Need Reply to Image.")
    xnxx = await client.download_media(ureply, "./downloads/")
    if xnxx.endswith(".tgs"):
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)
