# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .device_location_protocol import DeviceLocationProtocol
from .device_location_area_param import DeviceLocationAreaParam
from .device_location_config_param import DeviceLocationConfigParam
from .device_location_device_param import DeviceLocationDeviceParam
from .device_location_subscription_event_type import DeviceLocationSubscriptionEventType

__all__ = ["SubscriptionCreateParams", "Config", "ConfigSubscriptionDetail", "SinkCredential"]


class SubscriptionCreateParams(TypedDict, total=False):
    config: Required[Config]
    """
    Implementation-specific configuration parameters are needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.
    """

    protocol: Required[DeviceLocationProtocol]
    """Identifier of a delivery protocol. Only HTTP is allowed for now."""

    sink: Required[str]
    """The address to which events shall be delivered using the selected protocol."""

    types: Required[List[DeviceLocationSubscriptionEventType]]
    """
    Camara Event types which are eligible to be delivered by this subscription.
    Note: As of now we enforce to have only event type per subscription.
    """

    sink_credential: Annotated[SinkCredential, PropertyInfo(alias="sinkCredential")]
    """
    A sink credential provides authentication or authorization information necessary
    to enable delivery of events to a target.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]


class ConfigSubscriptionDetail(TypedDict, total=False):
    """The detail of the requested event subscription."""

    area: Required[DeviceLocationAreaParam]
    """The geofencing area where the monitor is active.

    This area is specified by API consumers in the subscription request. The same
    area definition is included in event notifications without any modifications.
    """

    device: DeviceLocationDeviceParam
    """End-user device able to connect to a mobile network.

    Examples of devices include smartphones or IoT sensors/actuators.

    The developer can choose to provide the below specified device identifiers:

    - `ipv4Address`
    - `ipv6Address`
    - `phoneNumber`
    - `networkAccessIdentifier`

    NOTE1: the API provider might support only a subset of these options. The API
    consumer can provide multiple identifiers to be compatible across different API
    providers. In this case the identifiers MUST belong to the same device. Where
    more than one device identifier is provided, only one identifier will be
    selected by the implementation and this choice indicated to the API consumer in
    the response or event. NOTE2: as for this Commonalities release, we are
    enforcing that the networkAccessIdentifier is only part of the schema for
    future-proofing, and CAMARA does not currently allow its use. After the CAMARA
    meta-release work is concluded and the relevant issues are resolved, its use
    will need to be explicitly documented in the guidelines.
    """


class Config(DeviceLocationConfigParam, total=False):
    """
    Implementation-specific configuration parameters are needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.
    """

    subscription_detail: Required[Annotated[ConfigSubscriptionDetail, PropertyInfo(alias="subscriptionDetail")]]
    """The detail of the requested event subscription."""


class SinkCredential(TypedDict, total=False):
    """
    A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    """

    credential_type: Required[
        Annotated[Literal["PLAIN", "ACCESSTOKEN", "REFRESHTOKEN"], PropertyInfo(alias="credentialType")]
    ]
    """
    The type of the credential. Note: Type of the credential - MUST be set to
    ACCESSTOKEN for now
    """
