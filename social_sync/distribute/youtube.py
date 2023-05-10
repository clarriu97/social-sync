"""Youtube module"""
import httplib2
import os
import sys
import time
import click

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from social_sync.entities import YoutubeUploadRequest
from social_sync import youtube_categories


httplib2.RETRIES = 1
MAX_RETRIES = 10
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def _get_authenticated_service(upload_request: YoutubeUploadRequest):
    MISSING_CLIENT_SECRETS_MESSAGE = f"""
    WARNING: Please configure OAuth 2.0

    To make this sample run you will need to populate the client_secrets.json file
    found at:

    {os.path.join(os.path.dirname(__file__), upload_request.client_secrets_file)}

    with information from the API Console
    https://console.cloud.google.com/

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """
    flow = flow_from_clientsecrets(upload_request.client_secrets_file,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage(f"{sys.argv[0]}-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, upload_request)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))


def _initialize_upload(youtube, options):
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body = {
        "snippet": {
            "title": options.title,
            "description": options.description,
            "tags": tags,
            "categoryId": options.category
        },
        "status": {
            "privacyStatus": options.privacy
        }
    }

    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    _resumable_upload(insert_request)


def _resumable_upload(insert_request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print("Uploading file...")
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print(f"Video id '{response['id']}' was successfully uploaded.")
                else:
                    exit(f"The upload failed with an unexpected response: {response}")
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"

        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                exit("No longer attempting to retry.")

            sleep_seconds = 2
            print(f"Sleeping {sleep_seconds} seconds and then retrying...")
            time.sleep(sleep_seconds)


def upload_video(upload_request: YoutubeUploadRequest):
    if not os.path.exists(upload_request.file):
        raise FileNotFoundError(f"File {upload_request.file} not found")
    youtube = _get_authenticated_service(upload_request)
    try:
        _initialize_upload(youtube, upload_request)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")


@click.command()
@click.option("--file", required=True, help="Video file to upload")
@click.option("--title", help="Video title", default="Test Title")
@click.option("--description", help="Video description", default="Test Description")
@click.option("--category", default=youtube_categories.ENTERTAINMENT,
              help="Numeric video category. " + "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
@click.option("--keywords", help="Video keywords, comma separated", default="")
@click.option("--privacy_status", default="private", help="Video privacy status.")
@click.option("--client_secrets_file", default="client_secrets.json", help="Absolute path to the client secrets JSON file")
def upload_video_cli(file, title, description, category, keywords, privacy_status, client_secrets_file):
    upload_request = YoutubeUploadRequest(
        file=file,
        title=title,
        description=description,
        category=category,
        keywords=keywords,
        privacy_status=privacy_status,
        client_secrets_file=client_secrets_file
    )
    upload_video(upload_request)


if __name__ == "__main__":
    upload_video_cli()
