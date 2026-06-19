# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionDeleteResponse"]


class SubscriptionDeleteResponse(BaseModel):
    """
    Response for a event-type subscription request managed asynchronously
    (Creation or Deletion)
    """

    subscription_id: Optional[str] = FieldInfo(alias="subscriptionId", default=None)
    """
    When this information is contained within an event notification, it SHALL be
    referred to as `subscriptionId` as per the Commonalities Event Notification
    Model.
    """
