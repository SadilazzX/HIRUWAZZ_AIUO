from PyroUbot import *

__MODULE__ = "kang"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>kang</code> [ʀᴇᴘʟʏ ᴛᴏ ɪᴍᴀɢᴇ/sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴅᴀɴ ᴄᴏsᴛᴜᴍ ᴇᴍᴏᴊɪ sᴛɪᴄᴋᴇʀ ᴋᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ

  <b>ɴᴏᴛᴇ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴘᴀᴋᴇᴛ ꜱᴛɪᴋᴇʀ ʙᴀʀᴜ ɢᴜɴᴀᴋᴀɴ ᴀɴɢᴋᴀ ᴅɪ ʙᴇʟᴀᴋᴀɴɢ !ᴋᴀɴɢ.
  <b>ᴇxᴀᴍᴘʟᴇ:</b> <code>kang 2</code> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴅᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴇ ᴘᴀᴋᴇᴛ ꜱᴛɪᴋᴇʀ ᴋᴇ-2</b>
"""



@PY.UBOT("kang", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await kang(client, message)
