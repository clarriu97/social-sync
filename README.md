<div align="center">

# Social sync

Social Sync is a software tool that helps content creators automate the process of uploading and sharing videos across multiple social media platforms, including TikTok, YouTube, Twitter, and Instagram. With Social Sync, users can easily manage and schedule their posts, allowing them to focus on creating great content without worrying about the logistics of social media. This tool helps to increase social media presence and grow followers by making sharing videos easy and efficient.

[Contributing Guidelines](./CONTRIBUTING.md) · [Request a Feature](https://github.com/clarriu97/social-sync/-/issues/new?issuable_template=Feature) · [Report a Bug](https://github.com/clarriu97/social-sync/-/issues/new?issuable_template=Bug)

</div>

## Usage

You can install this package using [pip](https://pip.pypa.io/en/stable/):

```
$ pip install social_sync
```

You can now import this module on your Python project:

```python
import social_sync
```

## Development

To start developing this project, clone this repo and do:

```
$ make env-create
```

This will create a virtual environment with all the needed dependencies (using [tox](https://tox.readthedocs.io/en/latest/)). You can activate this environment with:

```
$ source ./.tox/social_sync/bin/activate
```

Then, you can run `make help` to learn more about the different tasks you can perform on this project using [make](https://www.gnu.org/software/make/).

## License

[Copyright](./LICENSE)