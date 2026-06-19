# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Duration"]


class Duration(BaseModel):
    """Specification of duration"""

    unit: Optional[Literal["Days", "Hours", "Minutes", "Seconds", "Milliseconds", "Microseconds", "Nanoseconds"]] = None
    """Units of time"""

    value: Optional[int] = None
    """Quantity of duration"""
