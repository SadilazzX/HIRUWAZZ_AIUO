from PyroUbot import *


@PY.UBOT("prem")
@PY.OWNER
@PY.BOT("prem")
async def _(client, message):
    await prem_user(client, message)


@PY.UBOT("unprem")
@PY.BOT("unprem")
@PY.OWNER
async def _(client, message):
    await unprem_user(client, message)


@PY.UBOT("getprem")
@PY.BOT("getprem")
@PY.OWNER
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.UBOT("seles")
@PY.BOT("seles")
@PY.OWNER
async def _(client, message):
    await seles_user(client, message)


@PY.UBOT("unseles")
@PY.BOT("unseles")
@PY.OWNER
async def _(client, message):
    await unseles_user(client, message)


@PY.UBOT("getseles")
@PY.BOT("getseles")
@PY.OWNER
async def _(client, message):
    await get_seles_user(client, message)

@PY.UBOT("top")
@PY.BOT("top")
@PY.OWNER
async def _(client, message):
    await get_top_module(client, message)


@PY.UBOT("time")
@PY.BOT("time")
@PY.OWNER
async def _(client, message):
    await expired_add(client, message)

@PY.UBOT("cek")
@PY.BOT("cek")
@PY.OWNER
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("untime")
@PY.OWNER
async def _(client, message):
    await un_expired(client, message)

