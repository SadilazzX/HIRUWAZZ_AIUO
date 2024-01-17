import asyncio
import os
import random
from random import choice

from PyroUbot import *
from pyrogram import enums, filters
from pyrogram.enums import MessagesFilter

async def cari_asupan(client, message):
    y = await message.reply("<b>🔍 Mencari Video Asupan...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(
            message.chat.id,
            caption=f"<b>Asupan By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>")

async def cari_ayang(client, message, channel):
    y = await message.reply(f"<b>🔍 Mencari Ayang di {channel}...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            channel, filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(
            message.chat.id,
            caption=f"<b>Ayang By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit(f"<b>Ayang di {channel} tidak ditemukan silahkan ulangi beberapa saat lagi</b>")

async def cari_bokep(client, message):
    if message.chat.id in BLACKLIST_CHAT:
        return await message.reply("<b>Maaf perintah ini dilarang di sini</b>")
    y = await message.reply("<b>🔍 Mencari Video Bokep...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except BaseException:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(
            message.chat.id,
            caption=f"<b>Bokep By <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
            reply_to_message_id=message.id,
        )
        await y.delete()
    except Exception:
        await y.edit("<b>Video tidak ditemukan silahkan ulangi beberapa saat lagi</b>")
    if client.me.id == 1898065191:
        return
    await client.leave_chat(-1001867672427)

async def cari_anime(client, message, channel):
    iis = await message.reply("🔎 <code>Search Anime...</code>")
    try:
        # ...
    finally:
        await iis.delete()

async def cari_nimek(client, message):
    erna = await message.reply("🔎 <code>Search Anime...</code>")
    try:
        # ...
    finally:
        await erna.delete()

async def cari_sange_ah(client, message):
    kazu = await message.reply("🔎 <code>Nih PAP Nya...</code>")
    try:
        # ...
    finally:
        await kazu.delete()
