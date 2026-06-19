# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DeviceRoamingStatusSubscriptionEventType"]

DeviceRoamingStatusSubscriptionEventType: TypeAlias = Literal[
    "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-status",
    "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-on",
    "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-off",
    "org.camaraproject.device-roaming-status-subscriptions.v0.roaming-change-country",
]
