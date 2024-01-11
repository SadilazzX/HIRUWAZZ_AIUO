from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
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
        msg += f"<b>ᴄʜᴀᴛ : </b><code>{message.chat.title}</code>"
    await ky.edit(msg)


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"

async def join_vc(client, message):
    await edit_or_reply(message, f"**Processing....**")
    if len(message.text.split()) > 1:
        chat = message.chat.id
        chats = message.text.split(" ", 1)[1]
        try:
            chat = await client.get_chat(ngentod(chats))
        except asu as e:
            await call_py.leave_group_call(chat)
            clear_queue(chat)
            await asyncio.sleep(3)
            return await edit_delete(message, f"**ERROR:** `{e}`", 30)
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return await edit_or_reply(message, "NodeJs is not installed or installed version is too old.")
    else:
        chat_id = message.chat.id
        chats = message.text.split(" ", 1)[1]
        vcmention(message.from_user)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat_id,
        kartod('http://duramecho.com/Misc/SilentCd/Silence01s.mp3'),
        chats,
        stream_type=ya().pulse_stream,
    )
    await edit_delete(message, f"**Successfully Joined OS Jamet.**\n**ID:{chat_id}**", 5)

async def leave_vc(client, message):
    """ leave video chat """
    await edit_or_reply(message, "**Processing....**")
    chat_id = message.chat.id
    from_user = vcmention(message.from_user)
    if from_user:
        try:
            await client.raw(functions.phone.LeaveGroupCall(
                call=await client.raw(functions.phone.Call(
                    users=await client.resolve_peer(chat_id),
                    video=True,
                )),
            ))
        except (memek, ajg):
            await edit_or_reply(message, f"Woy {from_user}, Kontol Kau Ga Ada Di OS")
        await edit_delete(message, f"**In OS, Many Jamets, {from_user} Wants to Get Down Hahaha **", 2)
