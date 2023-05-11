"""Twitter module"""
import tweepy

from social_sync.entities import TwitterUploadRequest


def _get_twitter_api(apikey: str, apikey_secret: str, access_token: str, access_token_secret: str):
    """
    Gets a Twitter API object.

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

    Returns
    -------
    tweepy.API
        Twitter API object.
    """
    auth = tweepy.OAuthHandler(apikey, apikey_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def upload_video(upload_request: TwitterUploadRequest):
    """
    Uploads a video to Twitter.

    Parameters
    ----------
    upload_request : social_sync.entities.TwitterUploadRequest
    """
    api = _get_twitter_api(upload_request.apikey, upload_request.apikey_secret,
                           upload_request.access_token, upload_request.access_token_secret)
    api.update_status_with_media(status=upload_request.status, filename=upload_request.file)
