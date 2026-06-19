# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import QosProfileStatus, qualityondemand_retrieve_qos_profiles_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.qos_profile import QosProfile
from ..types.qos_profile_status import QosProfileStatus
from ..types.qualityondemand_retrieve_qos_profiles_response import QualityondemandRetrieveQosProfilesResponse

__all__ = ["QualityondemandResource", "AsyncQualityondemandResource"]


class QualityondemandResource(SyncAPIResource):
    """QoS Profiles"""

    @cached_property
    def with_raw_response(self) -> QualityondemandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return QualityondemandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityondemandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return QualityondemandResourceWithStreamingResponse(self)

    def retrieve_qos_profile(
        self,
        name: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QosProfile:
        """
        Returns a QoS Profile that matches the given name.

        The access token may be either a 2-legged or 3-legged access token. If the
        access token is 3-legged, a QoS Profile is only returned if available to all
        subjects associated with the access token.

        Args:
          name: A unique name for identifying a specific QoS profile. This may follow different
              formats depending on the service providers implementation. Some options
              addresses:

              - A UUID style string
              - Support for predefined profile names like `QOS_E`, `QOS_S`, `QOS_M`, and
                `QOS_L`
              - A searchable descriptive name

          x_correlator: Value for the x-correlator

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._get(
            path_template("/qualityondemand/qos-profiles/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QosProfile,
        )

    def retrieve_qos_profiles(
        self,
        *,
        device: qualityondemand_retrieve_qos_profiles_params.Device | Omit = omit,
        name: str | Omit = omit,
        status: QosProfileStatus | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityondemandRetrieveQosProfilesResponse:
        """Returns all QoS Profiles that match the given criteria.

        **NOTES:**

        - The access token may be either a 2-legged or 3-legged access token.
        - If the access token is 3-legged, all returned QoS Profiles will be available
          to the subject (device) associated with the access token.
        - If the access token is 2-legged and a device filter is provided, all returned
          QoS Profiles will be available to that device. If multiple device identifiers
          are provided within the device property, only QoS Profiles available to the
          device identifier chosen by the implementation will be returned, even if the
          identifiers do not match the same device. API provider does not perform any
          logic to validate/correlate that the indicated device identifiers match the
          same device. No error should be returned if the identifiers are otherwise
          valid to prevent API consumers correlating different identifiers with a given
          end user.
        - This call uses the POST method instead of GET to comply with the CAMARA
          Commonalities guidelines for sending sensitive or complex data in API calls.
          Since the device field may contain personally identifiable information, it
          should not be sent via GET. Additionally, this call may include complex data
          structures.
          [CAMARA API Design Guidelines](https://github.com/camaraproject/Commonalities/blob/r3.3/documentation/API-design-guidelines.md#post-or-get-for-transferring-sensitive-or-complex-data)

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators.

              The developer can choose to provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber` NOTE1: the network operator might support only a subset of these
                options. The API consumer can provide multiple identifiers to be compatible
                across different operators. In this case the identifiers MUST belong to the
                same device. NOTE2: as for this Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          name: A unique name for identifying a specific QoS profile. This may follow different
              formats depending on the service providers implementation. Some options
              addresses:

              - A UUID style string
              - Support for predefined profile names like `QOS_E`, `QOS_S`, `QOS_M`, and
                `QOS_L`
              - A searchable descriptive name

          status: The current status of the QoS Profile

              - `ACTIVE`- QoS Profile is available to be used
              - `INACTIVE`- QoS Profile is not currently available to be deployed
              - `DEPRECATED`- QoS profile is actively being used in a QoD session, but can not
                be deployed in new QoD sessions

          x_correlator: Value for the x-correlator

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/qualityondemand/retrieve-qos-profiles",
            body=maybe_transform(
                {
                    "device": device,
                    "name": name,
                    "status": status,
                },
                qualityondemand_retrieve_qos_profiles_params.QualityondemandRetrieveQosProfilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityondemandRetrieveQosProfilesResponse,
        )


class AsyncQualityondemandResource(AsyncAPIResource):
    """QoS Profiles"""

    @cached_property
    def with_raw_response(self) -> AsyncQualityondemandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQualityondemandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityondemandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncQualityondemandResourceWithStreamingResponse(self)

    async def retrieve_qos_profile(
        self,
        name: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QosProfile:
        """
        Returns a QoS Profile that matches the given name.

        The access token may be either a 2-legged or 3-legged access token. If the
        access token is 3-legged, a QoS Profile is only returned if available to all
        subjects associated with the access token.

        Args:
          name: A unique name for identifying a specific QoS profile. This may follow different
              formats depending on the service providers implementation. Some options
              addresses:

              - A UUID style string
              - Support for predefined profile names like `QOS_E`, `QOS_S`, `QOS_M`, and
                `QOS_L`
              - A searchable descriptive name

          x_correlator: Value for the x-correlator

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._get(
            path_template("/qualityondemand/qos-profiles/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QosProfile,
        )

    async def retrieve_qos_profiles(
        self,
        *,
        device: qualityondemand_retrieve_qos_profiles_params.Device | Omit = omit,
        name: str | Omit = omit,
        status: QosProfileStatus | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityondemandRetrieveQosProfilesResponse:
        """Returns all QoS Profiles that match the given criteria.

        **NOTES:**

        - The access token may be either a 2-legged or 3-legged access token.
        - If the access token is 3-legged, all returned QoS Profiles will be available
          to the subject (device) associated with the access token.
        - If the access token is 2-legged and a device filter is provided, all returned
          QoS Profiles will be available to that device. If multiple device identifiers
          are provided within the device property, only QoS Profiles available to the
          device identifier chosen by the implementation will be returned, even if the
          identifiers do not match the same device. API provider does not perform any
          logic to validate/correlate that the indicated device identifiers match the
          same device. No error should be returned if the identifiers are otherwise
          valid to prevent API consumers correlating different identifiers with a given
          end user.
        - This call uses the POST method instead of GET to comply with the CAMARA
          Commonalities guidelines for sending sensitive or complex data in API calls.
          Since the device field may contain personally identifiable information, it
          should not be sent via GET. Additionally, this call may include complex data
          structures.
          [CAMARA API Design Guidelines](https://github.com/camaraproject/Commonalities/blob/r3.3/documentation/API-design-guidelines.md#post-or-get-for-transferring-sensitive-or-complex-data)

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators.

              The developer can choose to provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber` NOTE1: the network operator might support only a subset of these
                options. The API consumer can provide multiple identifiers to be compatible
                across different operators. In this case the identifiers MUST belong to the
                same device. NOTE2: as for this Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          name: A unique name for identifying a specific QoS profile. This may follow different
              formats depending on the service providers implementation. Some options
              addresses:

              - A UUID style string
              - Support for predefined profile names like `QOS_E`, `QOS_S`, `QOS_M`, and
                `QOS_L`
              - A searchable descriptive name

          status: The current status of the QoS Profile

              - `ACTIVE`- QoS Profile is available to be used
              - `INACTIVE`- QoS Profile is not currently available to be deployed
              - `DEPRECATED`- QoS profile is actively being used in a QoD session, but can not
                be deployed in new QoD sessions

          x_correlator: Value for the x-correlator

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/qualityondemand/retrieve-qos-profiles",
            body=await async_maybe_transform(
                {
                    "device": device,
                    "name": name,
                    "status": status,
                },
                qualityondemand_retrieve_qos_profiles_params.QualityondemandRetrieveQosProfilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityondemandRetrieveQosProfilesResponse,
        )


class QualityondemandResourceWithRawResponse:
    def __init__(self, qualityondemand: QualityondemandResource) -> None:
        self._qualityondemand = qualityondemand

        self.retrieve_qos_profile = to_raw_response_wrapper(
            qualityondemand.retrieve_qos_profile,
        )
        self.retrieve_qos_profiles = to_raw_response_wrapper(
            qualityondemand.retrieve_qos_profiles,
        )


class AsyncQualityondemandResourceWithRawResponse:
    def __init__(self, qualityondemand: AsyncQualityondemandResource) -> None:
        self._qualityondemand = qualityondemand

        self.retrieve_qos_profile = async_to_raw_response_wrapper(
            qualityondemand.retrieve_qos_profile,
        )
        self.retrieve_qos_profiles = async_to_raw_response_wrapper(
            qualityondemand.retrieve_qos_profiles,
        )


class QualityondemandResourceWithStreamingResponse:
    def __init__(self, qualityondemand: QualityondemandResource) -> None:
        self._qualityondemand = qualityondemand

        self.retrieve_qos_profile = to_streamed_response_wrapper(
            qualityondemand.retrieve_qos_profile,
        )
        self.retrieve_qos_profiles = to_streamed_response_wrapper(
            qualityondemand.retrieve_qos_profiles,
        )


class AsyncQualityondemandResourceWithStreamingResponse:
    def __init__(self, qualityondemand: AsyncQualityondemandResource) -> None:
        self._qualityondemand = qualityondemand

        self.retrieve_qos_profile = async_to_streamed_response_wrapper(
            qualityondemand.retrieve_qos_profile,
        )
        self.retrieve_qos_profiles = async_to_streamed_response_wrapper(
            qualityondemand.retrieve_qos_profiles,
        )
