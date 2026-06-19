# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .protocol import Protocol
from .event_type import EventType
from .config_param import ConfigParam

__all__ = ["SubscriptionCreateParams", "SinkCredential"]


class SubscriptionCreateParams(TypedDict, total=False):
    config: Required[ConfigParam]
    """
    Implementation-specific configuration parameters needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent` Specific event
    type attributes must be defined in `subscriptionDetail` Note: if a request is
    performed for several event type, all subscribed event will use same `config`
    parameters.
    """

    protocol: Required[Protocol]
    """Identifier of a delivery protocol. Only HTTP is allowed for now"""

    sink: Required[str]
    """The address to which events shall be delivered using the selected protocol."""

    types: Required[List[EventType]]
    """Camara Event types eligible to be delivered by this subscription."""

    sink_credential: Annotated[SinkCredential, PropertyInfo(alias="sinkCredential")]
    """A sink credential provides authentication or authorization information"""

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]


class SinkCredential(TypedDict, total=False):
    """A sink credential provides authentication or authorization information"""

    credential_type: Required[
        Annotated[Literal["PLAIN", "ACCESSTOKEN", "REFRESHTOKEN"], PropertyInfo(alias="credentialType")]
    ]
    """
    The type of the credential. Note: Type of the credential - MUST be set to
    ACCESSTOKEN for now
    """
