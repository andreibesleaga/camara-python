# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DeviceReachabilityStatusSubscriptionEventType"]

DeviceReachabilityStatusSubscriptionEventType: TypeAlias = Literal[
    "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-data",
    "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-sms",
    "org.camaraproject.device-reachability-status-subscriptions.v0.reachability-disconnected",
]
