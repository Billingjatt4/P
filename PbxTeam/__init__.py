from PbxTeam.console import  SUDO_USERS, OWNER_ID, OWNER_USERNAME, MONGO_DB_URL
from aiohttp import ClientSession

# Ai-Userbot Version
__version__ = "v2.1.0"

spam_chats = []
aiosession = ClientSession()
SUDO_USER = SUDO_USERS
MONGO_DB_URL = MONGO_DB_URL
OWNER_USERNAME = OWNER_USERNAME
SUDO_USERS.append(OWNER_ID)


# All Clients
from .modules.clients.clients import (
    app, bot, call
)
app = app
bot = bot
call = call


# Command Handlers
from .modules.helpers.filters import (
    commandx, commandz
)
cdx = commandx
cdz = commandz


# Edit Or Reply
from .modules.helpers.events import (
    edit_or_reply
)
eor = edit_or_reply


# Logger
from .console import LOGGER
logs = LOGGER


# Plugins
from .console import PLUGINS
plugs = PLUGINS


# Variables
from . import console as config
vars = config


# Decorators
from .modules.helpers.wrapper import (
    super_user_only, sudo_users_only
)
super_user_only = super_user_only
sudo_users_only = sudo_users_only

