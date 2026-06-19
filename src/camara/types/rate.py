# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Rate"]


class Rate(BaseModel):
    """Specification of rate"""

    unit: Optional[Literal["bps", "kbps", "Mbps", "Gbps", "Tbps"]] = None
    """Units of rate"""

    value: Optional[int] = None
    """Quantity of rate"""
