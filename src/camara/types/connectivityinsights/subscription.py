# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .config import Config
from .protocol import Protocol
from ..._models import BaseModel
from .event_type import EventType

__all__ = ["Subscription"]


class Subscription(BaseModel):
    """Represents a event-type subscription."""

    config: Config
    """
    Implementation-specific configuration parameters needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent` Specific event
    type attributes must be defined in `subscriptionDetail` Note: if a request is
    performed for several event type, all subscribed event will use same `config`
    parameters.
    """

    protocol: Protocol
    """Identifier of a delivery protocol. Only HTTP is allowed for now"""

    sink: str
    """The address to which events shall be delivered using the selected protocol."""

    starts_at: datetime = FieldInfo(alias="startsAt")
    """
    Date when the event subscription will begin/began It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    types: List[EventType]
    """Camara Event types eligible to be delivered by this subscription."""

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Date when the event subscription will expire.

    Only provided when `subscriptionExpireTime` is indicated by API client or Telco
    Operator has specific policy about that. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    status: Optional[Literal["ACTIVATION_REQUESTED", "ACTIVE", "EXPIRED", "DEACTIVE", "DELETED"]] = None
    """
    Current status of the subscription - Management of Subscription State engine is
    not mandatory for now. Note not all statuses may be considered to be
    implemented. Details:

    - `ACTIVATION_REQUESTED`: Subscription creation (POST) is triggered but
      subscription creation process is not finished yet.
    - `ACTIVE`: Subscription creation process is completed. Subscription is fully
      operative.
    - `DEACTIVE`: Subscription is temporarily inactive, but its workflow logic is
      not deleted.
    - `EXPIRED`: Subscription is ended (no longer active). This status applies when
      subscription is ended due to `SUBSCRIPTION_EXPIRED` or `ACCESS_TOKEN_EXPIRED`
      event.
    - `DELETED`: Subscription is ended as deleted (no longer active). This status
      applies when subscription information is kept (i.e. subscription workflow is
      no longer active but its metainformation is kept).
    """

    subscription_id: Optional[str] = FieldInfo(alias="subscriptionId", default=None)
    """
    When this information is contained within an event notification, it SHALL be
    referred to as `subscriptionId` as per the Commonalities Event Notification
    Model.
    """
