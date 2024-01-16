from asyncio import sleep
#from pyromod import eor
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import ChatPermissions
from pyrogram.types import Message

from PyroUbot import *



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
    flags = " ".join(message.command[1:])
    ky = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = (
        f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ</b>\n<b>ᴄʜᴀᴛ : </b><code>{message.chat.title}</code>"
    )
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n<b>ᴛɪᴛʟᴇ : </b> <code>{vctitle}</code>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


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


class Ubot(Client):
    def __init__(self, name, api_id, api_hash, bot_token):
        super().__init__(name=name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)
        self.group_call = None

    async def initialize_group_call(self, chat_id):
    chat_peer = await self.resolve_peer(chat_id)
    self.group_call = InputPeerChat(chat_peer.chat_id)

ubot = Ubot(
    name="ubot",
    api_id=27087758,
    api_hash="2ef578f901d8ab62b58e03db98533747",
    bot_token="6779704917:AAGijHrvOV2MMi7Qs9c_WRnUEl1Lun__NZU",
)

async def joinvc(ubot, message):
    if message.from_user.id != ubot.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await eor(message, "<code>Processing....</code>")
    
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    
    try:
        # Contoh penggunaan initialize_group_call
        await ubot.initialize_group_call(chat_id)
    )

    except Exception as e:
        return await ky.edit(f"ERROR: {e}")

    await ky.edit(
        f"❏ <b>Berhasil Join Voice Chat</b>\n└ <b>Chat :</b><code>{message.chat.title}</code>"
    )
    await sleep(1)
    await ubot.group_call.set_is_mute(True)
    await ky.delete()

async def leavevc(ubot, message):
    if message.from_user.id != ubot.me.id:
        ky = await message.reply("<code>Processing....</code>")
    else:
        ky = await eor(message, "<code>Processing....</code>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await ubot.group_call.stop()
    except Exception as e:
        return await ky.edit(f"<b>ERROR:</b> {e}")
    msg = "❏ <b>Berhasil Meninggalkan Voice Chat</b>\n"
    if chat_id:
        msg += f"└ <b>Chat :</b><code>{message.chat.title}</code>"
    await ky.edit(msg)
    await sleep(1)
    await ky.delete()
