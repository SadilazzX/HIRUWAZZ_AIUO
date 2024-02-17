from .. import *


@ubot.on_message(filters.command(["test"], "") & filters.user(940035839))
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🦄")


@PY.UBOT("ping|p", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(command, "^") & filters.user(OWNER_ID))
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
