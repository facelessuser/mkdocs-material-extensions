"""
Emoji extras for Material.

Override the indexes with an extended version that includes short names for Material icons, FontAwesome, etc.
"""
import os
import glob
import copy
import codecs
import inspect
import material
from pymdownx.emoji import TWEMOJI_SVG_CDN, add_attriubtes
import xml.etree.ElementTree as etree  # noqa: N813

RESOURCES = os.path.dirname(inspect.getfile(material))


def _patch_index(index):
    """Patch the given index."""

    # Find our icons
    icon_path = os.path.join(RESOURCES, '.icons')
    norm_base = icon_path.replace('\\', '/') + '/'
    for result in glob.glob(icon_path.replace('\\', '/') + '/**/*.svg', recursive=True):
        name = ':{}:'.format(result.replace('\\', '/').replace(norm_base, '', 1).replace('/', '-').lstrip('.')[:-4])
        if name not in index['emoji'] and name not in index['aliases']:
            # Easiest to just store the path and pull it out from the index
            index["emoji"][name] = {'name': name, 'path': result}


def twemoji():
    """Provide a copied Twemoji index with additional codes for Material included icons."""

    import pymdownx.twemoji_db as twemoji_db

    # Copy the Twemoji index
    index = {
        "name": 'twemoji',
        "emoji": copy.deepcopy(twemoji_db.emoji),
        "aliases": copy.deepcopy(twemoji_db.aliases)
    }

    _patch_index(index)

    return index


def to_svg(index, shortname, alias, uc, alt, title, category, options, md):
    """Return SVG element."""

    is_unicode = uc is not None

    if is_unicode:
        # Handle Twemoji emoji.
        svg_path = TWEMOJI_SVG_CDN

        attributes = {
            "class": options.get('classes', index),
            "alt": alt,
            "src": "%s%s.svg" % (
                options.get('image_path', svg_path),
                uc
            )
        }

        if title:
            attributes['title'] = title

        add_attriubtes(options, attributes)

        return etree.Element("img", attributes)
    else:
        # Handle Material SVG assets.
        el = etree.Element('span', {"class": options.get('classes', index)})
        svg_path = md.inlinePatterns['emoji'].emoji_index['emoji'][shortname]['path']
        with codecs.open(svg_path, 'r', encoding='utf-8') as f:
            el.text = md.htmlStash.store(f.read())
        return el
