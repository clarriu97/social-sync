"""Data structures for social_sync"""
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from social_sync import youtube_categories


class YoutubeUploadRequest(BaseModel):
    """
    Youtube data structure to upload a video.

    Parameters
    ----------
    title : str
        Video title.
    description : str
        Video description.
    category : int, optional
        Numeric video category. See https://developers.google.com/youtube/v3/docs/videoCategories/list, by default youtube_categories.ENTERTAINMENT
    keywords : str, optional
        Video keywords, comma separated, by default ""
    privacy : str, optional
        Video privacy status, by default "private"
    file : str
        Video file to upload.
    client_secrets_file : str
        Absolute path to the client secrets JSON file.
    logging_level : str, optional
        Logging level, by default "ERROR"
    auth_host_name : str, optional
        Authentication host name, by default "localhost"
    auth_host_port : list, optional
        Authentication host port, by default [8080, 8090]
    noauth_local_webserver : bool, optional
        No authentication local webserver, by default False
    """
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
