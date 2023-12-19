from PyroUbot import *

__MODULE__ = "info"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>info</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀs]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>cinfo</code> [ᴄʜᴀᴛ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴄʜᴀᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ
"""


@PY.UBOT("info", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cinfo", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await cinfo_cmd(client, message)
