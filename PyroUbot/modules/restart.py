from PyroUbot import *


@PY.BOT("login")
@PY.OWNER
async def _(client, message):
    await login_cmd(client, message)


@PY.BOT("restart")
async def _(client, message):
    await restart_cmd(client, message)
