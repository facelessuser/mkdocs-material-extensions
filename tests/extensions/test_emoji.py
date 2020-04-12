"""Test emoji indexes and generators."""
from .. import util
from materialx import emoji


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

        self.check_markdown(
            r'''
            We can use Material Icons :material-airplane:.

            We can also use Fontawesome Icons :fontawesome-solid-ambulance:.

            That's not all, we can also use Octicons :octicons-octoface:.
            ''',
            r'''
            <p>We can use Material Icons <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21,16V14L13,9V3.5A1.5,1.5 0 0,0 11.5,2A1.5,1.5 0 0,0 10,3.5V9L2,14V16L10,13.5V19L8,20.5V22L11.5,21L15,22V20.5L13,19V13.5L21,16Z" /></svg></span>.</p>
            <p>We can also use Fontawesome Icons <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M624 352h-16V243.9c0-12.7-5.1-24.9-14.1-33.9L494 110.1c-9-9-21.2-14.1-33.9-14.1H416V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v320c0 26.5 21.5 48 48 48h16c0 53 43 96 96 96s96-43 96-96h128c0 53 43 96 96 96s96-43 96-96h48c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zM160 464c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm144-248c0 4.4-3.6 8-8 8h-56v56c0 4.4-3.6 8-8 8h-48c-4.4 0-8-3.6-8-8v-56h-56c-4.4 0-8-3.6-8-8v-48c0-4.4 3.6-8 8-8h56v-56c0-4.4 3.6-8 8-8h48c4.4 0 8 3.6 8 8v56h56c4.4 0 8 3.6 8 8v48zm176 248c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm80-208H416V144h44.1l99.9 99.9V256z"/></svg></span>.</p>
            <p>That's not all, we can also use Octicons <span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg></span>.</p>
            ''',  # noqa: E501
            True
        )

    def test_twemoji(self):
        """Test that normal Twemoji emoji work."""

        self.check_markdown(
            ':smile:',
            '<p><img alt="\U0001f604" class="twemoji" src="https://twemoji.maxcdn.com/v/latest/svg/1f604.svg" title=":smile:" /></p>'  # noqa: E501
        )
