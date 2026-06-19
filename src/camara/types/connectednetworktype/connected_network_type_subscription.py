# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .connected_network_type_config import ConnectedNetworkTypeConfig
from .connected_network_type_protocol import ConnectedNetworkTypeProtocol
from .connected_network_type_subscription_event_type import ConnectedNetworkTypeSubscriptionEventType

__all__ = ["ConnectedNetworkTypeSubscription"]


class ConnectedNetworkTypeSubscription(BaseModel):
    """Represents a event-type subscription."""

    id: str
    """
    The unique identifier of the subscription in the scope of the subscription
    manager. When this information is contained within an event notification, this
    concept SHALL be referred as subscriptionId as per Commonalities Event
    Notification Model.
    """

    config: ConnectedNetworkTypeConfig
    """
    Implementation-specific configuration parameters needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent` Specific event
    type attributes must be defined in `subscriptionDetail` Note: if a request is
    performed for several event type, all subscribed event will use same `config`
    parameters.
    """

    protocol: ConnectedNetworkTypeProtocol
    """Identifier of a delivery protocol. Only HTTP is allowed for now"""

    sink: str
    """The address to which events shall be delivered using the selected protocol."""

    types: List[ConnectedNetworkTypeSubscriptionEventType]
    """
    Camara Event types eligible to be delivered by this subscription. Note: For the
    current Commonalities API design guidelines, only one event type per
    subscription is allowed
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Date when the event subscription will expire.

    Only provided when `subscriptionExpireTime` is indicated by API client or Telco
    Operator has specific policy about that. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
    allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z)
    """

    starts_at: Optional[datetime] = FieldInfo(alias="startsAt", default=None)
    """
    Date when the event subscription will begin/began It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
    allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z)
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
