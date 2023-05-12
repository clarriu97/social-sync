"""
Comand line interface for social_sync.

Usage:

- Help:

    ```bash
        python -m social_sync.cli --help
    ```

- Help for a specific command:

    ```bash
        python -m social_sync.cli <command> --help
    ```

- Upload a video to Youtube:

    ```bash
        python -m social_sync.cli upload_to_youtube --file <video_file> --client_secrets_file <client_secrets_file>
    ```
"""
import click

from social_sync.distribute.youtube import upload_video as upload_youtube_video
from social_sync.distribute.twitter import upload_video as upload_twitter_video
from social_sync.entities import YoutubeUploadRequest, TwitterUploadRequest
from social_sync import youtube_categories


@click.group()
def cli():
    """Social Sync CLI."""


@cli.command()
@click.option("--file", required=True, help="Video file to upload")
@click.option("--status", required=True, help="The text of your tweet")
@click.option("--apikey", required=True, help="Twitter API key")
@click.option("--apikey_secret", required=True, help="Twitter API key secret")
@click.option("--access_token", required=True, help="Twitter access token")
@click.option("--access_token_secret", required=True, help="Twitter access token secret")
def upload_to_twitter(file, status, apikey, apikey_secret, access_token, access_token_secret):
    """Upload a video to Twitter."""
    upload_request = TwitterUploadRequest(
        file=file,
        apikey=apikey,
        apikey_secret=apikey_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        status=status
    )
    upload_twitter_video(upload_request)


@cli.command()
@click.option("--file", required=True, help="Video file to upload")
@click.option("--client_secrets_file", required=True, help="Absolute path to the client secrets JSON file")
@click.option("--title", help="Video title", default="Test Title")
@click.option("--description", help="Video description", default="Test Description")
@click.option("--category", default=youtube_categories.ENTERTAINMENT,
              help="Numeric video category. " + "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
@click.option("--keywords", help="Video keywords, comma separated", default="")
@click.option("--privacy_status", default="private", help="Video privacy status.")
def upload_to_youtube(file, client_secrets_file, title, description, category, keywords, privacy_status):
    """Upload a video to Youtube."""
    upload_request = YoutubeUploadRequest(
        file=file,
        title=title,
        description=description,
        category=category,
        keywords=keywords,
        privacy_status=privacy_status,
        client_secrets_file=client_secrets_file
    )
    upload_youtube_video(upload_request)


if __name__ == "__main__":
    cli()
