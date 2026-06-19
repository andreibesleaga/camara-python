# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    callforwardingsignal_check_active_forwardings_params,
    callforwardingsignal_check_unconditional_forwarding_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.callforwardingsignal_check_active_forwardings_response import (
    CallforwardingsignalCheckActiveForwardingsResponse,
)
from ..types.callforwardingsignal_check_unconditional_forwarding_response import (
    CallforwardingsignalCheckUnconditionalForwardingResponse,
)

__all__ = ["CallforwardingsignalResource", "AsyncCallforwardingsignalResource"]


class CallforwardingsignalResource(SyncAPIResource):
    """Call Forwarding Signal"""

    @cached_property
    def with_raw_response(self) -> CallforwardingsignalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return CallforwardingsignalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallforwardingsignalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return CallforwardingsignalResourceWithStreamingResponse(self)

    def check_active_forwardings(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallforwardingsignalCheckActiveForwardingsResponse:
        """
        This endpoint provides information about which type of call forwarding service
        is active. More than one service can be active, e.g. conditional and
        unconditional. This endpoint exceeds the main scope of the Call Forwarding
        Signal API, for this reason an error code 501 can be returned.

        Args:
          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/callforwardingsignal/call-forwardings",
            body=maybe_transform(
                {"phone_number": phone_number},
                callforwardingsignal_check_active_forwardings_params.CallforwardingsignalCheckActiveForwardingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallforwardingsignalCheckActiveForwardingsResponse,
        )

    def check_unconditional_forwarding(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallforwardingsignalCheckUnconditionalForwardingResponse:
        """
        This endpoint provides information about the status of the unconditional call
        forwarding, being active or not.

        Args:
          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/callforwardingsignal/unconditional-call-forwardings",
            body=maybe_transform(
                {"phone_number": phone_number},
                callforwardingsignal_check_unconditional_forwarding_params.CallforwardingsignalCheckUnconditionalForwardingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallforwardingsignalCheckUnconditionalForwardingResponse,
        )


class AsyncCallforwardingsignalResource(AsyncAPIResource):
    """Call Forwarding Signal"""

    @cached_property
    def with_raw_response(self) -> AsyncCallforwardingsignalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallforwardingsignalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallforwardingsignalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncCallforwardingsignalResourceWithStreamingResponse(self)

    async def check_active_forwardings(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallforwardingsignalCheckActiveForwardingsResponse:
        """
        This endpoint provides information about which type of call forwarding service
        is active. More than one service can be active, e.g. conditional and
        unconditional. This endpoint exceeds the main scope of the Call Forwarding
        Signal API, for this reason an error code 501 can be returned.

        Args:
          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/callforwardingsignal/call-forwardings",
            body=await async_maybe_transform(
                {"phone_number": phone_number},
                callforwardingsignal_check_active_forwardings_params.CallforwardingsignalCheckActiveForwardingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallforwardingsignalCheckActiveForwardingsResponse,
        )

    async def check_unconditional_forwarding(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallforwardingsignalCheckUnconditionalForwardingResponse:
        """
        This endpoint provides information about the status of the unconditional call
        forwarding, being active or not.

        Args:
          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/callforwardingsignal/unconditional-call-forwardings",
            body=await async_maybe_transform(
                {"phone_number": phone_number},
                callforwardingsignal_check_unconditional_forwarding_params.CallforwardingsignalCheckUnconditionalForwardingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallforwardingsignalCheckUnconditionalForwardingResponse,
        )


class CallforwardingsignalResourceWithRawResponse:
    def __init__(self, callforwardingsignal: CallforwardingsignalResource) -> None:
        self._callforwardingsignal = callforwardingsignal

        self.check_active_forwardings = to_raw_response_wrapper(
            callforwardingsignal.check_active_forwardings,
        )
        self.check_unconditional_forwarding = to_raw_response_wrapper(
            callforwardingsignal.check_unconditional_forwarding,
        )


class AsyncCallforwardingsignalResourceWithRawResponse:
    def __init__(self, callforwardingsignal: AsyncCallforwardingsignalResource) -> None:
        self._callforwardingsignal = callforwardingsignal

        self.check_active_forwardings = async_to_raw_response_wrapper(
            callforwardingsignal.check_active_forwardings,
        )
        self.check_unconditional_forwarding = async_to_raw_response_wrapper(
            callforwardingsignal.check_unconditional_forwarding,
        )


class CallforwardingsignalResourceWithStreamingResponse:
    def __init__(self, callforwardingsignal: CallforwardingsignalResource) -> None:
        self._callforwardingsignal = callforwardingsignal

        self.check_active_forwardings = to_streamed_response_wrapper(
            callforwardingsignal.check_active_forwardings,
        )
        self.check_unconditional_forwarding = to_streamed_response_wrapper(
            callforwardingsignal.check_unconditional_forwarding,
        )


class AsyncCallforwardingsignalResourceWithStreamingResponse:
    def __init__(self, callforwardingsignal: AsyncCallforwardingsignalResource) -> None:
        self._callforwardingsignal = callforwardingsignal

        self.check_active_forwardings = async_to_streamed_response_wrapper(
            callforwardingsignal.check_active_forwardings,
        )
        self.check_unconditional_forwarding = async_to_streamed_response_wrapper(
            callforwardingsignal.check_unconditional_forwarding,
        )
