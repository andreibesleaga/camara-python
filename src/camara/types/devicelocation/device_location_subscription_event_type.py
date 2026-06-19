# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DeviceLocationSubscriptionEventType"]

DeviceLocationSubscriptionEventType: TypeAlias = Literal[
    "org.camaraproject.geofencing-subscriptions.v0.area-entered",
    "org.camaraproject.geofencing-subscriptions.v0.area-left",
]
