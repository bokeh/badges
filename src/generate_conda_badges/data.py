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


BUCKET_BASE = "s3://anaconda-package-data/"

MONTHLY_URL = BUCKET_BASE + "conda/monthly/{year}/{year}-{month:02d}.parquet"


def get_package_counts_for_month(month: date) -> Any:
    counts = dd.read_parquet(
        MONTHLY_URL.format(year=month.year, month=month.month),
        storage_options={"anon": True},
        columns=("pkg_name", "counts"),
    )
    return counts.groupby("pkg_name").sum().compute()
