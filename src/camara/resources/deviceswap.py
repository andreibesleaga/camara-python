# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import deviceswap_check_params, deviceswap_retrieve_date_params
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
from ..types.deviceswap_check_response import DeviceswapCheckResponse
from ..types.deviceswap_retrieve_date_response import DeviceswapRetrieveDateResponse

__all__ = ["DeviceswapResource", "AsyncDeviceswapResource"]


class DeviceswapResource(SyncAPIResource):
    """Device Swap"""

    @cached_property
    def with_raw_response(self) -> DeviceswapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return DeviceswapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeviceswapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return DeviceswapResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        max_age: int | Omit = omit,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceswapCheckResponse:
        """
        Check if device swap has been performed during a past period

        Args:
          max_age: Period in hours to be checked for device swap.

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
            "/deviceswap/check",
            body=maybe_transform(
                {
                    "max_age": max_age,
                    "phone_number": phone_number,
                },
                deviceswap_check_params.DeviceswapCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceswapCheckResponse,
        )

    def retrieve_date(
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
    ) -> DeviceswapRetrieveDateResponse:
        """
        Get timestamp of last device swap for a mobile user account provided with phone
        number.

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
            "/deviceswap/retrieve-date",
            body=maybe_transform(
                {"phone_number": phone_number}, deviceswap_retrieve_date_params.DeviceswapRetrieveDateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceswapRetrieveDateResponse,
        )


class AsyncDeviceswapResource(AsyncAPIResource):
    """Device Swap"""

    @cached_property
    def with_raw_response(self) -> AsyncDeviceswapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeviceswapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeviceswapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncDeviceswapResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        max_age: int | Omit = omit,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceswapCheckResponse:
        """
        Check if device swap has been performed during a past period

        Args:
          max_age: Period in hours to be checked for device swap.

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
            "/deviceswap/check",
            body=await async_maybe_transform(
                {
                    "max_age": max_age,
                    "phone_number": phone_number,
                },
                deviceswap_check_params.DeviceswapCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceswapCheckResponse,
        )

    async def retrieve_date(
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
    ) -> DeviceswapRetrieveDateResponse:
        """
        Get timestamp of last device swap for a mobile user account provided with phone
        number.

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
            "/deviceswap/retrieve-date",
            body=await async_maybe_transform(
                {"phone_number": phone_number}, deviceswap_retrieve_date_params.DeviceswapRetrieveDateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceswapRetrieveDateResponse,
        )


class DeviceswapResourceWithRawResponse:
    def __init__(self, deviceswap: DeviceswapResource) -> None:
        self._deviceswap = deviceswap

        self.check = to_raw_response_wrapper(
            deviceswap.check,
        )
        self.retrieve_date = to_raw_response_wrapper(
            deviceswap.retrieve_date,
        )


class AsyncDeviceswapResourceWithRawResponse:
    def __init__(self, deviceswap: AsyncDeviceswapResource) -> None:
        self._deviceswap = deviceswap

        self.check = async_to_raw_response_wrapper(
            deviceswap.check,
        )
        self.retrieve_date = async_to_raw_response_wrapper(
            deviceswap.retrieve_date,
        )


class DeviceswapResourceWithStreamingResponse:
    def __init__(self, deviceswap: DeviceswapResource) -> None:
        self._deviceswap = deviceswap

        self.check = to_streamed_response_wrapper(
            deviceswap.check,
        )
        self.retrieve_date = to_streamed_response_wrapper(
            deviceswap.retrieve_date,
        )


class AsyncDeviceswapResourceWithStreamingResponse:
    def __init__(self, deviceswap: AsyncDeviceswapResource) -> None:
        self._deviceswap = deviceswap

        self.check = async_to_streamed_response_wrapper(
            deviceswap.check,
        )
        self.retrieve_date = async_to_streamed_response_wrapper(
            deviceswap.retrieve_date,
        )
