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
import logging
from BROKENXMUSIC import LOGGER
from urllib.parse import urlparse

from brokenxapi import BrokenXAPI

BROKENX_API_KEY = os.getenv("YTKEY")  # Get from https://t.me/ABOUTBROKENX




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


# ================= AUDIO DOWNLOAD (SDK) =================

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
        async with BrokenXAPI(api_key=BROKENX_API_KEY) as api:
            logger.info("🔄 [AUDIO] Requesting via BROKENXAPI SDK")
            data = await api.download(video_id, "audio")

        if not data or "telegram_url" not in data:
            logger.error(f"❌ [AUDIO] Invalid SDK response: {data}")
            return None

        telegram_url = data["telegram_url"]
        logger.info(f"🔗 [AUDIO] Telegram URL: {telegram_url}")

        downloaded_file = await get_telegram_file(
            telegram_url, video_id, "audio"
        )

        if downloaded_file:
            logger.info(f"🎉 [AUDIO] Successfully downloaded: {video_id}")
            return downloaded_file

        logger.error(f"⚠️ [AUDIO] Telegram download failed: {video_id}")
        return None

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
        async with BrokenXAPI(api_key=BROKENX_API_KEY) as api:
            logger.info("🔄 [VIDEO] Requesting via BROKENXAPI SDK")
            data = await api.download(video_id, "video")

        if not data or "telegram_url" not in data:
            logger.error(f"❌ [VIDEO] Invalid SDK response: {data}")
            return None

        telegram_url = data["telegram_url"]
        logger.info(f"🔗 [VIDEO] Telegram URL: {telegram_url}")

        downloaded_file = await get_telegram_file(
            telegram_url, video_id, "video"
        )

        if downloaded_file:
            logger.info(f"🎉 [VIDEO] Successfully downloaded: {video_id}")
            return downloaded_file

        logger.error(f"⚠️ [VIDEO] Telegram download failed: {video_id}")
        return None

    except Exception as e:
        logger.error(f"❌ [VIDEO] Exception: {e}")
        return None




class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        r = (await results.next())["result"][0]
        return (
            r["title"],
            r["duration"],
            int(time_to_seconds(r["duration"])) if r["duration"] else 0,
            r["thumbnails"][0]["url"].split("?")[0],
            r["id"],
        )

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
    ):
        if videoid:
            link = self.base + link

        try:
            if video:
                file = await download_video(link)
            else:
                file = await download_song(link)

            return (file, True) if file else (None, False)

        except Exception as e:
            logger = LOGGER("BrokenXAPI")
            logger.error(f"❌ Download failed: {e}")
            return None, False
