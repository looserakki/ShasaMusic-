import os
from os import getenv



que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCCJtbo92Z0XHqJ8vcf-4g1E26UMbts7PncmQpwGB2ZQUcXaA89prvS1gZTBPc8_H5VUerZYFSEvNXPG33kZNZ_XPz9nNYilgUjGN1roTLCoeKrjFbv750oocf1dUcQ6iO7NaCqcC8VRo6VyrLmaHALm1ypiRqBvdMQTOHLB42tjx_ZAPoQTHK9g6Voi7r4o_-0T6jzpoCizoWD1j_ZXSNlovyhrGfhBs0B9zjRWYf-YQOTmArEdlwFotiEGWQC8vYc260Fzl7jLSmee4VWk7vA6-ZEIXBbwdsndug9NLbUy__AKN2rN5DHfXtPO-W22WDmZWmnyvNpY1YAeWSOa1ZIck0dzQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAHpuAEOph7_QVA3kswuU2xcjYMuSwhZmu8")
BOT_NAME = getenv("BOT_NAME", " MUSICBOT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeCodeBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3365191a863f7fd4c2e85.jpg")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")
BOT_USERNAME = getenv("BOT_USERNAME", "PATRICIA_ROBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PATRICIA_ASSISTANT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DeCodeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "Patricia v4")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/piroXpower")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
PMMSG = getenv(
    "PMMSG",
    f"Hi there, This is a music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n",
)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2012882227").split()))
