# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
from urllib.parse import urlencode

__all__ = ("get_shields_io_url", "STYLES")

STYLES = ("plastic", "flat", "flat-square", "for-the-badge", "social")


SHIELDS_URL = "https://img.shields.io/badge"


def get_shields_io_url(
    value: str, color: str, style: str, label: str, logo: str | None
) -> str:

    params = {"style": style}
    if logo is not None:
        params["logo"] = logo

    arguments = f"?{urlencode(params)}" if params else ""

    return f"{SHIELDS_URL}/{label}-{value}-{color}{arguments}"
