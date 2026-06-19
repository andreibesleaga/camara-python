# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["DeviceroamingstatusResource", "AsyncDeviceroamingstatusResource"]


class DeviceroamingstatusResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Device Roaming Status Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeviceroamingstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return DeviceroamingstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeviceroamingstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return DeviceroamingstatusResourceWithStreamingResponse(self)


class AsyncDeviceroamingstatusResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Device Roaming Status Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeviceroamingstatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeviceroamingstatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeviceroamingstatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncDeviceroamingstatusResourceWithStreamingResponse(self)


class DeviceroamingstatusResourceWithRawResponse:
    def __init__(self, deviceroamingstatus: DeviceroamingstatusResource) -> None:
        self._deviceroamingstatus = deviceroamingstatus

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Device Roaming Status Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._deviceroamingstatus.subscriptions)


class AsyncDeviceroamingstatusResourceWithRawResponse:
    def __init__(self, deviceroamingstatus: AsyncDeviceroamingstatusResource) -> None:
        self._deviceroamingstatus = deviceroamingstatus

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Device Roaming Status Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._deviceroamingstatus.subscriptions)


class DeviceroamingstatusResourceWithStreamingResponse:
    def __init__(self, deviceroamingstatus: DeviceroamingstatusResource) -> None:
        self._deviceroamingstatus = deviceroamingstatus

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Device Roaming Status Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._deviceroamingstatus.subscriptions)


class AsyncDeviceroamingstatusResourceWithStreamingResponse:
    def __init__(self, deviceroamingstatus: AsyncDeviceroamingstatusResource) -> None:
        self._deviceroamingstatus = deviceroamingstatus

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Device Roaming Status Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._deviceroamingstatus.subscriptions)
