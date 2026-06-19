# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .connected_network_type_subscription import ConnectedNetworkTypeSubscription

__all__ = ["SubscriptionListResponse"]

SubscriptionListResponse: TypeAlias = List[ConnectedNetworkTypeSubscription]
