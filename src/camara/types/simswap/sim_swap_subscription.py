# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sim_swap_config import SimSwapConfig
from .sim_swap_protocol import SimSwapProtocol
from .sim_swap_subscription_event_type import SimSwapSubscriptionEventType

__all__ = ["SimSwapSubscription"]


class SimSwapSubscription(BaseModel):
    """Represents a event-type subscription."""

    id: str
    """
    The unique identifier of the subscription in the scope of the subscription
    manager. When this information is contained within an event notification, this
    concept SHALL be referred as subscriptionId as per Commonalities Event
    Notification Model.
    """

    config: SimSwapConfig
    """
    Implementation-specific configuration parameters needed by the subscription
    manager for acquiring events. In CAMARA we have predefined attributes like
    `subscriptionExpireTime` or `subscriptionMaxEvents` to limit subscription
    lifetime. Event type attributes must be defined in `subscriptionDetail`
    """

    protocol: SimSwapProtocol
    """Identifier of a delivery protocol. Only HTTP is allowed for now"""

    sink: str
    """The address to which events shall be delivered using the selected protocol."""

    types: List[SimSwapSubscriptionEventType]
    """Camara Event types eligible for subscription:

    - org.camaraproject.sim-swap-subscriptions.v0.swapped: receive a notification
      when a sim swap is performed on the line. Note: for the Commonalities
      meta-release v0.4 we enforce to have only event type per subscription then for
      following meta-release use of array MUST be decided at API project level.
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Date when the event subscription will expire.

    Only provided when `subscriptionExpireTime` is indicated by API client or Telco
    Operator has specific policy about that. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    starts_at: Optional[datetime] = FieldInfo(alias="startsAt", default=None)
    """
    Date when the event subscription will begin/began It must follow
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
      subscription is ended due to `SUBSCRIPTION_EXPIRED` event.
    - `DELETED`: Subscription is ended as deleted (no longer active). This status
      applies when subscription information is kept (i.e. subscription workflow is
      no longer active but its metainformation is kept).
    """
