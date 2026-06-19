# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .device_reachability_status_subscription import DeviceReachabilityStatusSubscription

__all__ = ["SubscriptionListResponse"]

SubscriptionListResponse: TypeAlias = List[DeviceReachabilityStatusSubscription]
