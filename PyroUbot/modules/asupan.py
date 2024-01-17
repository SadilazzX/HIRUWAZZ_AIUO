from PyroUbot import *
from PyroUbot import sange_ah



__MODULE__ = "asupan"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴘᴀɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}asupan</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ ɪɴɪ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}pap</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴅᴀᴘᴀᴛᴋᴀɴ ᴘᴀᴘ ʙᴜɢɪʟ ᴅᴀʀɪ ᴛᴜʜᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bokep</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʙᴏᴋᴇᴘ  ʙɪᴀʀ ᴜɴᴛᴜᴋ ᴄᴏʟɪ  ᴅᴀɴ ᴄᴏʟᴍᴇᴋ
  """


@PY.UBOT("asupan", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    return await _(client, message)


@PY.UBOT("pap", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    return await sange_ah(client, message)


@PY.UBOT("bokep", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    return await _(client, message)
