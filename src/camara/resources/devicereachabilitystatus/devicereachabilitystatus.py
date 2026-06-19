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

__all__ = ["DevicereachabilitystatusResource", "AsyncDevicereachabilitystatusResource"]


class DevicereachabilitystatusResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Device Reachability Status Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevicereachabilitystatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return DevicereachabilitystatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicereachabilitystatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return DevicereachabilitystatusResourceWithStreamingResponse(self)


class AsyncDevicereachabilitystatusResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Device Reachability Status Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicereachabilitystatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicereachabilitystatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicereachabilitystatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncDevicereachabilitystatusResourceWithStreamingResponse(self)


class DevicereachabilitystatusResourceWithRawResponse:
    def __init__(self, devicereachabilitystatus: DevicereachabilitystatusResource) -> None:
        self._devicereachabilitystatus = devicereachabilitystatus

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Device Reachability Status Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._devicereachabilitystatus.subscriptions)


class AsyncDevicereachabilitystatusResourceWithRawResponse:
    def __init__(self, devicereachabilitystatus: AsyncDevicereachabilitystatusResource) -> None:
        self._devicereachabilitystatus = devicereachabilitystatus

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Device Reachability Status Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._devicereachabilitystatus.subscriptions)


class DevicereachabilitystatusResourceWithStreamingResponse:
    def __init__(self, devicereachabilitystatus: DevicereachabilitystatusResource) -> None:
        self._devicereachabilitystatus = devicereachabilitystatus

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Device Reachability Status Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._devicereachabilitystatus.subscriptions)


class AsyncDevicereachabilitystatusResourceWithStreamingResponse:
    def __init__(self, devicereachabilitystatus: AsyncDevicereachabilitystatusResource) -> None:
        self._devicereachabilitystatus = devicereachabilitystatus

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Device Reachability Status Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._devicereachabilitystatus.subscriptions)
