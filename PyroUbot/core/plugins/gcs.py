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
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
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
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>✅ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀs</b>")

async def broadcast_bot_cmd(client, message):
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
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            done += 1
        except FloodWait as e:
                        await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            else:
                await client.send_message(chat_id, send, reply_markup=f"<emoji id={emot_proses}>⏰</emoji>")
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<b>✅ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ʙᴏᴛs</b>")

# Fungsi untuk mengirim pesan
async def send_msg_cmd(client, message):
    emot_send = await get_premium_emoji(client, "EMOJI_SEND")

    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    # Menggunakan emoji premium pada pesan yang dikirim
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id,
                        reply_markup=f"<emoji id={emot_send}>📬</emoji>"
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                # Menggunakan emoji premium pada pesan yang dikirim
                return await message.reply_to_message.copy(
                    chat_id, reply_markup=f"<emoji id={emot_send}>📬</emoji>"
                )
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            if "_" in chat_id:
                msg_id, to_chat = chat_id.split("_")
                return await client.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                # Menggunakan emoji premium pada pesan yang dikirim
                return await client.send_message(chat_id, chat_text, reply_markup=f"<emoji id={emot_send}>📬</emoji>")
        except Exception as t:
            return await message.reply(f"{t}")

# Fungsi untuk menangani inline query
async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )

