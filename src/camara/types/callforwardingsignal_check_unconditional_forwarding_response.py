# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallforwardingsignalCheckUnconditionalForwardingResponse"]


class CallforwardingsignalCheckUnconditionalForwardingResponse(BaseModel):
    """
    resource containing the information about the Unconditional Call Forwarding Service for the given phone number (PhoneNumber)
    """

    active: Optional[bool] = None
    """Indicates if the unconditional call forwarding service is active."""
