# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import otpvalidation_send_code_params, otpvalidation_validate_code_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.otpvalidation_send_code_response import OtpvalidationSendCodeResponse

__all__ = ["OtpvalidationResource", "AsyncOtpvalidationResource"]


class OtpvalidationResource(SyncAPIResource):
    """One Time Password SMS"""

    @cached_property
    def with_raw_response(self) -> OtpvalidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return OtpvalidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OtpvalidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return OtpvalidationResourceWithStreamingResponse(self)

    def send_code(
        self,
        *,
        message: str,
        phone_number: str,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtpvalidationSendCodeResponse:
        """
        Sends an SMS with the desired message and an OTP code to the received phone
        number.

        Args:
          message: Message template used to compose the content of the SMS sent to the phone
              number. It must include the following label indicating where to include the
              short code `{{code}}`

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
            "/otpvalidation/send-code",
            body=maybe_transform(
                {
                    "message": message,
                    "phone_number": phone_number,
                },
                otpvalidation_send_code_params.OtpvalidationSendCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtpvalidationSendCodeResponse,
        )

    def validate_code(
        self,
        *,
        authentication_id: str,
        code: str,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Verifies the code is valid for the received authenticationId

        Args:
          authentication_id: unique id of the verification attempt the code belongs to.

          code: temporal, short code to be validated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/otpvalidation/validate-code",
            body=maybe_transform(
                {
                    "authentication_id": authentication_id,
                    "code": code,
                },
                otpvalidation_validate_code_params.OtpvalidationValidateCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOtpvalidationResource(AsyncAPIResource):
    """One Time Password SMS"""

    @cached_property
    def with_raw_response(self) -> AsyncOtpvalidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOtpvalidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOtpvalidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncOtpvalidationResourceWithStreamingResponse(self)

    async def send_code(
        self,
        *,
        message: str,
        phone_number: str,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtpvalidationSendCodeResponse:
        """
        Sends an SMS with the desired message and an OTP code to the received phone
        number.

        Args:
          message: Message template used to compose the content of the SMS sent to the phone
              number. It must include the following label indicating where to include the
              short code `{{code}}`

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
            "/otpvalidation/send-code",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "phone_number": phone_number,
                },
                otpvalidation_send_code_params.OtpvalidationSendCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtpvalidationSendCodeResponse,
        )

    async def validate_code(
        self,
        *,
        authentication_id: str,
        code: str,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Verifies the code is valid for the received authenticationId

        Args:
          authentication_id: unique id of the verification attempt the code belongs to.

          code: temporal, short code to be validated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/otpvalidation/validate-code",
            body=await async_maybe_transform(
                {
                    "authentication_id": authentication_id,
                    "code": code,
                },
                otpvalidation_validate_code_params.OtpvalidationValidateCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OtpvalidationResourceWithRawResponse:
    def __init__(self, otpvalidation: OtpvalidationResource) -> None:
        self._otpvalidation = otpvalidation

        self.send_code = to_raw_response_wrapper(
            otpvalidation.send_code,
        )
        self.validate_code = to_raw_response_wrapper(
            otpvalidation.validate_code,
        )


class AsyncOtpvalidationResourceWithRawResponse:
    def __init__(self, otpvalidation: AsyncOtpvalidationResource) -> None:
        self._otpvalidation = otpvalidation

        self.send_code = async_to_raw_response_wrapper(
            otpvalidation.send_code,
        )
        self.validate_code = async_to_raw_response_wrapper(
            otpvalidation.validate_code,
        )


class OtpvalidationResourceWithStreamingResponse:
    def __init__(self, otpvalidation: OtpvalidationResource) -> None:
        self._otpvalidation = otpvalidation

        self.send_code = to_streamed_response_wrapper(
            otpvalidation.send_code,
        )
        self.validate_code = to_streamed_response_wrapper(
            otpvalidation.validate_code,
        )


class AsyncOtpvalidationResourceWithStreamingResponse:
    def __init__(self, otpvalidation: AsyncOtpvalidationResource) -> None:
        self._otpvalidation = otpvalidation

        self.send_code = async_to_streamed_response_wrapper(
            otpvalidation.send_code,
        )
        self.validate_code = async_to_streamed_response_wrapper(
            otpvalidation.validate_code,
        )
