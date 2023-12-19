from PyroUbot import *


@PY.UBOT("getubot")
@PY.OWNER
async def _(client, message):
    await getubot_cmd(client, message)


@PY.INLINE("^ambil_ubot")
async def _(client, inline_query):
    await getubot_query(client, inline_query)
