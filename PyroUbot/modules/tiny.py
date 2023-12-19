from PyroUbot import *

__MODULE__ = "tiny"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪɴʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>tiny</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ
"""


@PY.UBOT("tiny", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await tiny_cmd(client, message)
