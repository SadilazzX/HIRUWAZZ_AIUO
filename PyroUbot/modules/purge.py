from PyroUbot import *

__MODULE__ = "purge"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴜʀɢᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>purge</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʙᴇʀsɪʜᴋᴀɴ (ʜᴀᴘᴜs sᴇᴍᴜᴀ ᴘᴇsᴀɴ) ᴏʙʀᴏʟᴀɴ ᴅᴀʀɪ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀs ʜɪɴɢɢᴀ ʏᴀɴɢ ᴛᴇʀᴀᴋʜɪʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>del</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʜᴀᴘᴜs ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀs

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>purgeme</code> [ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇssᴀɢᴇs]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʜᴀᴘᴜs ᴘᴇsᴀɴ ᴀɴᴅᴀ sᴇɴᴅɪʀɪ ᴅᴇɴɢᴀɴ ᴍᴇɴᴇɴᴛᴜᴋᴀɴ ᴛᴏᴛᴀʟ ᴘᴇsᴀɴ
"""


@PY.UBOT("del", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await del_cmd(client, message)


@PY.UBOT("purgeme", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await purgeme_cmd(client, message)


@PY.UBOT("purge", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await purge_cmd(client, message)
