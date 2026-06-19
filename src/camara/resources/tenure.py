# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import tenure_verify_params
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
from ..types.tenure_verify_response import TenureVerifyResponse

__all__ = ["TenureResource", "AsyncTenureResource"]


class TenureResource(SyncAPIResource):
    """KYC Tenure"""

    @cached_property
    def with_raw_response(self) -> TenureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return TenureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return TenureResourceWithStreamingResponse(self)

    def verify(
        self,
        *,
        tenure_date: Union[str, date],
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenureVerifyResponse:
        """
        Verifies a specified length of tenure, based on a provided date, for a network
        subscriber to establish a level of trust for the network subscription
        identifier.

        Args:
          tenure_date: The date, in RFC 3339 / ISO 8601 compliant format "YYYY-MM-DD", from which
              continuous tenure of the identified network subscriber is required to be
              confirmed

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
            "/tenure/check-tenure",
            body=maybe_transform(
                {
                    "tenure_date": tenure_date,
                    "phone_number": phone_number,
                },
                tenure_verify_params.TenureVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenureVerifyResponse,
        )


class AsyncTenureResource(AsyncAPIResource):
    """KYC Tenure"""

    @cached_property
    def with_raw_response(self) -> AsyncTenureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncTenureResourceWithStreamingResponse(self)

    async def verify(
        self,
        *,
        tenure_date: Union[str, date],
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenureVerifyResponse:
        """
        Verifies a specified length of tenure, based on a provided date, for a network
        subscriber to establish a level of trust for the network subscription
        identifier.

        Args:
          tenure_date: The date, in RFC 3339 / ISO 8601 compliant format "YYYY-MM-DD", from which
              continuous tenure of the identified network subscriber is required to be
              confirmed

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
            "/tenure/check-tenure",
            body=await async_maybe_transform(
                {
                    "tenure_date": tenure_date,
                    "phone_number": phone_number,
                },
                tenure_verify_params.TenureVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenureVerifyResponse,
        )


class TenureResourceWithRawResponse:
    def __init__(self, tenure: TenureResource) -> None:
        self._tenure = tenure

        self.verify = to_raw_response_wrapper(
            tenure.verify,
        )


class AsyncTenureResourceWithRawResponse:
    def __init__(self, tenure: AsyncTenureResource) -> None:
        self._tenure = tenure

        self.verify = async_to_raw_response_wrapper(
            tenure.verify,
        )


class TenureResourceWithStreamingResponse:
    def __init__(self, tenure: TenureResource) -> None:
        self._tenure = tenure

        self.verify = to_streamed_response_wrapper(
            tenure.verify,
        )


class AsyncTenureResourceWithStreamingResponse:
    def __init__(self, tenure: AsyncTenureResource) -> None:
        self._tenure = tenure

        self.verify = async_to_streamed_response_wrapper(
            tenure.verify,
        )
