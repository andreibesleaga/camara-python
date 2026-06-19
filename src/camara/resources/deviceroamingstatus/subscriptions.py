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
from ...types.deviceroamingstatus import (
    DeviceRoamingStatusProtocol,
    subscription_create_params,
)
from ...types.deviceroamingstatus.subscription_list_response import SubscriptionListResponse
from ...types.deviceroamingstatus.subscription_delete_response import SubscriptionDeleteResponse
from ...types.deviceroamingstatus.device_roaming_status_protocol import DeviceRoamingStatusProtocol
from ...types.deviceroamingstatus.device_roaming_status_config_param import DeviceRoamingStatusConfigParam
from ...types.deviceroamingstatus.device_roaming_status_subscription import DeviceRoamingStatusSubscription
from ...types.deviceroamingstatus.device_roaming_status_subscription_event_type import (
    DeviceRoamingStatusSubscriptionEventType,
)

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    """Device Roaming Status Subscriptions"""

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: DeviceRoamingStatusConfigParam,
        protocol: DeviceRoamingStatusProtocol,
        sink: str,
        types: List[DeviceRoamingStatusSubscriptionEventType],
        sink_credential: subscription_create_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceRoamingStatusSubscription:
        """
        Create a device roaming status event subscription for a device

        Args:
          config: Implementation-specific configuration parameters needed by the subscription
              manager for acquiring events. In CAMARA we have predefined attributes like
              `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent` Specific event
              type attributes must be defined in `subscriptionDetail` Note: if a request is
              performed for several event type, all subscribed event will use same `config`
              parameters.

          protocol: Identifier of a delivery protocol. Only HTTP is allowed for now

          sink: The address to which events shall be delivered using the selected protocol.

          types: Camara Event types eligible to be delivered by this subscription. Note: for the
              current Commonalities version (v0.5) only one event type per subscription is
              allowed, yet in the following releases use of array of event types SHALL be
              specified without changing this definition.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/deviceroamingstatus/subscriptions",
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
            cast_to=DeviceRoamingStatusSubscription,
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
    ) -> DeviceRoamingStatusSubscription:
        """
        retrieve device roaming status subscription information for a given
        subscription.

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
            path_template("/deviceroamingstatus/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceRoamingStatusSubscription,
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
        Retrieve a list of device roaming status event subscription(s)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._get(
            "/deviceroamingstatus/subscriptions",
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
        Delete a given device-roaming-status subscription by ID

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
            path_template("/deviceroamingstatus/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    """Device Roaming Status Subscriptions"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: DeviceRoamingStatusConfigParam,
        protocol: DeviceRoamingStatusProtocol,
        sink: str,
        types: List[DeviceRoamingStatusSubscriptionEventType],
        sink_credential: subscription_create_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceRoamingStatusSubscription:
        """
        Create a device roaming status event subscription for a device

        Args:
          config: Implementation-specific configuration parameters needed by the subscription
              manager for acquiring events. In CAMARA we have predefined attributes like
              `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent` Specific event
              type attributes must be defined in `subscriptionDetail` Note: if a request is
              performed for several event type, all subscribed event will use same `config`
              parameters.

          protocol: Identifier of a delivery protocol. Only HTTP is allowed for now

          sink: The address to which events shall be delivered using the selected protocol.

          types: Camara Event types eligible to be delivered by this subscription. Note: for the
              current Commonalities version (v0.5) only one event type per subscription is
              allowed, yet in the following releases use of array of event types SHALL be
              specified without changing this definition.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/deviceroamingstatus/subscriptions",
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
            cast_to=DeviceRoamingStatusSubscription,
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
    ) -> DeviceRoamingStatusSubscription:
        """
        retrieve device roaming status subscription information for a given
        subscription.

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
            path_template("/deviceroamingstatus/subscriptions/{subscription_id}", subscription_id=subscription_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceRoamingStatusSubscription,
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
        Retrieve a list of device roaming status event subscription(s)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._get(
            "/deviceroamingstatus/subscriptions",
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
        Delete a given device-roaming-status subscription by ID

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
            path_template("/deviceroamingstatus/subscriptions/{subscription_id}", subscription_id=subscription_id),
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
