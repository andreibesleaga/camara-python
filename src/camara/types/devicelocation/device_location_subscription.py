# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .device_location_area import DeviceLocationArea
from .device_location_config import DeviceLocationConfig
from .device_location_device import DeviceLocationDevice
from .device_location_protocol import DeviceLocationProtocol
from .device_location_subscription_event_type import DeviceLocationSubscriptionEventType

__all__ = ["DeviceLocationSubscription", "Config", "ConfigSubscriptionDetail"]


class ConfigSubscriptionDetail(BaseModel):
    """The detail of the event subscription granted by the implementation."""

    area: DeviceLocationArea
    """The geofencing area where the monitor is active.

    This area is specified by API consumers in the subscription request. The same
    area definition is included in event notifications without any modifications.
    """

    device: Optional[DeviceLocationDevice] = None
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


class Config(DeviceLocationConfig):
    """
    Implementation-specific configuration parameters are needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.
    """

    subscription_detail: ConfigSubscriptionDetail = FieldInfo(alias="subscriptionDetail")
    """The detail of the event subscription granted by the implementation."""


class DeviceLocationSubscription(BaseModel):
    """Represents a event-type subscription."""

    id: str
    """
    The unique identifier of the subscription in the scope of the subscription
    manager. When this information is contained within an event notification, this
    concept SHALL be referred as subscriptionId as per Commonalities Event
    Notification Model.
    """

    config: Config
    """
    Implementation-specific configuration parameters are needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.
    """

    protocol: DeviceLocationProtocol
    """Identifier of a delivery protocol. Only HTTP is allowed for now."""

    sink: str
    """The address to which events shall be delivered using the selected protocol."""

    starts_at: datetime = FieldInfo(alias="startsAt")
    """
    Date when the event subscription will begin/began It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    types: List[DeviceLocationSubscriptionEventType]
    """
    Camara Event types eligible to be delivered by this subscription. Note: As of
    now we enforce to have only event type per subscription.
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Date when the event subscription will expire.

    Only provided when `subscriptionExpireTime` is indicated by API client or Telco
    Operator has specific policy about that. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    status: Optional[Literal["ACTIVATION_REQUESTED", "ACTIVE", "EXPIRED", "INACTIVE", "DELETED"]] = None
    """
    Current status of the subscription - Management of Subscription State engine is
    not mandatory for now. Note not all statuses may be considered to be
    implemented. Details:

    - `ACTIVATION_REQUESTED`: Subscription creation (POST) is triggered but
      subscription creation process is not finished yet.
    - `ACTIVE`: Subscription creation process is completed. Subscription is fully
      operative.
    - `INACTIVE`: Subscription is temporarily inactive, but its workflow logic is
      not deleted.
    - `EXPIRED`: Subscription is ended (no longer active). This status applies when
      subscription is ended due to `SUBSCRIPTION_EXPIRED` or `ACCESS_TOKEN_EXPIRED`
      event.
    - `DELETED`: Subscription is ended as deleted (no longer active). This status
      applies when subscription information is kept (i.e. subscription workflow is
      no longer active but its meta-information is kept).
    """
