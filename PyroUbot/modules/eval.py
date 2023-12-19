from PyroUbot import *


@PY.UBOT("sh")
@PY.BOT("sh")
@PY.OWNER
async def _(client, message):
    await shell_cmd(client, message)


@PY.UBOT("eval")
@PY.OWNER
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
@PY.TOP_CMD
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum")
@PY.OWNER
async def _(client, message):
    await get_my_otp(client, message)

