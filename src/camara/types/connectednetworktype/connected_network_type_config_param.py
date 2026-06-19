# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ConnectedNetworkTypeConfigParam",
    "SubscriptionDetail",
    "SubscriptionDetailDevice",
    "SubscriptionDetailDeviceIpv4Address",
]


class SubscriptionDetailDeviceIpv4Address(TypedDict, total=False):
    """
    The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object)

    In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone.
    """

    private_address: Annotated[str, PropertyInfo(alias="privateAddress")]
    """A single IPv4 address with no subnet mask"""

    public_address: Annotated[str, PropertyInfo(alias="publicAddress")]
    """A single IPv4 address with no subnet mask"""

    public_port: Annotated[int, PropertyInfo(alias="publicPort")]
    """TCP or UDP port number"""


class SubscriptionDetailDevice(TypedDict, total=False):
    """End-user equipment able to connect to a mobile network.

    Examples of devices include smartphones or IoT sensors/actuators.

    The developer can choose to provide the below specified device identifiers:

    * `ipv4Address`
    * `ipv6Address`
    * `phoneNumber`
    * `networkAccessIdentifier`

    NOTE: the MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    """

    ipv4_address: Annotated[SubscriptionDetailDeviceIpv4Address, PropertyInfo(alias="ipv4Address")]
    """
    The device should be identified by either the public (observed) IP address and
    port as seen by the application server, or the private (local) and any public
    (observed) IP addresses in use by the device (this information can be obtained
    by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use)
    then the same address should be specified for both publicAddress and
    privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and
    publicPort, or separately by its allocated IPv6 address (field ipv6Address of
    the Device object)

    In all cases, publicAddress must be specified, along with at least one of either
    privateAddress or publicPort, dependent upon which is known. In general, mobile
    devices cannot be identified by their public IPv4 address alone.
    """

    ipv6_address: Annotated[str, PropertyInfo(alias="ipv6Address")]
    """
    The device should be identified by the observed IPv6 address, or by any single
    IPv6 address from within the subnet allocated to the device (e.g. adding ::0 to
    the /64 prefix).
    """

    network_access_identifier: Annotated[str, PropertyInfo(alias="networkAccessIdentifier")]
    """A public identifier addressing a subscription in a mobile network.

    In 3GPP terminology, it corresponds to the GPSI formatted with the External
    Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone
    number, the network access identifier is not subjected to portability ruling in
    force, and is individually managed by each operator.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """


class SubscriptionDetail(TypedDict, total=False):
    """The detail of the requested event subscription."""

    device: SubscriptionDetailDevice
    """End-user equipment able to connect to a mobile network.

    Examples of devices include smartphones or IoT sensors/actuators.

    The developer can choose to provide the below specified device identifiers:

    - `ipv4Address`
    - `ipv6Address`
    - `phoneNumber`
    - `networkAccessIdentifier`

    NOTE: the MNO might support only a subset of these options. The API invoker can
    provide multiple identifiers to be compatible across different MNOs. In this
    case the identifiers MUST belong to the same device.
    """


class ConnectedNetworkTypeConfigParam(TypedDict, total=False):
    """
    Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`
    Specific event type attributes must be defined in `subscriptionDetail`
    Note: if a request is performed for several event type, all subscribed event will use same `config` parameters.
    """

    subscription_detail: Required[Annotated[SubscriptionDetail, PropertyInfo(alias="subscriptionDetail")]]
    """The detail of the requested event subscription."""

    initial_event: Annotated[bool, PropertyInfo(alias="initialEvent")]
    """
    Set to `true` by API consumer if consumer wants to get an event as soon as the
    subscription is created and current situation reflects event request. Example:
    Consumer request area entered event. If consumer sets initialEvent to true and
    device is already in the geofence, an event is triggered
    """

    subscription_expire_time: Annotated[
        Union[str, datetime], PropertyInfo(alias="subscriptionExpireTime", format="iso8601")
    ]
    """
    The subscription expiration time (in date-time format) requested by the API
    consumer.
    """

    subscription_max_events: Annotated[int, PropertyInfo(alias="subscriptionMaxEvents")]
    """
    Identifies the maximum number of event reports to be generated (>=1) requested
    by the API consumer - Once this number is reached, the subscription ends.
    """
