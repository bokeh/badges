# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
from typing import TYPE_CHECKING
from urllib.parse import quote

from ..shields import get_shields_io_url
from .data import get_package_counts_for_month

if TYPE_CHECKING:
    from datetime import date


__all__ = ("get_badges_for_packages",)


def _nice(downloads: int) -> str:
    if downloads > 1e9:
        num, unit = f"{downloads/1e9:0.1f}".rstrip(".0"), "B"
    elif downloads > 1e6:
        num, unit = f"{downloads/1e6:0.1f}".rstrip(".0"), "M"
    elif downloads > 1e3:
        num, unit = f"{int(downloads/1e3)}", "k"
    else:
        num, unit = f"{downloads}", ""

    return quote(f"{num}{unit}/month", safe="")


def get_badges_for_packages(
    packages: list[str], month: date, color: str, style: str, label: str, logo: str
) -> dict[str, str]:
    counts_by_package = get_package_counts_for_month(month)

    result = {}

    for package in packages:
        downloads = _nice(counts_by_package.counts.loc[package])
        result[package] = get_shields_io_url(downloads, color, style, label, logo)

    return result
