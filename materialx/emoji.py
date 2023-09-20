"""
Emoji extras for Material.

Override the indexes with an extended version that includes short names for Material icons, FontAwesome, etc.
"""
import os
import glob
import copy
import codecs
import functools
import inspect
import material
import pymdownx
from pymdownx.emoji import TWEMOJI_SVG_CDN, add_attriubtes
import xml.etree.ElementTree as etree  # noqa: N813

OPTION_SUPPORT = pymdownx.__version_info__ >= (7, 1, 0)
RESOURCES = os.path.dirname(inspect.getfile(material))


def _patch_index(options):
    """Patch the given index."""

    icon_locations = options.get('custom_icons', [])[:]
    icon_locations.append(os.path.join(RESOURCES, 'templates', '.icons'))
    return _patch_index_for_locations(tuple(icon_locations))


@functools.lru_cache(maxsize=None)
def _patch_index_for_locations(icon_locations):
    import pymdownx.twemoji_db as twemoji_db

    # Copy the Twemoji index
    index = {
        "name": 'twemoji',
        "emoji": copy.deepcopy(twemoji_db.emoji) if not OPTION_SUPPORT else twemoji_db.emoji,
        "aliases": copy.deepcopy(twemoji_db.aliases) if not OPTION_SUPPORT else twemoji_db.aliases
    }

    # Find our icons
    for icon_path in icon_locations:
        norm_base = icon_path.replace('\\', '/') + '/'
        for result in glob.glob(glob.escape(icon_path.replace('\\', '/')) + '/**/*.svg', recursive=True):
            name = ':{}:'.format(result.replace('\\', '/').replace(norm_base, '', 1).replace('/', '-').lstrip('.')[:-4])
            if name not in index['emoji'] and name not in index['aliases']:
                # Easiest to just store the path and pull it out from the index
                index["emoji"][name] = {'name': name, 'path': result}
    return index


if OPTION_SUPPORT:  # pragma: no cover
    def twemoji(options, md):
        """Provide a copied Twemoji index with additional codes for Material included icons."""

        return _patch_index(options)

else:  # pragma: no cover
    def twemoji():
        """Provide a copied Twemoji index with additional codes for Material included icons."""

        return _patch_index({})


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
