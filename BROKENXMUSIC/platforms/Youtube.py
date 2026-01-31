import asyncio
import os
import re
import json
from typing import Union
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from py_yt import VideosSearch
from ..utils.database import is_on_off
from ..utils.formatters import time_to_seconds
from BROKENXMUSIC import app
from BROKENXMUSIC import LOGGER
from urllib.parse import urlparse


from brokenxapi import BrokenXAPI

API_KEY = os.getenv("YTKEY")  # Get it for free from https://t.me/aboutbrokenx



async def get_telegram_file(telegram_url: str, video_id: str, file_type: str) -> str:
    logger = LOGGER("BrokenXAPI")
    try:
        extension = ".webm" if file_type == "audio" else ".mkv"
        file_path = os.path.join("downloads", f"{video_id}{extension}")

        if os.path.exists(file_path):
            logger.info(f"📂 [LOCAL] File exists: {video_id}")
            return file_path

        parsed = urlparse(telegram_url)
        parts = parsed.path.strip("/").split("/")

        if len(parts) < 2:
            logger.error(f"❌ Invalid Telegram link format: {telegram_url}")
            return None

        channel_name = parts[0]
        message_id = int(parts[1])

        logger.info(f"📥 [TELEGRAM] Downloading from @{channel_name}/{message_id}")

        msg = await app.get_messages(channel_name, message_id)

        os.makedirs("downloads", exist_ok=True)
        await msg.download(file_name=file_path)

        timeout = 0
        while not os.path.exists(file_path) and timeout < 60:
            await asyncio.sleep(0.5)
            timeout += 0.5

        if os.path.exists(file_path):
            logger.info(f"✅ [TELEGRAM] Downloaded: {video_id}")
            return file_path

        logger.error(f"❌ [TELEGRAM] Timeout: {video_id}")
        return None

    except Exception as e:
        logger.error(f"❌ [TELEGRAM] Failed to download {video_id}: {e}")
        return None




async def download_song(link: str) -> str:
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    logger = LOGGER("BrokenXAPI")
    logger.info(f"🎵 [AUDIO] Starting download for: {video_id}")

    if not video_id or len(video_id) < 3:
        logger.error(f"❌ [AUDIO] Invalid video ID: {video_id}")
        return None

    os.makedirs("downloads", exist_ok=True)
    file_path = os.path.join("downloads", f"{video_id}.webm")

    if os.path.exists(file_path):
        logger.info(f"🎵 [LOCAL] File exists: {video_id}")
        return file_path

    try:
        async with BrokenXAPI(api_key=API_KEY) as api:
            data = await api.download(video_id, "audio")

        if not data or "telegram_url" not in data:
            logger.error(f"❌ [AUDIO] Invalid SDK response: {data}")
            return None

        return await get_telegram_file(
            data["telegram_url"], video_id, "audio"
        )

    except Exception as e:
        logger.error(f"❌ [AUDIO] Exception: {e}")
        return None




async def download_video(link: str) -> str:
    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link
    logger = LOGGER("BrokenXAPI")
    logger.info(f"🎥 [VIDEO] Starting download for: {video_id}")

    if not video_id or len(video_id) < 3:
        logger.error(f"❌ [VIDEO] Invalid video ID: {video_id}")
        return None

    os.makedirs("downloads", exist_ok=True)
    file_path = os.path.join("downloads", f"{video_id}.mkv")

    if os.path.exists(file_path):
        logger.info(f"🎥 [LOCAL] File exists: {video_id}")
        return file_path

    try:
        async with BrokenXAPI(api_key=API_KEY) as api:
            data = await api.download(video_id, "video")

        if not data or "telegram_url" not in data:
            logger.error(f"❌ [VIDEO] Invalid SDK response: {data}")
            return None

        return await get_telegram_file(
            data["telegram_url"], video_id, "video"
        )

    except Exception as e:
        logger.error(f"❌ [VIDEO] Exception: {e}")
        return None



class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        return None

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid
