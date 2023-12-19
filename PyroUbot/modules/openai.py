from PyroUbot import *

__MODULE__ = "openai"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴘᴇɴᴀɪ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>ai</code> ᴏʀ <code>ask</code>  [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴊᴜᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴇ ᴄʜᴀᴛɢᴘᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>dalle</code> ᴏʀ <code>photo</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ᴘʜᴏᴛᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>stt</code> [ʀᴇᴘʟʏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘᴇsᴀɴ sᴜᴀʀᴀ ᴋᴇ ᴛᴇxᴛ
"""


@PY.UBOT("ai|ask", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("photo", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await stt_cmd(client, message)
