# Changelog

## 1.3.1

- **FIX**: Better deprecation warning.

## 1.3

- **NEW**: The final release. `mkdocs-material` (version 9.4) now has this library's logic built-in making this library
  obsolete. Users should migrate to using `mkdocs-material`'s `material.extensions.emoji.twemoji` and
  `material.extensions.emoji.to_svg` in place of the respective `materialx.emoji.twemoji` and `materialx.emoji.to_svg`
  functions.

## 1.2

- **NEW**: Add official support for Python 3.11 and 3.12.
- **NEW**: Remove support for Python 3.7.
- **FIX**: Update to support latest Material.

## 1.1.1

- **FIX**: Properly handle special glob characters in path.

## 1.1

- **NEW**: Drop Python 3.6 and officially support 3.10.
- **NEW**: Cache emoji table to reduce build times.

## 1.0.3

- **FIX**: Remove version check which is not compatible with Material Insiders. Material will completely be responsible
  for ensuring the correct version of `mkdocs-material-extensions`.

## 1.0.2

- **FIX**: No longer specify `mkdocs-material` as a dependency as `mkdocs-material` specifies these extensions as a
  dependency. This created a circular dependency. While `pip` has no issues with such scenarios, this created issues
  for some versioning packages. `mkdocs-material` (the only package this works with) will now manage which version of
  `mkdocs-material-extensions` it needs.

## 1.0.1

- **FIX**: Ensure we don't modify the original icon path setting.

## 1.0

- **NEW**: First stable release.
