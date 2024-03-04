import asyncio
import random

kopi = [
    "**Hadir Bang** 😁",
    "**Mmuaahh** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

@devs("absen")
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))

@PY.UBOT("tping|tp", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["tping"], "^") & filters.user(940035839))
async def _(client, message):
    await ping_cmd(client, message)