# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
from urllib.parse import quote, urlencode

__all__ = ("get_shields_io_url",)

SHIELDS_URL = "https://img.shields.io/badge"


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


def get_shields_io_url(
    downloads: int, color: str, style: str, label: str, logo: str | None
) -> str:
    dm = _nice(downloads)

    params = {"style": style}
    if logo is not None:
        params["logo"] = logo

    arguments = f"?{urlencode(params)}" if params else ""

    return f"{SHIELDS_URL}/{label}-{dm}-{color}{arguments}"
