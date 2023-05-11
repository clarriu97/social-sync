"""Data structures for social_sync"""
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from social_sync import youtube_categories


class Request(BaseModel):
    """
    Base request class.

    Parameters
    ----------
    file : str
        Video file to upload.
    """
    file: str


class TwitterUploadRequest(Request):
    """
    Twitter data structure to upload a video.

    Parameters
    ----------
    apikey : str
        Twitter API key.
    apikey_secret : str
        Twitter API key secret.
    access_token : str
        Twitter access token.
    access_token_secret : str
        Twitter access token secret.
    status : str
        The text of your tweet.
    """
    apikey: str
    apikey_secret: str
    access_token: str
    access_token_secret: str
    status: str


class YoutubeUploadRequest(Request):
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
    client_secrets_file: str
    logging_level: str = "ERROR"
    auth_host_name: str = "localhost"
    auth_host_port: list = [8080, 8090]
    noauth_local_webserver: bool = False
