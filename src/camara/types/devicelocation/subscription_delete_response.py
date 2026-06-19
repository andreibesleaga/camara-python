# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SubscriptionDeleteResponse"]


class SubscriptionDeleteResponse(BaseModel):
    """
    Response for an event-type subscription request managed asynchronously (Creation or Deletion).
    """

    id: str
    """
    The unique identifier of the subscription in the scope of the subscription
    manager. When this information is contained within an event notification, this
    concept SHALL be referred as subscriptionId as per Commonalities Event
    Notification Model.
    """
