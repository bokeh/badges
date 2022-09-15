# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

# Standard library imports
from typing import TYPE_CHECKING, Any

# External imports
import dask.dataframe as dd

if TYPE_CHECKING:
    from datetime import date

__all__ = ("get_package_counts_for_month",)


BUCKET_BASE = "s3://anaconda-package-data/conda/hourly"

BUCKET_URL = "{bucket_base}/{year}/{month:02d}/{year}-{month:02d}-*.parquet"


def get_package_counts_for_month(month: date) -> Any:
    url = (
        BUCKET_URL.format(bucket_base=BUCKET_BASE, year=month.year, month=month.month),
    )
    counts = dd.read_parquet(
        url,
        storage_options={"anon": True},
        columns=("pkg_name", "counts"),
    )
    return counts.groupby("pkg_name").sum().compute()
