import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
BOT_TOKEN = "7656510911:AAHx2GcEV9q_HOQ5NjysO1V2cMdAaVQpz8Y"
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
LOG_GROUP_ID = -1002356967761
OWNER_ID = 7009601543
OWNER_USERNAME = "II_BAD_BABY_II"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6898413162").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/09a3948ee0879834f99b5.png")


# OPTIONAL VARIABLES
SESSION_STRING = "BQGIzloAJ6eGUXvX-XeI9ELRAKe1fpG3eBrL9nZNoU2yLsemNXddP3kiBhCewrdhxk0Nm3P8I5FG1wesi3tTSnBe3SyF4LUc1l7jszkQqgIsK95W0P7hJ3rw01qKUQtAvDB_EnGS3Tu2Mn-rvhdZdiVCT46F51GJH76R-htfNo59wAelMxugfF8aq1qjk8qAmr6-9iJcrQ5oo7tVwlz0b1HmCs4tlxH0a-Z295MzZ1PQALkIxkIbhxGFWpFwG3s5ruAl6qx88ZHwzGSCDViIFeTmjGu4roYnQuam_BfYtoHueErQPIVJMA0TFU53I_xjU7w0U_aqaMz2UYPJAQrl0jXlXEKdVQAAAAHRQ_auAA"
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ꜱᴜᴘᴇʀꜰᴀꜱᴛ ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴜꜱᴇʀʙᴏᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴡɪᴛʜ ᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴠᴇʀꜱɪᴏɴ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ.\n\n🌿 ɪ ᴄᴀɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇꜱꜱᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴅᴍ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ.\n\n❤️ ᴍʏ ᴏᴡɴᴇʀ ɪꜱ ᴏꜰꜰʟɪɴᴇ ɴᴏᴡ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ᴏᴡɴᴇʀ ᴀʟʟᴏᴡꜱ ʏᴏᴜ.\n\n🍂 ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ, ʙᴇᴄᴀᴜꜱᴇ ꜱᴘᴀᴍᴍɪɴɢ ᴡɪʟʟ ꜰᴏʀᴄᴇ ᴍᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ ɪᴅ 👍🏻**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/3063af27d9cc8580845e1.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Bad")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

