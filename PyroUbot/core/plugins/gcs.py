import asyncio
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from PyroUbot import *
from PyroUbot.config import *

async def get_premium_emoji(client, emoji_name):
    emoji_id = await get_vars(client.me.id, emoji_name)
    return emoji_id if emoji_id else "default_premium_emoji_id"

async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats

async def broadcast_group_cmd(client, message):
    emot_proses = await get_premium_emoji(client, "EMOJI_PROSES")

    if client.me.is_premium:
        _broadcast = f"""
<b><emoji id={emot_proses}>⏰</emoji>ᴘʀᴏsᴇs...
"""
    msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>✅ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ɢʀᴏᴜᴘ</b>")

async def broadcast_users_cmd(client, message):
    emot_proses = await get_premium_emoji(client, "EMOJI_PROSES")

    if client.me.is_premium:
        _broadcast = f"""
<b><emoji id={emot_proses}>⏰</emoji>ᴘʀᴏsᴇs...
"""
    msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ...")

    chats = await get_broadcast_id(client, "users")

    done = 0
    for chat_id in chats:
        if chat_id == client.me.id or chat_id in DEVS:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>✅ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀs</b>")

async def broadcast_bot(client, message):
    emot_proses = await get_premium_emoji(client, "EMOJI_PROSES")

    if client.me.is_premium:
        _broadcast = f"""
<b><emoji id={emot_proses}>⏰</emoji>ᴘʀᴏsᴇs...
"""
    msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ...")
        
    susers = await get_list_from_vars(client.me.id, "SAVED_USERS")
    done = 0
    for chat_id in susers:
        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>✅ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀs</b>")

async def send_msg_cmd(client, message):
    emot_send = await get_premium_emoji(client, "EMOJI_SEND")

    if message.reply_to_message
