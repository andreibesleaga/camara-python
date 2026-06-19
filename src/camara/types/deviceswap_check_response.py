# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeviceswapCheckResponse"]


class DeviceswapCheckResponse(BaseModel):
    swapped: bool
    """
    Indicates whether the device has been swapped during the period within the
    provided age.
    """
