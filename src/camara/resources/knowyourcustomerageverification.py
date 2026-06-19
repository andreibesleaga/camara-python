# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import knowyourcustomerageverification_verify_params
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
from ..types.knowyourcustomerageverification_verify_response import KnowyourcustomerageverificationVerifyResponse

__all__ = ["KnowyourcustomerageverificationResource", "AsyncKnowyourcustomerageverificationResource"]


class KnowyourcustomerageverificationResource(SyncAPIResource):
    """Know Your Customer Age Verification"""

    @cached_property
    def with_raw_response(self) -> KnowyourcustomerageverificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return KnowyourcustomerageverificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowyourcustomerageverificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return KnowyourcustomerageverificationResourceWithStreamingResponse(self)

    def verify(
        self,
        *,
        age_threshold: int,
        birthdate: Union[str, date] | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        family_name_at_birth: str | Omit = omit,
        given_name: str | Omit = omit,
        id_document: str | Omit = omit,
        include_content_lock: bool | Omit = omit,
        include_parental_control: bool | Omit = omit,
        middle_names: str | Omit = omit,
        name: str | Omit = omit,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomerageverificationVerifyResponse:
        """
        Verify that the age of the subscriber associated with a phone number is equal to
        or greater than the specified age threshold value.

        As it is possible that the person holding the contract and the end-user of the
        subscription may not be the same, the endpoint also admits a list of optional
        properties to be included in the request to improve the identification. The
        response may optionally include the `identityMatchScore` property with a value
        that indicates how certain it is that the information returned relates to the
        person that the API Client is requesting. To increase the reliability of the
        information returned, the API Provider may include in the response the
        `verifiedStatus` property, indicating whether the identity information in its
        possession has been verified against an identification document legally accepted
        as an age verification document (Note). Note: Depending on the country,
        credit-check or other mechanism can be used instead of official identification
        for Age Verification. For details, please contact API Provider.

        If the API Client indicates request properties `includeContentLock` or
        `includeParentalControl` with value `true` and the API Provider implements this
        functionality, then the response will also include `contentLock` and
        `parentalControl` properties to indicate if the subscription has any kind of
        content filtering enabled. On the other hand, if the request properties are not
        included or the API Client specifies value `false`, then the response properties
        will not be returned. If the API Provider doesn't implement this functionality,
        request properties will be ignored and response properties won't be returned in
        any case.

        Args:
          age_threshold: The age to be verified. The indicated range is a global definition of maximum
              and minimum values allowed to be requested. It is important to note that this
              range might be more restrictive in some implementations due to local regulations
              of a country i.e. A country does not allow to request for an age under 18. This
              limitation must be informed during the onboarding process.

          birthdate: The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
              (YYYY-MM-DD).

          email: Email address of the customer in the RFC specified format (local-part@domain).

          family_name: Last name, family name, or surname of the customer.

          family_name_at_birth: Last/family/sur- name at birth of the customer.

          given_name: First/given name or compound first/given name of the customer.

          id_document: Id number associated to the official identity document in the country. It may
              contain alphanumeric characters.

          include_content_lock: If this parameter is included in the request with value `true`, the response
              property `contentLock` will be returned. If it is not included or its value is
              `false`, the response property will not be returned.

          include_parental_control: If this parameter is included in the request with value `true`, the response
              property `parentalControl` will be returned. If it is not included or its value
              is `false`, the response property will not be returned.

          middle_names: Middle name/s of the customer.

          name: Complete name of the customer, usually composed of first/given name and
              last/family/sur- name in a country. Depending on the country, the order of
              first/give name and last/family/sur- name varies, and middle name could be
              included. It can use givenName, middleNames, familyName and/or
              familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
              name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.

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
            "/knowyourcustomerageverification/verify",
            body=maybe_transform(
                {
                    "age_threshold": age_threshold,
                    "birthdate": birthdate,
                    "email": email,
                    "family_name": family_name,
                    "family_name_at_birth": family_name_at_birth,
                    "given_name": given_name,
                    "id_document": id_document,
                    "include_content_lock": include_content_lock,
                    "include_parental_control": include_parental_control,
                    "middle_names": middle_names,
                    "name": name,
                    "phone_number": phone_number,
                },
                knowyourcustomerageverification_verify_params.KnowyourcustomerageverificationVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomerageverificationVerifyResponse,
        )


class AsyncKnowyourcustomerageverificationResource(AsyncAPIResource):
    """Know Your Customer Age Verification"""

    @cached_property
    def with_raw_response(self) -> AsyncKnowyourcustomerageverificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowyourcustomerageverificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowyourcustomerageverificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncKnowyourcustomerageverificationResourceWithStreamingResponse(self)

    async def verify(
        self,
        *,
        age_threshold: int,
        birthdate: Union[str, date] | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        family_name_at_birth: str | Omit = omit,
        given_name: str | Omit = omit,
        id_document: str | Omit = omit,
        include_content_lock: bool | Omit = omit,
        include_parental_control: bool | Omit = omit,
        middle_names: str | Omit = omit,
        name: str | Omit = omit,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomerageverificationVerifyResponse:
        """
        Verify that the age of the subscriber associated with a phone number is equal to
        or greater than the specified age threshold value.

        As it is possible that the person holding the contract and the end-user of the
        subscription may not be the same, the endpoint also admits a list of optional
        properties to be included in the request to improve the identification. The
        response may optionally include the `identityMatchScore` property with a value
        that indicates how certain it is that the information returned relates to the
        person that the API Client is requesting. To increase the reliability of the
        information returned, the API Provider may include in the response the
        `verifiedStatus` property, indicating whether the identity information in its
        possession has been verified against an identification document legally accepted
        as an age verification document (Note). Note: Depending on the country,
        credit-check or other mechanism can be used instead of official identification
        for Age Verification. For details, please contact API Provider.

        If the API Client indicates request properties `includeContentLock` or
        `includeParentalControl` with value `true` and the API Provider implements this
        functionality, then the response will also include `contentLock` and
        `parentalControl` properties to indicate if the subscription has any kind of
        content filtering enabled. On the other hand, if the request properties are not
        included or the API Client specifies value `false`, then the response properties
        will not be returned. If the API Provider doesn't implement this functionality,
        request properties will be ignored and response properties won't be returned in
        any case.

        Args:
          age_threshold: The age to be verified. The indicated range is a global definition of maximum
              and minimum values allowed to be requested. It is important to note that this
              range might be more restrictive in some implementations due to local regulations
              of a country i.e. A country does not allow to request for an age under 18. This
              limitation must be informed during the onboarding process.

          birthdate: The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
              (YYYY-MM-DD).

          email: Email address of the customer in the RFC specified format (local-part@domain).

          family_name: Last name, family name, or surname of the customer.

          family_name_at_birth: Last/family/sur- name at birth of the customer.

          given_name: First/given name or compound first/given name of the customer.

          id_document: Id number associated to the official identity document in the country. It may
              contain alphanumeric characters.

          include_content_lock: If this parameter is included in the request with value `true`, the response
              property `contentLock` will be returned. If it is not included or its value is
              `false`, the response property will not be returned.

          include_parental_control: If this parameter is included in the request with value `true`, the response
              property `parentalControl` will be returned. If it is not included or its value
              is `false`, the response property will not be returned.

          middle_names: Middle name/s of the customer.

          name: Complete name of the customer, usually composed of first/given name and
              last/family/sur- name in a country. Depending on the country, the order of
              first/give name and last/family/sur- name varies, and middle name could be
              included. It can use givenName, middleNames, familyName and/or
              familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
              name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.

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
            "/knowyourcustomerageverification/verify",
            body=await async_maybe_transform(
                {
                    "age_threshold": age_threshold,
                    "birthdate": birthdate,
                    "email": email,
                    "family_name": family_name,
                    "family_name_at_birth": family_name_at_birth,
                    "given_name": given_name,
                    "id_document": id_document,
                    "include_content_lock": include_content_lock,
                    "include_parental_control": include_parental_control,
                    "middle_names": middle_names,
                    "name": name,
                    "phone_number": phone_number,
                },
                knowyourcustomerageverification_verify_params.KnowyourcustomerageverificationVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomerageverificationVerifyResponse,
        )


class KnowyourcustomerageverificationResourceWithRawResponse:
    def __init__(self, knowyourcustomerageverification: KnowyourcustomerageverificationResource) -> None:
        self._knowyourcustomerageverification = knowyourcustomerageverification

        self.verify = to_raw_response_wrapper(
            knowyourcustomerageverification.verify,
        )


class AsyncKnowyourcustomerageverificationResourceWithRawResponse:
    def __init__(self, knowyourcustomerageverification: AsyncKnowyourcustomerageverificationResource) -> None:
        self._knowyourcustomerageverification = knowyourcustomerageverification

        self.verify = async_to_raw_response_wrapper(
            knowyourcustomerageverification.verify,
        )


class KnowyourcustomerageverificationResourceWithStreamingResponse:
    def __init__(self, knowyourcustomerageverification: KnowyourcustomerageverificationResource) -> None:
        self._knowyourcustomerageverification = knowyourcustomerageverification

        self.verify = to_streamed_response_wrapper(
            knowyourcustomerageverification.verify,
        )


class AsyncKnowyourcustomerageverificationResourceWithStreamingResponse:
    def __init__(self, knowyourcustomerageverification: AsyncKnowyourcustomerageverificationResource) -> None:
        self._knowyourcustomerageverification = knowyourcustomerageverification

        self.verify = async_to_streamed_response_wrapper(
            knowyourcustomerageverification.verify,
        )
