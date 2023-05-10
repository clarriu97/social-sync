"""Comand line interface for social_sync."""
import click

from social_sync.distribute.youtube import upload_video as upload_youtube_video
from social_sync.entities import YoutubeUploadRequest
from social_sync import youtube_categories


@click.group()
def cli():
    """Social Sync CLI."""


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
