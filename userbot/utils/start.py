from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/922aee497e89433ef5cfb.jpg",
                caption="🐣 **Senja x Userbot Has Been Actived**!!\n━━━━━━━━━━━━━\n⌬ **Userbot Version** - 8.0@SenjaxUserbot\n━━━━━━━━━━━━━\n⌬ **Powered By:** @Senjaprojectt ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Senjaprojectt"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
