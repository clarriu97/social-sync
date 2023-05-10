"""Data structures for social_sync"""
from pydantic import BaseModel

from social_sync import youtube_categories


class YoutubeUploadRequest(BaseModel):
    title: str
    description: str
    category: int = youtube_categories.ENTERTAINMENT
    keywords: str = ""
    privacy: str = "private"
    file: str
    client_secrets_file: str
