# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import knowyourcustomermatch_match_params
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
from ..types.knowyourcustomermatch_match_response import KnowyourcustomermatchMatchResponse

__all__ = ["KnowyourcustomermatchResource", "AsyncKnowyourcustomermatchResource"]


class KnowyourcustomermatchResource(SyncAPIResource):
    """Know Your Customer Match"""

    @cached_property
    def with_raw_response(self) -> KnowyourcustomermatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return KnowyourcustomermatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowyourcustomermatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return KnowyourcustomermatchResourceWithStreamingResponse(self)

    def match(
        self,
        *,
        address: str | Omit = omit,
        birthdate: Union[str, date] | Omit = omit,
        city_of_birth: str | Omit = omit,
        country: str | Omit = omit,
        country_of_birth: str | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        family_name_at_birth: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "OTHER"] | Omit = omit,
        given_name: str | Omit = omit,
        house_number_extension: str | Omit = omit,
        id_document: str | Omit = omit,
        id_document_expiry_date: Union[str, date] | Omit = omit,
        id_document_type: Literal[
            "passport",
            "national_id_card",
            "residence_permit",
            "diplomatic_id",
            "driver_licence",
            "social_security_id",
            "other",
        ]
        | Omit = omit,
        locality: str | Omit = omit,
        middle_names: str | Omit = omit,
        name: str | Omit = omit,
        name_kana_hankaku: str | Omit = omit,
        name_kana_zenkaku: str | Omit = omit,
        nationality: str | Omit = omit,
        phone_number: str | Omit = omit,
        postal_code: str | Omit = omit,
        region: str | Omit = omit,
        street_name: str | Omit = omit,
        street_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomermatchMatchResponse:
        """
        Verify matching of a number of attributes related to a customer identity against
        the verified data bound to their phone number in the Operator systems.
        Regardless of whether the `phoneNumber` is explicitly stated in the request
        body, at least one of the other fields must be provided, otherwise a
        `HTTP 400 - KNOW_YOUR_CUSTOMER.INVALID_PARAM_COMBINATION` error will be
        returned.

        The API will return the result of the matching process for each requested
        attribute. This means that the response will **only** contain the attributes for
        which validation has been requested. Possible values are:

        - **true**: the attribute provided matches with the one in the Operator systems,
          which is equal to a `match_score` of 100.
        - **false**: the attribute provided does not match with the one in the Operator
          systems.
        - **not_available**: the attribute is not available to validate.

        Args:
          address: Complete address of the customer. For some countries, it is built following the
              usual concatenation of parameters in a country, but for other countries, this is
              not the case. For some countries, it can use streetName, streetNumber and/or
              houseNumberExtension. For example, in ESP, streetName+streetNumber; in NLD, it
              can be streetName+streetNumber or streetName+streetNumber+houseNumberExtension.

          birthdate: The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
              (YYYY-MM-DD).

          city_of_birth: City where the customer was born.

          country: Country of the customer's address. Format ISO 3166-1 alpha-2

          country_of_birth: Country where the customer was born. Format ISO 3166-1 alpha-2.

          email: Email address of the customer in the RFC specified format (local-part@domain).

          family_name: Last name, family name, or surname of the customer.

          family_name_at_birth: Last/family/sur- name at birth of the customer.

          gender: Gender of the customer (Male/Female/Other).

          given_name: First/given name or compound first/given name of the customer.

          house_number_extension: Specific identifier of the house needed depending on the property type. For
              example, number of apartment in an apartment building.

          id_document: Id number associated to the official identity document in the country. It may
              contain alphanumeric characters.

          id_document_expiry_date: Expiration date of the identity document (ISO 8601).

          id_document_type: Type of the official identity document provided.

          locality: Locality of the customer's address

          middle_names: Middle name/s of the customer.

          name: Complete name of the customer, usually composed of first/given name and
              last/family/sur- name in a country. Depending on the country, the order of
              first/give name and last/family/sur- name varies, and middle name could be
              included. It can use givenName, middleNames, familyName and/or
              familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
              name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.

          name_kana_hankaku: Complete name of the customer in Hankaku-Kana format (reading of name) for
              Japan.

          name_kana_zenkaku: Complete name of the customer in Zenkaku-Kana format (reading of name) for
              Japan.

          nationality: ISO 3166-1 alpha-2 code of the customer’s nationality. In the case a customer
              has more than one nationality, it is supposed to be the nationality related to
              the ID document provided in the match request.

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          postal_code: Zip code or postal code

          region: Region/prefecture of the customer's address

          street_name: Name of the street of the customer's address. It should not include the type of
              the street.

          street_number: The street number of the customer's address. Number identifying a specific
              property on the 'streetName'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/knowyourcustomermatch/match",
            body=maybe_transform(
                {
                    "address": address,
                    "birthdate": birthdate,
                    "city_of_birth": city_of_birth,
                    "country": country,
                    "country_of_birth": country_of_birth,
                    "email": email,
                    "family_name": family_name,
                    "family_name_at_birth": family_name_at_birth,
                    "gender": gender,
                    "given_name": given_name,
                    "house_number_extension": house_number_extension,
                    "id_document": id_document,
                    "id_document_expiry_date": id_document_expiry_date,
                    "id_document_type": id_document_type,
                    "locality": locality,
                    "middle_names": middle_names,
                    "name": name,
                    "name_kana_hankaku": name_kana_hankaku,
                    "name_kana_zenkaku": name_kana_zenkaku,
                    "nationality": nationality,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "region": region,
                    "street_name": street_name,
                    "street_number": street_number,
                },
                knowyourcustomermatch_match_params.KnowyourcustomermatchMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomermatchMatchResponse,
        )


class AsyncKnowyourcustomermatchResource(AsyncAPIResource):
    """Know Your Customer Match"""

    @cached_property
    def with_raw_response(self) -> AsyncKnowyourcustomermatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowyourcustomermatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowyourcustomermatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncKnowyourcustomermatchResourceWithStreamingResponse(self)

    async def match(
        self,
        *,
        address: str | Omit = omit,
        birthdate: Union[str, date] | Omit = omit,
        city_of_birth: str | Omit = omit,
        country: str | Omit = omit,
        country_of_birth: str | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        family_name_at_birth: str | Omit = omit,
        gender: Literal["MALE", "FEMALE", "OTHER"] | Omit = omit,
        given_name: str | Omit = omit,
        house_number_extension: str | Omit = omit,
        id_document: str | Omit = omit,
        id_document_expiry_date: Union[str, date] | Omit = omit,
        id_document_type: Literal[
            "passport",
            "national_id_card",
            "residence_permit",
            "diplomatic_id",
            "driver_licence",
            "social_security_id",
            "other",
        ]
        | Omit = omit,
        locality: str | Omit = omit,
        middle_names: str | Omit = omit,
        name: str | Omit = omit,
        name_kana_hankaku: str | Omit = omit,
        name_kana_zenkaku: str | Omit = omit,
        nationality: str | Omit = omit,
        phone_number: str | Omit = omit,
        postal_code: str | Omit = omit,
        region: str | Omit = omit,
        street_name: str | Omit = omit,
        street_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomermatchMatchResponse:
        """
        Verify matching of a number of attributes related to a customer identity against
        the verified data bound to their phone number in the Operator systems.
        Regardless of whether the `phoneNumber` is explicitly stated in the request
        body, at least one of the other fields must be provided, otherwise a
        `HTTP 400 - KNOW_YOUR_CUSTOMER.INVALID_PARAM_COMBINATION` error will be
        returned.

        The API will return the result of the matching process for each requested
        attribute. This means that the response will **only** contain the attributes for
        which validation has been requested. Possible values are:

        - **true**: the attribute provided matches with the one in the Operator systems,
          which is equal to a `match_score` of 100.
        - **false**: the attribute provided does not match with the one in the Operator
          systems.
        - **not_available**: the attribute is not available to validate.

        Args:
          address: Complete address of the customer. For some countries, it is built following the
              usual concatenation of parameters in a country, but for other countries, this is
              not the case. For some countries, it can use streetName, streetNumber and/or
              houseNumberExtension. For example, in ESP, streetName+streetNumber; in NLD, it
              can be streetName+streetNumber or streetName+streetNumber+houseNumberExtension.

          birthdate: The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
              (YYYY-MM-DD).

          city_of_birth: City where the customer was born.

          country: Country of the customer's address. Format ISO 3166-1 alpha-2

          country_of_birth: Country where the customer was born. Format ISO 3166-1 alpha-2.

          email: Email address of the customer in the RFC specified format (local-part@domain).

          family_name: Last name, family name, or surname of the customer.

          family_name_at_birth: Last/family/sur- name at birth of the customer.

          gender: Gender of the customer (Male/Female/Other).

          given_name: First/given name or compound first/given name of the customer.

          house_number_extension: Specific identifier of the house needed depending on the property type. For
              example, number of apartment in an apartment building.

          id_document: Id number associated to the official identity document in the country. It may
              contain alphanumeric characters.

          id_document_expiry_date: Expiration date of the identity document (ISO 8601).

          id_document_type: Type of the official identity document provided.

          locality: Locality of the customer's address

          middle_names: Middle name/s of the customer.

          name: Complete name of the customer, usually composed of first/given name and
              last/family/sur- name in a country. Depending on the country, the order of
              first/give name and last/family/sur- name varies, and middle name could be
              included. It can use givenName, middleNames, familyName and/or
              familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
              name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.

          name_kana_hankaku: Complete name of the customer in Hankaku-Kana format (reading of name) for
              Japan.

          name_kana_zenkaku: Complete name of the customer in Zenkaku-Kana format (reading of name) for
              Japan.

          nationality: ISO 3166-1 alpha-2 code of the customer’s nationality. In the case a customer
              has more than one nationality, it is supposed to be the nationality related to
              the ID document provided in the match request.

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          postal_code: Zip code or postal code

          region: Region/prefecture of the customer's address

          street_name: Name of the street of the customer's address. It should not include the type of
              the street.

          street_number: The street number of the customer's address. Number identifying a specific
              property on the 'streetName'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/knowyourcustomermatch/match",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "birthdate": birthdate,
                    "city_of_birth": city_of_birth,
                    "country": country,
                    "country_of_birth": country_of_birth,
                    "email": email,
                    "family_name": family_name,
                    "family_name_at_birth": family_name_at_birth,
                    "gender": gender,
                    "given_name": given_name,
                    "house_number_extension": house_number_extension,
                    "id_document": id_document,
                    "id_document_expiry_date": id_document_expiry_date,
                    "id_document_type": id_document_type,
                    "locality": locality,
                    "middle_names": middle_names,
                    "name": name,
                    "name_kana_hankaku": name_kana_hankaku,
                    "name_kana_zenkaku": name_kana_zenkaku,
                    "nationality": nationality,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "region": region,
                    "street_name": street_name,
                    "street_number": street_number,
                },
                knowyourcustomermatch_match_params.KnowyourcustomermatchMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomermatchMatchResponse,
        )


class KnowyourcustomermatchResourceWithRawResponse:
    def __init__(self, knowyourcustomermatch: KnowyourcustomermatchResource) -> None:
        self._knowyourcustomermatch = knowyourcustomermatch

        self.match = to_raw_response_wrapper(
            knowyourcustomermatch.match,
        )


class AsyncKnowyourcustomermatchResourceWithRawResponse:
    def __init__(self, knowyourcustomermatch: AsyncKnowyourcustomermatchResource) -> None:
        self._knowyourcustomermatch = knowyourcustomermatch

        self.match = async_to_raw_response_wrapper(
            knowyourcustomermatch.match,
        )


class KnowyourcustomermatchResourceWithStreamingResponse:
    def __init__(self, knowyourcustomermatch: KnowyourcustomermatchResource) -> None:
        self._knowyourcustomermatch = knowyourcustomermatch

        self.match = to_streamed_response_wrapper(
            knowyourcustomermatch.match,
        )


class AsyncKnowyourcustomermatchResourceWithStreamingResponse:
    def __init__(self, knowyourcustomermatch: AsyncKnowyourcustomermatchResource) -> None:
        self._knowyourcustomermatch = knowyourcustomermatch

        self.match = async_to_streamed_response_wrapper(
            knowyourcustomermatch.match,
        )
