[![Donate via PayPal][donate-image]][donate-link]
[![Build][github-ci-image]][github-ci-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]
[![PyPI - Python Version][python-image]][pypi-link]
![License][license-image-mit]
# MkDocs Material Extensions

Markdown extension resources for MkDocs Material

## Install

```
pip install mkdocs-material-extensions
```

## Inline SVG Icons

MkDocs Material provides numerous icons from Material, FontAwesome, and Octicons, but it does so by inlining the SVG
icons into the source. Currently there is no easy way access these icons and arbitrarily insert them into Markdown
content. Users must include the icon fonts themselves and do it with HTML.

This module allows you to use PyMdown Extensions' [Emoji][emoji] extension to enable easy insertion of MkDocs Material's
SVG assets using simple `:emoji-syntax:`.  This is done by creating our own [emoji index][emoji-index] and
[emoji generator][emoji-generator]. The custom index provides a modified version of the Emoji extensions Twemoji
index.

In addition to the custom index, you must also specify the associated custom generator. This will will find the
appropriate icon and insert it into your Markdown content as an inlined SVG.

Example:

```yaml
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
```

Then, using the folder structure of Material's `.icons` folder, you can specify icons:

```
We can use Material Icons :material-airplane:.

We can also use Fontawesome Icons :fontawesome-solid-ambulance:.

That's not all, we can also use Octicons :octicons-octoface:.
```

[emoji]: https://facelessuser.github.io/mkdocs-material-extensions/extensions/emoji/
[emoji-index]: https://facelessuser.github.io/mkdocs-material-extensions/extensions/emoji/#custom-emoji-indexes
[emoji-generator]: https://facelessuser.github.io/mkdocs-material-extensions/extensions/emoji/#custom-emoji-generators

[donate-image]: https://img.shields.io/badge/Donate-PayPal-3fabd1?logo=paypal
[donate-link]: https://www.paypal.me/facelessuser
[github-ci-image]: https://github.com/facelessuser/mkdocs-material-extensions/workflows/build/badge.svg
[github-ci-link]: https://github.com/facelessuser/mkdocs-material-extensions/actions?workflow=build
[discord-image]: https://img.shields.io/discord/678289859768745989?logo=discord&logoColor=aaaaaa&color=mediumpurple&labelColor=333333
[discord-link]: https://discord.gg/fqQ7ypS
[codecov-image]: https://img.shields.io/codecov/c/github/facelessuser/mkdocs-material-extensions/master.svg?logo=codecov&logoColor=aaaaaa&labelColor=333333
[codecov-link]: https://codecov.io/github/facelessuser/mkdocs-material-extensions
[pypi-image]: https://img.shields.io/pypi/v/mkdocs-material-extensions.svg?logo=pypi&logoColor=aaaaaa&labelColor=333333
[pypi-link]: https://pypi.python.org/pypi/mkdocs-material-extensions
[python-image]: https://img.shields.io/pypi/pyversions/mkdocs-material-extensions?logo=python&logoColor=aaaaaa&labelColor=333333
[license-image-mit]: https://img.shields.io/badge/license-MIT-blue.svg?labelColor=333333
