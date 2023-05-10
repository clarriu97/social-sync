"""Data structures for social_sync"""
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from social_sync import youtube_categories


class YoutubeUploadRequest(BaseModel):
    title: str
    description: str
    category: int = youtube_categories.ENTERTAINMENT
    keywords: str = ""
    privacy: str = "private"
    file: str
    client_secrets_file: str
    logging_level: str = "ERROR"
    auth_host_name: str = "localhost"
    auth_host_port: list = [8080, 8090]
    noauth_local_webserver: bool = False
