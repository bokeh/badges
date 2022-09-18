# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
import json

# External imports
import click

from ..shields import STYLES
from . import get_badges_for_tags

__all__ = ("main",)


@click.command(help="Generate shields.io badge URLs with total SQ questions for a tag")
@click.option(
    "--tag",
    "-t",
    "tags",
    multiple=True,
    default=["bokeh"],
    show_default=True,
    help="SO tag to generate a badge for",
)
@click.option(
    "--color",
    "-c",
    default="goldenrod",
    show_default=True,
    help="Highlight color for the badge",
)
@click.option(
    "--style",
    "-s",
    type=click.Choice(STYLES),
    default="for-the-badge",
    show_default=True,
    help="Style type for shields.io badge",
)
@click.option(
    "--label",
    "-l",
    default="stackoverflow",
    show_default=True,
    help="Label for the badge. If '__name__' is passed, use package names for each label",
)
@click.option(
    "--logo",
    default=None,
    show_default=True,
    help="A shields.io named logo for the badge",
)
def main(
    tags: list[str],
    color: str,
    style: str,
    label: str,
    logo: str,
) -> None:
    print(json.dumps(get_badges_for_tags(tags, color, style, label, logo), indent=2))
