# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .device_roaming_status_subscription import DeviceRoamingStatusSubscription

__all__ = ["SubscriptionListResponse"]

SubscriptionListResponse: TypeAlias = List[DeviceRoamingStatusSubscription]
