# Jangan hapus ini ya mmk!
# By @Itsmesenjaaah SenjaxUserbot

from time import sleep
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd


@Xa_cmd(pattern=r"lebaran2(?: |$)(.*)")
async def _(typew):
    await typew.edit("🕌")
    await typew.edit("🕌🕌")
    await typew.edit("🕌🕌🕌")
    await typew.edit("✨")
    sleep(1)
    await typew.edit("🕌 𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙃𝙖𝙧𝙞 𝙍𝙖𝙮𝙖 𝙄𝙙𝙪𝙡 𝙁𝙞𝙩𝙧𝙞 🕌\n"
                     "Ramadhan akan segera pergi, tapi diri tak bisa suci\n"
                     "Jika marah dan sakit hati belum juga bisa dimaafkan dan dimengerti\n"
                     "Taqobballahu minna wa minkum \n"
                     "Taqobbal ya Kariim\n"
                     "𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐋𝐚𝐡𝐢𝐫 𝐃𝐚𝐧 𝐁𝐚𝐭𝐢𝐧\n")


@Xa_cmd(pattern=r"lebaran3(?: |$)(.*)")
async def _(typew):
    await typew.edit("𝐌𝐢𝐧𝐚𝐥 '𝐀𝐢𝐝𝐢𝐧 𝐰𝐚𝐥-𝐅𝐚𝐢𝐳𝐢𝐧🕌\n"
                     "Mohon maaf kalo ada salah kata,\n"
                     "Salah Cinta, atau Salah menaruh rasa\n"
                     "Selamat  Hari Raya Idul Fitri 🕌\n")


@Xa_cmd(pattern=r"lebaran4(?: |$)(.*)")
async def _(typew):
    await typew.edit("𝘾𝙏𝙍𝙇 + 𝙎 Berkah Ramadan\n"
                     "𝘾𝙏𝙍𝙇 + 𝘼 DELETE Dosa dan kesalahan\n"
                     "𝘾𝙏𝙍𝙇 + 𝘾 𝘾𝙏𝙍𝙇 + 𝙑 Kebahagian Lebaran\n"
                     "𝙎𝙀𝙇𝘼𝙈𝘼𝙏 𝙃𝘼𝙍𝙄 𝙍𝘼𝙔𝘼 𝙄𝘿𝙐𝙇 𝙁𝙄𝙏𝙍𝙄 !!\n")


@Xa_cmd(pattern=r"lebaran5(?: |$)(.*)")
async def _(typew):
    await typew.edit("Walaupun gua pernah nyimpen perasaan ke lu, setidaknya gua ga mau nyimpen dosa ke lu,")
    sleep(2)
    await typew.edit("Jadiii... ")
    sleep(2)
    await typew.edit("Maaf kalo gua pernah suka & cinta sama lu ")
    sleep(1.5)
    await typew.edit("Eh maksudnya, pernah berbuat salah ke lu ")
    sleep(2)
    await typew.edit("maafin ya!!")


@Xa_cmd(pattern=r"petasan(?: |$)(.*)")
async def _(typew):
    await typew.edit("🎆")
    sleep(2)
    await typew.edit("𝐒𝐄𝐋𝐀𝐌𝐀𝐓 𝐈𝐃𝐔𝐋 𝐅𝐈𝐓𝐑𝐈 1443")
    sleep(1)
    await typew.edit("Mohon Maaf Lahir Dan Batin")


@Xa_cmd(pattern=r"thr(?: |$)(.*)")
async def _(typew):
    await typew.edit("Sory, lebih butuh Thr daripada Maaf dari lu !")


@Xa_cmd(pattern=r"slok(?: |$)(.*)")
async def _(typew):
    await typew.edit("Udah Kelar nih Puasanya, Mau berantem ga? Sharelok cepet!")


@Xa_cmd(pattern=r"thr2(?: |$)(.*)")
async def _(typew):
    await typew.edit("Minal aidzin Bro! Jangan lupa kirim thr ke rekening gua")


@Xa_cmd(pattern=r"thr3(?: |$)(.*)")
async def _(typew):
    await typew.edit("Lebaran nih...")
    sleep(1)
    await typew.edit("Bagi Thr lah jjingg!!!!")


CMD_HELP.update(
    {
        "idulfitri": f"**Plugin : **`idulfitri`\
        \n\n  •  **Perintah :** `{cmd}lebaran1`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran2`\
        \n  •  **Fungsi : **Coba Aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran3`\
        \n  •  **Fungsi : **Coba Aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran4`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran5`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran6`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}petasan`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}thr`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}slok`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}thr2`\
        \n  •  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}thr3`\
        \n  •  **Fungsi : **Coba aja.\
        "
    }
)
