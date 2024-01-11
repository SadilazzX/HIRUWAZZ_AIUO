from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

# Asumsikan VoiceChat adalah kelas yang memiliki metode start dan stop
class VoiceChat:
    async def start(self, chat_id):
        # Implementasi metode start
        pass
    
    async def stop(self):
        # Implementasi metode stop
        pass

# Asumsikan Ubot adalah kelas turunan dari Client
class Ubot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vc = VoiceChat()

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"ɴᴏ ɢʀᴏᴜᴘ ᴄᴀʟʟ ꜰᴏᴜɴᴅ {err_msg}")
    return False

async def start_vctools(client, message):
    # (Kode sebelumnya)

async def stop_vctools(client, message):
    ky = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", ᴋᴇꜱᴀʟᴀʜᴀɴ..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴀᴋʜɪʀɪ</b>\n<b>ᴄʜᴀᴛ : </b><code>{message.chat.title}</code>"
    )

async def join_os(client, message):
    kk = message.from_user.id
    ky = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.vc.start(chat_id)

    except Exception as e:
        return await ky.edit(f"ERROR: {e}")
    await ky.edit(
        f"<b>ʙᴇʀʜᴀꜱɪʟ ᴊᴏɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n<b>ᴄʜᴀᴛ : </b><code>{message.chat.title}</code>"
    )
    await client.vc.set_is_mute(True)

async def turun_os(client, message):
    ky = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
      
        await client.vc.stop()

    except Exception as e:
        return await ky.edit(f"<b>ERROR:</b> {e}")
    msg = "<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n"
    if chat_id:
        msg += f"<b>
