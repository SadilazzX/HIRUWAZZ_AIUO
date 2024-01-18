from PyroUbot import *


__MODULE__ = "vctools"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>stopvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ.
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>joinvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ɴᴀɪᴋ ᴋᴇ ᴏs ᴋᴇ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>leavevc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏs ɢʀᴏᴜᴘ
  
"""


@PY.UBOT("startvc", sudo=True)
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc", sudo=True)
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await stop_vctools(client, message)


@PY.UBOT("joinvc", sudo=True)
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await join_os(client, message)

@PY.UBOT("leavevc", sudo=True)
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await turun_os(client, message)
