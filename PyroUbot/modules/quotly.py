from PyroUbot import *

__MODULE__ = "quotly"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫᴜᴏᴛʟʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>q</code> [ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ
"""


@PY.UBOT("q", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await quotly_cmd(client, message)
