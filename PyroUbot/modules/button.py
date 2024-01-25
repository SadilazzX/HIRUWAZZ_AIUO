from PyroUbot import *


__MODULE__ = "Button"
__HELP__ = """
Bantuan Untuk Button

• Perintah: <code>{0}button</code> [balas pesan]
• Penjelasan: Untuk membuat teks menjadi button.
"""


@PY.UBOT("button", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await cmd_button(client, message)


@PY.UBOT("get_button", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await inline_button(client, message)
