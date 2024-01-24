import logging
import os
import re
from aiohttp import ClientSession
from typing import Any, Dict
from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pyromod import listen
from pytgcalls import GroupCallFactory
from PyroUbot.config import *

# Kelas ConnectionHandler dan set konfigurasi logger
class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSErro", "TimeoutError"]:
            if X in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

# Daftar Chat yang di-blacklist
BLACKLIST_CHAT = [
    -1001599474353,
    -1001692751821,
    # ... (daftar chat lainnya)
]

# Inisialisasi ClientSession untuk aiohttp
aiosession = ClientSession()

# Objek dict contoh
custom_dict = {
    "welcome_message": "Selamat datang di bot kami!",
    "command_prefix": ".",
    "api_key": "your_api_key_here",
    "max_connections": 10,
    # ... (Tambahkan item sesuai kebutuhan)
}

# Kelas Bot yang diturunkan dari Client
class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="ᴍᴀxɢᴜɴs ᴜʙᴏᴛ")

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()

# Kelas Ubot yang juga diturunkan dari Client
class Ubot(Client):
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}
    group_call = {}
    custom_dict = custom_dict  # Tambahkan objek dict ke dalam kelas

    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="ᴍᴀxɢᴜɴs ᴜʙᴏᴛ")

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix

    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, ["."])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            if message.text:
                text = message.text.strip().encode("utf-8").decode("utf-8")
                username = client.me.username or ""
                prefixes = await self.get_prefix(client.me.id)

                if not text:
                    return False

                for prefix in prefixes:
                    if not text.startswith(prefix):
                        continue

                    without_prefix = text[len(prefix) :]

                    for command in cmd.split("|"):
                        if not re.match(
                            rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                            without_prefix,
                            flags=re.IGNORECASE | re.UNICODE,
                        ):
                            continue

                        without_command = re.sub(
                            rf"{command}(?:@?{username})?\s?",
                            "",
                            without_prefix,
                            count=1,
                            flags=re.IGNORECASE | re.UNICODE,
                        )
                        message.command = [command] + [
                            re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                            for m in command_re.finditer(without_command)
                        ]

                        return True

                return False

        return filters.create(func)

    async def start(self):
        await super().start()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = ["."]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")

# Inisialisasi objek bot dan ubot
bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(name="ubot")

# Loop untuk setiap bot (bot dan ubot)
for current_bot in [bot, ubot]:
    if not hasattr(current_bot, "group_call"):
        setattr(current_bot, "group_call", GroupCallFactory(current_bot).get_group_call())
