# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .device_location_subscription import DeviceLocationSubscription

__all__ = ["SubscriptionListResponse"]

SubscriptionListResponse: TypeAlias = List[DeviceLocationSubscription]
