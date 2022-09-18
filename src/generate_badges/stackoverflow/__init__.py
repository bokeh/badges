# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
import json
from urllib.parse import quote

# External imports
import requests

from ..shields import get_shields_io_url

BASE_URL = "https://api.stackexchange.com/2.3"

# just total, ref: https://api.stackexchange.com/docs/questions
FILTER = "!)EyhHQ0RGE(-RGC3maupgc*8RQ*aCMk2jnmk)oq5YfUUQ1N94"

QUERY = f"{BASE_URL}/questions?tagged={{tag}}&site=stackoverflow&filter={FILTER}"


def _nice(downloads: int) -> str:
    if downloads > 1e3:
        num, unit = f"{downloads/1e3:0.1f}", "k"
    else:
        num, unit = f"{downloads}", ""

    return quote(f"{num}{unit}", safe="")


def get_badges_for_tags(
    tags: list[str], color: str, style: str, label: str, logo: str
) -> dict[str, str]:
    result = {}

    for tag in tags:
        posts = int(json.loads(requests.get(QUERY.format(tag=tag)).text)["total"])
        result[tag] = get_shields_io_url(_nice(posts), color, style, label, logo)

    return result
