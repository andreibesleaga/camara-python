# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sim_swap_protocol import SimSwapProtocol
from .sim_swap_config_param import SimSwapConfigParam
from .sim_swap_subscription_event_type import SimSwapSubscriptionEventType

__all__ = ["SubscriptionCreateParams", "SinkCredential"]


class SubscriptionCreateParams(TypedDict, total=False):
    config: Required[SimSwapConfigParam]
    """
    Implementation-specific configuration parameters needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime` or `subscriptionMaxEvents` to limit subscription
    lifetime. Event type attributes must be defined in `subscriptionDetail`
    """

    protocol: Required[SimSwapProtocol]
    """Identifier of a delivery protocol. Only HTTP is allowed for now"""

    sink: Required[str]
    """The address to which events shall be delivered using the selected protocol."""

    types: Required[List[SimSwapSubscriptionEventType]]
    """Camara Event types eligible for subscription:

    - org.camaraproject.sim-swap-subscriptions.v0.swapped: receive a notification
      when a sim swap is performed on the line.
    """

    sink_credential: Annotated[SinkCredential, PropertyInfo(alias="sinkCredential")]
    """
    A sink credential provides authentication or authorization information necessary
    to enable delivery of events to a target.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]


class SinkCredential(TypedDict, total=False):
    """
    A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    """

    credential_type: Required[
        Annotated[Literal["PLAIN", "ACCESSTOKEN", "REFRESHTOKEN"], PropertyInfo(alias="credentialType")]
    ]
    """The type of the credential.

    With the current API version the type MUST be set to ACCESSTOKEN.
    """
