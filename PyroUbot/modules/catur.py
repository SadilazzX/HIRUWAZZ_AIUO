from PyroUbot import *


__MODULE__ = "game"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴀᴍᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}catur</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴇʀᴍᴀɪɴ ɢᴀᴍᴇ ᴄᴀᴛᴜʀ
  """


@PY.UBOT("catur", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await catur_cmd(client, message)
