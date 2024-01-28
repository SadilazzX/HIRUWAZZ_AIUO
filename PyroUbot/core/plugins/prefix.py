from PyroUbot import *


async def setprefix(client, message):
    emot_1 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_proses = emot_1 if emot_1 else "6298454498884978957"
    if client.me.is_premium:
        _prefix = f"""
<b><emoji id={emot_proses}>⏰</emoji>ᴍᴇᴍᴘᴇʀᴏsᴇs...</b>
"""
    else:
        _prefix = f"""
<b>ᴍᴇᴍᴘᴇʀᴏsᴇs...</b>
"""
        Tm = await message.reply(_prefix, quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text}</code> sɪᴍʙᴏʟ ᴘʀᴇғɪx")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
    emot_1 = await get_vars(client.me.id, "EMOJI_SETUJU")
    emot_setuju = emot_1 if emot_1 else "5852871561983299073"
    if client.me.is_premium:
        _setuju = f"""
<b><emoji id={emot_setuju}>✅</emoji>ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>
"""
    else:
        _setuju = f"""
<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>
"""
            return await Tm.edit(_setuju)
        except Exception as error:
            return await Tm.edit(str(error))


async def change_emot(client, message):
    try:
        msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                "<b>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜ ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ</b>"
            )

        if len(message.command) < 3:
            return await msg.edit("<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")

        query_mapping = {"signal": "EMOJI_PING", "owner": "EMOJI_MENTION"}
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"<b>✅ <code>{query_var}</code> ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ</b>")
        else:
            await msg.edit("<b>ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    except Exception as error:
        await msg.edit(str(error))
