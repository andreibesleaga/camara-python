# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.devicelocation import DeviceLocationProtocol, subscription_create_params
from ...types.devicelocation.device_location_protocol import DeviceLocationProtocol
from ...types.devicelocation.subscription_list_response import SubscriptionListResponse
from ...types.devicelocation.device_location_subscription import DeviceLocationSubscription
from ...types.devicelocation.subscription_delete_response import SubscriptionDeleteResponse
from ...types.devicelocation.device_location_subscription_event_type import DeviceLocationSubscriptionEventType

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    """Device Geofencing Subscriptions"""

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: subscription_create_params.Config,
        protocol: DeviceLocationProtocol,
        sink: str,
        types: List[DeviceLocationSubscriptionEventType],
        sink_credential: subscription_create_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceLocationSubscription:
        """
        Create a subscription for a device to receive notifications when the device
        enters or exits a specified area.

        Args:
          config: Implementation-specific configuration parameters are needed by the subscription
              manager for acquiring events. In CAMARA we have predefined attributes like
              `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.

          protocol: Identifier of a delivery protocol. Only HTTP is allowed for now.

          sink: The address to which events shall be delivered using the selected protocol.

          types: Camara Event types which are eligible to be delivered by this subscription.
              Note: As of now we enforce to have only event type per subscription.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/devicelocation/subscriptions",
            body=maybe_transform(
                {
                    "config": config,
                    "protocol": protocol,
                    "sink": sink,
                    "types": types,
                    "sink_credential": sink_credential,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceLocationSubscription,
        )

    def retrieve(
        self,
        subscription_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceLocationSubscription:
        """
        Retrieve Geofencing subscription information for a given subscription ID.

        Args:
          subscription_id: The unique identifier of the subscription in the scope of the subscription
              manager. When this information is contained within an event notification, this
              concept SHALL be referred as subscriptionId as per Commonalities Event
              Notification Model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._get(
            path_template("/devicelocation/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceLocationSubscription,
        )

    def list(
        self,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve a list of geofencing event subscription(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._get(
            "/devicelocation/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    def delete(
        self,
        subscription_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDeleteResponse:
        """
        Delete a given Geofencing subscription.

        Args:
          subscription_id: The unique identifier of the subscription in the scope of the subscription
              manager. When this information is contained within an event notification, this
              concept SHALL be referred as subscriptionId as per Commonalities Event
              Notification Model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._delete(
            path_template("/devicelocation/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    """Device Geofencing Subscriptions"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: subscription_create_params.Config,
        protocol: DeviceLocationProtocol,
        sink: str,
        types: List[DeviceLocationSubscriptionEventType],
        sink_credential: subscription_create_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceLocationSubscription:
        """
        Create a subscription for a device to receive notifications when the device
        enters or exits a specified area.

        Args:
          config: Implementation-specific configuration parameters are needed by the subscription
              manager for acquiring events. In CAMARA we have predefined attributes like
              `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.

          protocol: Identifier of a delivery protocol. Only HTTP is allowed for now.

          sink: The address to which events shall be delivered using the selected protocol.

          types: Camara Event types which are eligible to be delivered by this subscription.
              Note: As of now we enforce to have only event type per subscription.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/devicelocation/subscriptions",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "protocol": protocol,
                    "sink": sink,
                    "types": types,
                    "sink_credential": sink_credential,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceLocationSubscription,
        )

    async def retrieve(
        self,
        subscription_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceLocationSubscription:
        """
        Retrieve Geofencing subscription information for a given subscription ID.

        Args:
          subscription_id: The unique identifier of the subscription in the scope of the subscription
              manager. When this information is contained within an event notification, this
              concept SHALL be referred as subscriptionId as per Commonalities Event
              Notification Model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._get(
            path_template("/devicelocation/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceLocationSubscription,
        )

    async def list(
        self,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve a list of geofencing event subscription(s).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._get(
            "/devicelocation/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    async def delete(
        self,
        subscription_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDeleteResponse:
        """
        Delete a given Geofencing subscription.

        Args:
          subscription_id: The unique identifier of the subscription in the scope of the subscription
              manager. When this information is contained within an event notification, this
              concept SHALL be referred as subscriptionId as per Commonalities Event
              Notification Model.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._delete(
            path_template("/devicelocation/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
