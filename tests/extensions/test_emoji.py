"""Test emoji indexes and generators."""
from .. import util
from materialx import emoji
from bs4 import BeautifulSoup
import markdown
from pymdownx.emoji import TWEMOJI_SVG_CDN


class TestEmoji(util.MdCase):
    """Test extra raw HTML."""

    extension = ['pymdownx.emoji']
    extension_configs = {
        'pymdownx.emoji': {
            "emoji_index": emoji.twemoji,
            "emoji_generator": emoji.to_svg
        }
    }

    def test_material_svg_injection(self):
        """Test that we inject icons for all the Material icon types."""

        text = r'''
        We can use Material Icons :material-airplane:.

        We can also use Fontawesome Icons :fontawesome-solid-hand:.

        That's not all, we can also use Octicons :octicons-alert-16:.
        '''

        html = markdown.markdown(
            self.dedent(text, True),
            extensions=self.extension,
            extension_configs=self.extension_configs
        )

        soup = BeautifulSoup(html, 'html.parser')

        p = soup.select('p')
        self.assertTrue(len(p) == 3)
        self.assertTrue(p[0].select('span.twemoji > svg'))
        self.assertTrue(p[1].select('span.twemoji > svg'))
        self.assertTrue(p[2].select('span.twemoji > svg'))

    def test_twemoji(self):
        """Test that normal Twemoji emoji work."""

        self.check_markdown(
            ':smile:',
            '<p><img alt="\U0001f604" class="twemoji" src="{}1f604.svg" title=":smile:" /></p>'.format(TWEMOJI_SVG_CDN)  # noqa: E501
        )
