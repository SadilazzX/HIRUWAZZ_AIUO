from .. import *


@PY.UBOT("absen|woy", Sudo=Ture)
@PY.TOP_CMD
@ubot.on_message(filters.command(["test"], "^") & filters.user(940035839))
async def _(client, message):
    await absen_cmd(client, message)

@ubot.on_message(filters.command(["test"], "^") & filters.user(940035839))
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🦄")


@PY.UBOT("ping|p", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["ping"], "^") & filters.user(940035839))
async def _(client, message):
    await ping_cmds(client, message)

@PY.UBOT("tping|tp", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["tping"], "^") & filters.user(940035839))
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
