"""Utilities."""
import sys
import os
import unittest
import textwrap
import markdown
import difflib

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

if sys.platform.startswith('win'):
    _PLATFORM = "windows"
elif sys.platform == "darwin":
    _PLATFORM = "osx"
else:
    _PLATFORM = "linux"


def is_win():  # pragma: no cover
    """Is Windows."""

    return _PLATFORM == "windows"


def is_linux():  # pragma: no cover
    """Is Linux."""

    return _PLATFORM == "linux"


def is_mac():  # pragma: no cover
    """Is macOS."""

    return _PLATFORM == "osx"


class MdCase(unittest.TestCase):
    """Markdown unittest test case base."""

    extension = []
    extension_configs = {}
    base = CURRENT_DIR

    def setUp(self):
        """Setup."""

        for k1, v1 in self.extension_configs.items():
            if v1 is not None:
                for k2, v2 in v1.items():
                    if isinstance(v2, str):
                        v1[k2] = v2.replace(
                            '{{BASE}}', self.base
                        ).replace(
                            '{{RELATIVE}}', CURRENT_DIR
                        )
            self.extension_configs[k1] = v1

        self.md = markdown.Markdown(extensions=self.extension, extension_configs=self.extension_configs)

    def dedent(self, text, strip=False):
        """Reduce indentation."""

        return textwrap.dedent(text).strip('\n') if strip else textwrap.dedent(text)

    def check_markdown(self, text, expected, dedent=False):
        """Check the markdown."""

        if dedent:
            # For markdown, beginning and ending new lines get stripped out with
            # no issues, but for HTML (expected), we need to trim.
            # If there are tests that are newline sensitive, it may make sense
            # to call dedent directly to control this.
            text = self.dedent(text)
            expected = self.dedent(expected, True)

        results = self.md.convert(text)

        diff = [
            l for l in difflib.unified_diff(
                expected.splitlines(True),
                results.splitlines(True),
                'Expected',
                'Actual',
                n=3
            )
        ]

        print(''.join(diff))
        self.assertTrue(not diff)
