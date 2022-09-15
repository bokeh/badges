# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
import json
from datetime import date, timedelta

# External imports
import click

from . import get_badges_for_packages

__all__ = ("main",)

STYLES = ("plastic", "flat", "flat-square", "for-the-badge", "social")


@click.command(
    help="Generate shields.io badge URLs with monthly conda package download numbers"
)
@click.option(
    "--package",
    "-p",
    "packages",
    multiple=True,
    default=["bokeh"],
    show_default=True,
    help="Conda package name to generate a badge for",
)
@click.option(
    "--month",
    "-m",
    default=None,
    type=click.DateTime(formats=["%Y-%m"]),
    help="A month to collect data for expressed as YYYY-MM",
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
    default="conda",
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
    packages: list[str],
    month: date | None,
    color: str,
    style: str,
    label: str,
    logo: str,
) -> None:
    month = month or date.today().replace(day=1) - timedelta(days=1)
    print(
        json.dumps(
            get_badges_for_packages(packages, month, color, style, label, logo),
            indent=2,
        )
    )
