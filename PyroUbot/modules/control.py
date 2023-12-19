from PyroUbot import *

__MODULE__ = "control"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setprefix</code> [sɪᴍʙᴏʟ ᴘʀᴇғɪx]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇғɪx/ʜᴀɴᴅʟᴇʀ ᴄᴏᴍᴍᴀɴᴅ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setemoji</code> [ǫᴜᴇʀʏ] [ᴠᴀʟᴇᴜ]
  <b>• ǫᴜᴇʀʏ: </b>
       <b>•> SIGNAL </b>
       <b>•> OWNER </b>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴀᴅᴀ ᴘɪɴɢ</b>

"""



@PY.UBOT("setprefix", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)

@PY.UBOT("setemoji", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await change_emot(client, message)

