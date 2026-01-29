import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", 35852042)) 
API_HASH = getenv("API_HASH", None)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_USERNAME = ("BOT_USERNAME", None) 
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 19000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002094142057))


OWNER_ID = int(getenv("OWNER_ID", 1841914911))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mrxbroken011/BROKEN-X-MUSIC.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Brokenxnetwork1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+GdYztKC7jPk1N2Y1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 1000))



TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))




STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

AYU = [
    "💞", "𝚃𝙷𝙸𝚂 𝚂𝙾𝙽𝙶 𝙸𝚂 𝚃𝙾𝚃𝙰𝙻𝙻𝚈 𝙵𝙰𝙱𝚄𝙻𝙰𝚂𝚃𝙸𝙲...🔥🥰", "🔍", "🧪", "ʜᴏʟᴅ ᴏɴ ᴅᴀʀʟɪɴɢ 💗", "⚡️", "🔥", "ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...❤‍🔥", "🎩", "🌈", "🍷", "🥂", "🥃", 
    "ᴀᴄᴄʜɪ ᴘᴀsᴀɴᴅ ʜᴀɪ 🥰", "ʟᴏᴏᴋɪɴɢ ғᴏʀ ʏᴏᴜʀ sᴏɴɢ... ᴡᴀɪᴛ! 💗", "🪄", "💌", "ᴏᴋ ʙᴀʙʏ ᴡᴀɪᴛ😘 ғᴇᴡ sᴇᴄᴏɴᴅs", "ᴀʜʜ! ɢᴏᴏᴅ ᴄʜᴏɪᴄᴇ ʜᴏʟᴅ ᴏɴ...",  
    "ᴡᴏᴡ! ɪᴛ's ᴍʏ ғᴀᴠᴏʀɪᴛᴇ sᴏɴɢ...", "ɴɪᴄᴇ ᴄʜᴏɪᴄᴇ..! ᴡᴀɪᴛ 𝟸 sᴇᴄᴏɴᴅ", "🔎", "🍹", "ɪ ʟᴏᴠᴇ ᴛʜᴀᴛ sᴏɴɢ..!😍", "💥", "💗", "✨"
]



START_IMG_URL = [
     "https://files.catbox.moe/dkmm7b.jpeg", 
     "https://files.catbox.moe/ja6mf5.jpeg", 
     "https://files.catbox.moe/2tmu0j.jpeg", 
     "https://files.catbox.moe/e5mxx2.jpeg", 
     "https://files.catbox.moe/7c6qzc.jpeg", 
     "https://files.catbox.moe/4x1m0u.jpeg", 
     "https://files.catbox.moe/7juopm.jpeg", 
     "https://files.catbox.moe/0crhh2.jpeg", 
     "https://files.catbox.moe/b1da6m.jpg", 
     "https://files.catbox.moe/hsv9el.jpg", 
]

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/dkmm7b.jpeg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://telegra.ph/file/0ffb4a004185a3991ce18.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
