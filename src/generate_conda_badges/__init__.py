# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
from typing import TYPE_CHECKING

from .data import get_package_counts_for_month
from .shields import get_shields_io_url

if TYPE_CHECKING:
    from datetime import date


__all__ = ("get_badges_for_packages",)


def get_badges_for_packages(
    packages: list[str], month: date, color: str, style: str, label: str, logo: str
) -> dict[str, str]:
    counts_by_package = get_package_counts_for_month(month)

    result = {}

    for package in packages:
        downloads = counts_by_package.counts.loc[package]
        result[package] = get_shields_io_url(downloads, color, style, label, logo)

    return result
