# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CamaraError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        tenure,
        webrtc,
        simswap,
        deviceswap,
        otpvalidation,
        devicelocation,
        numberrecycling,
        qualityondemand,
        customerinsights,
        deviceidentifier,
        regiondevicecount,
        deviceroamingstatus,
        callforwardingsignal,
        connectednetworktype,
        connectivityinsights,
        knowyourcustomermatch,
        populationdensitydata,
        knowyourcustomerfill_in,
        devicereachabilitystatus,
        knowyourcustomerageverification,
    )
    from .resources.tenure import TenureResource, AsyncTenureResource
    from .resources.deviceswap import DeviceswapResource, AsyncDeviceswapResource
    from .resources.otpvalidation import OtpvalidationResource, AsyncOtpvalidationResource
    from .resources.webrtc.webrtc import WebrtcResource, AsyncWebrtcResource
    from .resources.numberrecycling import NumberrecyclingResource, AsyncNumberrecyclingResource
    from .resources.qualityondemand import QualityondemandResource, AsyncQualityondemandResource
    from .resources.simswap.simswap import SimswapResource, AsyncSimswapResource
    from .resources.deviceidentifier import DeviceidentifierResource, AsyncDeviceidentifierResource
    from .resources.regiondevicecount import RegiondevicecountResource, AsyncRegiondevicecountResource
    from .resources.callforwardingsignal import CallforwardingsignalResource, AsyncCallforwardingsignalResource
    from .resources.knowyourcustomermatch import KnowyourcustomermatchResource, AsyncKnowyourcustomermatchResource
    from .resources.populationdensitydata import PopulationdensitydataResource, AsyncPopulationdensitydataResource
    from .resources.knowyourcustomerfill_in import KnowyourcustomerfillInResource, AsyncKnowyourcustomerfillInResource
    from .resources.devicelocation.devicelocation import DevicelocationResource, AsyncDevicelocationResource
    from .resources.knowyourcustomerageverification import (
        KnowyourcustomerageverificationResource,
        AsyncKnowyourcustomerageverificationResource,
    )
    from .resources.customerinsights.customerinsights import CustomerinsightsResource, AsyncCustomerinsightsResource
    from .resources.deviceroamingstatus.deviceroamingstatus import (
        DeviceroamingstatusResource,
        AsyncDeviceroamingstatusResource,
    )
    from .resources.connectednetworktype.connectednetworktype import (
        ConnectednetworktypeResource,
        AsyncConnectednetworktypeResource,
    )
    from .resources.connectivityinsights.connectivityinsights import (
        ConnectivityinsightsResource,
        AsyncConnectivityinsightsResource,
    )
    from .resources.devicereachabilitystatus.devicereachabilitystatus import (
        DevicereachabilitystatusResource,
        AsyncDevicereachabilitystatusResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Camara", "AsyncCamara", "Client", "AsyncClient"]


class Camara(SyncAPIClient):
    # client options
    bearer_token: str
    customer_insights_token: str
    device_swap_token: str
    kyc_age_verification_token: str
    kyc_fill_in_token: str
    kyc_match_token: str
    tenure_token: str
    number_recycling_token: str
    otp_validation_token: str
    call_forwarding_signal_token: str
    device_location_token: str
    population_density_data_token: str
    region_device_count_token: str
    web_rtc_token: str
    connectivity_insights_token: str
    quality_on_demand_token: str
    device_identifier_token: str
    sim_swap_token: str
    device_roaming_status_token: str
    device_reachability_status_token: str
    connected_network_type_token: str
    device_location_notifications_api_key: str
    notifications_api_key: str
    population_density_data_notifications_api_key: str
    region_device_count_notifications_api_key: str
    connectivity_insights_notifications_api_key: str
    sim_swap_notifications_api_key: str
    device_roaming_status_notifications_api_key: str
    device_reachability_status_notifications_api_key: str
    connected_network_type_notifications_api_key: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        customer_insights_token: str | None = None,
        device_swap_token: str | None = None,
        kyc_age_verification_token: str | None = None,
        kyc_fill_in_token: str | None = None,
        kyc_match_token: str | None = None,
        tenure_token: str | None = None,
        number_recycling_token: str | None = None,
        otp_validation_token: str | None = None,
        call_forwarding_signal_token: str | None = None,
        device_location_token: str | None = None,
        population_density_data_token: str | None = None,
        region_device_count_token: str | None = None,
        web_rtc_token: str | None = None,
        connectivity_insights_token: str | None = None,
        quality_on_demand_token: str | None = None,
        device_identifier_token: str | None = None,
        sim_swap_token: str | None = None,
        device_roaming_status_token: str | None = None,
        device_reachability_status_token: str | None = None,
        connected_network_type_token: str | None = None,
        device_location_notifications_api_key: str | None = None,
        notifications_api_key: str | None = None,
        population_density_data_notifications_api_key: str | None = None,
        region_device_count_notifications_api_key: str | None = None,
        connectivity_insights_notifications_api_key: str | None = None,
        sim_swap_notifications_api_key: str | None = None,
        device_roaming_status_notifications_api_key: str | None = None,
        device_reachability_status_notifications_api_key: str | None = None,
        connected_network_type_notifications_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Camara client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `CAMARA_BEARER_TOKEN`
        - `customer_insights_token` from `CAMARA_BEARER_TOKEN`
        - `device_swap_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_age_verification_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_fill_in_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_match_token` from `CAMARA_BEARER_TOKEN`
        - `tenure_token` from `CAMARA_BEARER_TOKEN`
        - `number_recycling_token` from `CAMARA_BEARER_TOKEN`
        - `otp_validation_token` from `CAMARA_BEARER_TOKEN`
        - `call_forwarding_signal_token` from `CAMARA_BEARER_TOKEN`
        - `device_location_token` from `CAMARA_BEARER_TOKEN`
        - `population_density_data_token` from `CAMARA_BEARER_TOKEN`
        - `region_device_count_token` from `CAMARA_BEARER_TOKEN`
        - `web_rtc_token` from `CAMARA_BEARER_TOKEN`
        - `connectivity_insights_token` from `CAMARA_BEARER_TOKEN`
        - `quality_on_demand_token` from `CAMARA_BEARER_TOKEN`
        - `device_identifier_token` from `CAMARA_BEARER_TOKEN`
        - `sim_swap_token` from `CAMARA_BEARER_TOKEN`
        - `device_roaming_status_token` from `CAMARA_BEARER_TOKEN`
        - `device_reachability_status_token` from `CAMARA_BEARER_TOKEN`
        - `connected_network_type_token` from `CAMARA_BEARER_TOKEN`
        - `device_location_notifications_api_key` from `CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY`
        - `notifications_api_key` from `CAMARA_NOTIFICATIONS_API_KEY`
        - `population_density_data_notifications_api_key` from `CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY`
        - `region_device_count_notifications_api_key` from `CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY`
        - `connectivity_insights_notifications_api_key` from `CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY`
        - `sim_swap_notifications_api_key` from `CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY`
        - `device_roaming_status_notifications_api_key` from `CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY`
        - `device_reachability_status_notifications_api_key` from `CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY`
        - `connected_network_type_notifications_api_key` from `CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if bearer_token is None:
            raise CamaraError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if customer_insights_token is None:
            customer_insights_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if customer_insights_token is None:
            raise CamaraError(
                "The customer_insights_token client option must be set either by passing customer_insights_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.customer_insights_token = customer_insights_token

        if device_swap_token is None:
            device_swap_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_swap_token is None:
            raise CamaraError(
                "The device_swap_token client option must be set either by passing device_swap_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_swap_token = device_swap_token

        if kyc_age_verification_token is None:
            kyc_age_verification_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_age_verification_token is None:
            raise CamaraError(
                "The kyc_age_verification_token client option must be set either by passing kyc_age_verification_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_age_verification_token = kyc_age_verification_token

        if kyc_fill_in_token is None:
            kyc_fill_in_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_fill_in_token is None:
            raise CamaraError(
                "The kyc_fill_in_token client option must be set either by passing kyc_fill_in_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_fill_in_token = kyc_fill_in_token

        if kyc_match_token is None:
            kyc_match_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_match_token is None:
            raise CamaraError(
                "The kyc_match_token client option must be set either by passing kyc_match_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_match_token = kyc_match_token

        if tenure_token is None:
            tenure_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if tenure_token is None:
            raise CamaraError(
                "The tenure_token client option must be set either by passing tenure_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.tenure_token = tenure_token

        if number_recycling_token is None:
            number_recycling_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if number_recycling_token is None:
            raise CamaraError(
                "The number_recycling_token client option must be set either by passing number_recycling_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.number_recycling_token = number_recycling_token

        if otp_validation_token is None:
            otp_validation_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if otp_validation_token is None:
            raise CamaraError(
                "The otp_validation_token client option must be set either by passing otp_validation_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.otp_validation_token = otp_validation_token

        if call_forwarding_signal_token is None:
            call_forwarding_signal_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if call_forwarding_signal_token is None:
            raise CamaraError(
                "The call_forwarding_signal_token client option must be set either by passing call_forwarding_signal_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.call_forwarding_signal_token = call_forwarding_signal_token

        if device_location_token is None:
            device_location_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_location_token is None:
            raise CamaraError(
                "The device_location_token client option must be set either by passing device_location_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_location_token = device_location_token

        if population_density_data_token is None:
            population_density_data_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if population_density_data_token is None:
            raise CamaraError(
                "The population_density_data_token client option must be set either by passing population_density_data_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.population_density_data_token = population_density_data_token

        if region_device_count_token is None:
            region_device_count_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if region_device_count_token is None:
            raise CamaraError(
                "The region_device_count_token client option must be set either by passing region_device_count_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.region_device_count_token = region_device_count_token

        if web_rtc_token is None:
            web_rtc_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if web_rtc_token is None:
            raise CamaraError(
                "The web_rtc_token client option must be set either by passing web_rtc_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.web_rtc_token = web_rtc_token

        if connectivity_insights_token is None:
            connectivity_insights_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if connectivity_insights_token is None:
            raise CamaraError(
                "The connectivity_insights_token client option must be set either by passing connectivity_insights_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.connectivity_insights_token = connectivity_insights_token

        if quality_on_demand_token is None:
            quality_on_demand_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if quality_on_demand_token is None:
            raise CamaraError(
                "The quality_on_demand_token client option must be set either by passing quality_on_demand_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.quality_on_demand_token = quality_on_demand_token

        if device_identifier_token is None:
            device_identifier_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_identifier_token is None:
            raise CamaraError(
                "The device_identifier_token client option must be set either by passing device_identifier_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_identifier_token = device_identifier_token

        if sim_swap_token is None:
            sim_swap_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if sim_swap_token is None:
            raise CamaraError(
                "The sim_swap_token client option must be set either by passing sim_swap_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.sim_swap_token = sim_swap_token

        if device_roaming_status_token is None:
            device_roaming_status_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_roaming_status_token is None:
            raise CamaraError(
                "The device_roaming_status_token client option must be set either by passing device_roaming_status_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_roaming_status_token = device_roaming_status_token

        if device_reachability_status_token is None:
            device_reachability_status_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_reachability_status_token is None:
            raise CamaraError(
                "The device_reachability_status_token client option must be set either by passing device_reachability_status_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_reachability_status_token = device_reachability_status_token

        if connected_network_type_token is None:
            connected_network_type_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if connected_network_type_token is None:
            raise CamaraError(
                "The connected_network_type_token client option must be set either by passing connected_network_type_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.connected_network_type_token = connected_network_type_token

        if device_location_notifications_api_key is None:
            device_location_notifications_api_key = os.environ.get("CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY")
        if device_location_notifications_api_key is None:
            raise CamaraError(
                "The device_location_notifications_api_key client option must be set either by passing device_location_notifications_api_key to the client or by setting the CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_location_notifications_api_key = device_location_notifications_api_key

        if notifications_api_key is None:
            notifications_api_key = os.environ.get("CAMARA_NOTIFICATIONS_API_KEY")
        if notifications_api_key is None:
            raise CamaraError(
                "The notifications_api_key client option must be set either by passing notifications_api_key to the client or by setting the CAMARA_NOTIFICATIONS_API_KEY environment variable"
            )
        self.notifications_api_key = notifications_api_key

        if population_density_data_notifications_api_key is None:
            population_density_data_notifications_api_key = os.environ.get(
                "CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY"
            )
        if population_density_data_notifications_api_key is None:
            raise CamaraError(
                "The population_density_data_notifications_api_key client option must be set either by passing population_density_data_notifications_api_key to the client or by setting the CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY environment variable"
            )
        self.population_density_data_notifications_api_key = population_density_data_notifications_api_key

        if region_device_count_notifications_api_key is None:
            region_device_count_notifications_api_key = os.environ.get(
                "CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY"
            )
        if region_device_count_notifications_api_key is None:
            raise CamaraError(
                "The region_device_count_notifications_api_key client option must be set either by passing region_device_count_notifications_api_key to the client or by setting the CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY environment variable"
            )
        self.region_device_count_notifications_api_key = region_device_count_notifications_api_key

        if connectivity_insights_notifications_api_key is None:
            connectivity_insights_notifications_api_key = os.environ.get(
                "CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY"
            )
        if connectivity_insights_notifications_api_key is None:
            raise CamaraError(
                "The connectivity_insights_notifications_api_key client option must be set either by passing connectivity_insights_notifications_api_key to the client or by setting the CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.connectivity_insights_notifications_api_key = connectivity_insights_notifications_api_key

        if sim_swap_notifications_api_key is None:
            sim_swap_notifications_api_key = os.environ.get("CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY")
        if sim_swap_notifications_api_key is None:
            raise CamaraError(
                "The sim_swap_notifications_api_key client option must be set either by passing sim_swap_notifications_api_key to the client or by setting the CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY environment variable"
            )
        self.sim_swap_notifications_api_key = sim_swap_notifications_api_key

        if device_roaming_status_notifications_api_key is None:
            device_roaming_status_notifications_api_key = os.environ.get(
                "CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY"
            )
        if device_roaming_status_notifications_api_key is None:
            raise CamaraError(
                "The device_roaming_status_notifications_api_key client option must be set either by passing device_roaming_status_notifications_api_key to the client or by setting the CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_roaming_status_notifications_api_key = device_roaming_status_notifications_api_key

        if device_reachability_status_notifications_api_key is None:
            device_reachability_status_notifications_api_key = os.environ.get(
                "CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY"
            )
        if device_reachability_status_notifications_api_key is None:
            raise CamaraError(
                "The device_reachability_status_notifications_api_key client option must be set either by passing device_reachability_status_notifications_api_key to the client or by setting the CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_reachability_status_notifications_api_key = device_reachability_status_notifications_api_key

        if connected_network_type_notifications_api_key is None:
            connected_network_type_notifications_api_key = os.environ.get(
                "CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY"
            )
        if connected_network_type_notifications_api_key is None:
            raise CamaraError(
                "The connected_network_type_notifications_api_key client option must be set either by passing connected_network_type_notifications_api_key to the client or by setting the CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY environment variable"
            )
        self.connected_network_type_notifications_api_key = connected_network_type_notifications_api_key

        if base_url is None:
            base_url = os.environ.get("CAMARA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com/camara"

        custom_headers_env = os.environ.get("CAMARA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def customerinsights(self) -> CustomerinsightsResource:
        from .resources.customerinsights import CustomerinsightsResource

        return CustomerinsightsResource(self)

    @cached_property
    def deviceswap(self) -> DeviceswapResource:
        """Device Swap"""
        from .resources.deviceswap import DeviceswapResource

        return DeviceswapResource(self)

    @cached_property
    def knowyourcustomerageverification(self) -> KnowyourcustomerageverificationResource:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import KnowyourcustomerageverificationResource

        return KnowyourcustomerageverificationResource(self)

    @cached_property
    def knowyourcustomerfill_in(self) -> KnowyourcustomerfillInResource:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import KnowyourcustomerfillInResource

        return KnowyourcustomerfillInResource(self)

    @cached_property
    def knowyourcustomermatch(self) -> KnowyourcustomermatchResource:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import KnowyourcustomermatchResource

        return KnowyourcustomermatchResource(self)

    @cached_property
    def tenure(self) -> TenureResource:
        """KYC Tenure"""
        from .resources.tenure import TenureResource

        return TenureResource(self)

    @cached_property
    def numberrecycling(self) -> NumberrecyclingResource:
        """Number Recycling"""
        from .resources.numberrecycling import NumberrecyclingResource

        return NumberrecyclingResource(self)

    @cached_property
    def otpvalidation(self) -> OtpvalidationResource:
        """One Time Password SMS"""
        from .resources.otpvalidation import OtpvalidationResource

        return OtpvalidationResource(self)

    @cached_property
    def callforwardingsignal(self) -> CallforwardingsignalResource:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import CallforwardingsignalResource

        return CallforwardingsignalResource(self)

    @cached_property
    def devicelocation(self) -> DevicelocationResource:
        from .resources.devicelocation import DevicelocationResource

        return DevicelocationResource(self)

    @cached_property
    def populationdensitydata(self) -> PopulationdensitydataResource:
        """Population Density Data"""
        from .resources.populationdensitydata import PopulationdensitydataResource

        return PopulationdensitydataResource(self)

    @cached_property
    def regiondevicecount(self) -> RegiondevicecountResource:
        """Region Device Count"""
        from .resources.regiondevicecount import RegiondevicecountResource

        return RegiondevicecountResource(self)

    @cached_property
    def webrtc(self) -> WebrtcResource:
        from .resources.webrtc import WebrtcResource

        return WebrtcResource(self)

    @cached_property
    def connectivityinsights(self) -> ConnectivityinsightsResource:
        from .resources.connectivityinsights import ConnectivityinsightsResource

        return ConnectivityinsightsResource(self)

    @cached_property
    def qualityondemand(self) -> QualityondemandResource:
        """QoS Profiles"""
        from .resources.qualityondemand import QualityondemandResource

        return QualityondemandResource(self)

    @cached_property
    def deviceidentifier(self) -> DeviceidentifierResource:
        """Device Identifier"""
        from .resources.deviceidentifier import DeviceidentifierResource

        return DeviceidentifierResource(self)

    @cached_property
    def simswap(self) -> SimswapResource:
        from .resources.simswap import SimswapResource

        return SimswapResource(self)

    @cached_property
    def deviceroamingstatus(self) -> DeviceroamingstatusResource:
        from .resources.deviceroamingstatus import DeviceroamingstatusResource

        return DeviceroamingstatusResource(self)

    @cached_property
    def devicereachabilitystatus(self) -> DevicereachabilitystatusResource:
        from .resources.devicereachabilitystatus import DevicereachabilitystatusResource

        return DevicereachabilitystatusResource(self)

    @cached_property
    def connectednetworktype(self) -> ConnectednetworktypeResource:
        from .resources.connectednetworktype import ConnectednetworktypeResource

        return ConnectednetworktypeResource(self)

    @cached_property
    def with_raw_response(self) -> CamaraWithRawResponse:
        return CamaraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CamaraWithStreamedResponse:
        return CamaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._customer_insightsopen_id,
            **self._open_id,
            **self._device_swapopen_id,
            **self._know_your_customer_age_verificationopen_id,
            **self._know_your_customer_fill_inopen_id,
            **self._know_your_customer_matchopen_id,
            **self._tenureopen_id,
            **self._number_recyclingopen_id,
            **self._otp_validationopen_id,
            **self._call_forwarding_signalopen_id,
            **self._device_locationopen_id,
            **self._device_locationnotifications_bearer_auth,
            **self._notifications_bearer_auth,
            **self._population_density_dataopen_id,
            **self._population_density_datanotifications_bearer_auth,
            **self._region_device_countopen_id,
            **self._region_device_countnotifications_bearer_auth,
            **self._web_rt_copen_id,
            **self._connectivity_insightsopen_id,
            **self._connectivity_insightsnotifications_bearer_auth,
            **self._quality_on_demandopen_id,
            **self._device_identifieropen_id,
            **self._sim_swapopen_id,
            **self._sim_swapnotifications_bearer_auth,
            **self._device_roaming_statusopen_id,
            **self._device_roaming_statusnotifications_bearer_auth,
            **self._device_reachability_statusopen_id,
            **self._device_reachability_statusnotifications_bearer_auth,
            **self._connected_network_typeopen_id,
            **self._connected_network_typenotifications_bearer_auth,
        }

    @property
    def _customer_insightsopen_id(self) -> dict[str, str]:
        customer_insights_token = self.customer_insights_token
        return {"Authorization": f"Bearer {customer_insights_token}"}

    @property
    def _open_id(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _device_swapopen_id(self) -> dict[str, str]:
        device_swap_token = self.device_swap_token
        return {"Authorization": f"Bearer {device_swap_token}"}

    @property
    def _know_your_customer_age_verificationopen_id(self) -> dict[str, str]:
        kyc_age_verification_token = self.kyc_age_verification_token
        return {"Authorization": f"Bearer {kyc_age_verification_token}"}

    @property
    def _know_your_customer_fill_inopen_id(self) -> dict[str, str]:
        kyc_fill_in_token = self.kyc_fill_in_token
        return {"Authorization": f"Bearer {kyc_fill_in_token}"}

    @property
    def _know_your_customer_matchopen_id(self) -> dict[str, str]:
        kyc_match_token = self.kyc_match_token
        return {"Authorization": f"Bearer {kyc_match_token}"}

    @property
    def _tenureopen_id(self) -> dict[str, str]:
        tenure_token = self.tenure_token
        return {"Authorization": f"Bearer {tenure_token}"}

    @property
    def _number_recyclingopen_id(self) -> dict[str, str]:
        number_recycling_token = self.number_recycling_token
        return {"Authorization": f"Bearer {number_recycling_token}"}

    @property
    def _otp_validationopen_id(self) -> dict[str, str]:
        otp_validation_token = self.otp_validation_token
        return {"Authorization": f"Bearer {otp_validation_token}"}

    @property
    def _call_forwarding_signalopen_id(self) -> dict[str, str]:
        call_forwarding_signal_token = self.call_forwarding_signal_token
        return {"Authorization": f"Bearer {call_forwarding_signal_token}"}

    @property
    def _device_locationopen_id(self) -> dict[str, str]:
        device_location_token = self.device_location_token
        return {"Authorization": f"Bearer {device_location_token}"}

    @property
    def _device_locationnotifications_bearer_auth(self) -> dict[str, str]:
        device_location_notifications_api_key = self.device_location_notifications_api_key
        return {"Authorization": f"Bearer {device_location_notifications_api_key}"}

    @property
    def _notifications_bearer_auth(self) -> dict[str, str]:
        notifications_api_key = self.notifications_api_key
        return {"Authorization": f"Bearer {notifications_api_key}"}

    @property
    def _population_density_dataopen_id(self) -> dict[str, str]:
        population_density_data_token = self.population_density_data_token
        return {"Authorization": f"Bearer {population_density_data_token}"}

    @property
    def _population_density_datanotifications_bearer_auth(self) -> dict[str, str]:
        population_density_data_notifications_api_key = self.population_density_data_notifications_api_key
        return {"Authorization": f"Bearer {population_density_data_notifications_api_key}"}

    @property
    def _region_device_countopen_id(self) -> dict[str, str]:
        region_device_count_token = self.region_device_count_token
        return {"Authorization": f"Bearer {region_device_count_token}"}

    @property
    def _region_device_countnotifications_bearer_auth(self) -> dict[str, str]:
        region_device_count_notifications_api_key = self.region_device_count_notifications_api_key
        return {"Authorization": f"Bearer {region_device_count_notifications_api_key}"}

    @property
    def _web_rt_copen_id(self) -> dict[str, str]:
        web_rtc_token = self.web_rtc_token
        return {"Authorization": f"Bearer {web_rtc_token}"}

    @property
    def _connectivity_insightsopen_id(self) -> dict[str, str]:
        connectivity_insights_token = self.connectivity_insights_token
        return {"Authorization": f"Bearer {connectivity_insights_token}"}

    @property
    def _connectivity_insightsnotifications_bearer_auth(self) -> dict[str, str]:
        connectivity_insights_notifications_api_key = self.connectivity_insights_notifications_api_key
        return {"Authorization": f"Bearer {connectivity_insights_notifications_api_key}"}

    @property
    def _quality_on_demandopen_id(self) -> dict[str, str]:
        quality_on_demand_token = self.quality_on_demand_token
        return {"Authorization": f"Bearer {quality_on_demand_token}"}

    @property
    def _device_identifieropen_id(self) -> dict[str, str]:
        device_identifier_token = self.device_identifier_token
        return {"Authorization": f"Bearer {device_identifier_token}"}

    @property
    def _sim_swapopen_id(self) -> dict[str, str]:
        sim_swap_token = self.sim_swap_token
        return {"Authorization": f"Bearer {sim_swap_token}"}

    @property
    def _sim_swapnotifications_bearer_auth(self) -> dict[str, str]:
        sim_swap_notifications_api_key = self.sim_swap_notifications_api_key
        return {"Authorization": f"Bearer {sim_swap_notifications_api_key}"}

    @property
    def _device_roaming_statusopen_id(self) -> dict[str, str]:
        device_roaming_status_token = self.device_roaming_status_token
        return {"Authorization": f"Bearer {device_roaming_status_token}"}

    @property
    def _device_roaming_statusnotifications_bearer_auth(self) -> dict[str, str]:
        device_roaming_status_notifications_api_key = self.device_roaming_status_notifications_api_key
        return {"Authorization": f"Bearer {device_roaming_status_notifications_api_key}"}

    @property
    def _device_reachability_statusopen_id(self) -> dict[str, str]:
        device_reachability_status_token = self.device_reachability_status_token
        return {"Authorization": f"Bearer {device_reachability_status_token}"}

    @property
    def _device_reachability_statusnotifications_bearer_auth(self) -> dict[str, str]:
        device_reachability_status_notifications_api_key = self.device_reachability_status_notifications_api_key
        return {"Authorization": f"Bearer {device_reachability_status_notifications_api_key}"}

    @property
    def _connected_network_typeopen_id(self) -> dict[str, str]:
        connected_network_type_token = self.connected_network_type_token
        return {"Authorization": f"Bearer {connected_network_type_token}"}

    @property
    def _connected_network_typenotifications_bearer_auth(self) -> dict[str, str]:
        connected_network_type_notifications_api_key = self.connected_network_type_notifications_api_key
        return {"Authorization": f"Bearer {connected_network_type_notifications_api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        customer_insights_token: str | None = None,
        device_swap_token: str | None = None,
        kyc_age_verification_token: str | None = None,
        kyc_fill_in_token: str | None = None,
        kyc_match_token: str | None = None,
        tenure_token: str | None = None,
        number_recycling_token: str | None = None,
        otp_validation_token: str | None = None,
        call_forwarding_signal_token: str | None = None,
        device_location_token: str | None = None,
        population_density_data_token: str | None = None,
        region_device_count_token: str | None = None,
        web_rtc_token: str | None = None,
        connectivity_insights_token: str | None = None,
        quality_on_demand_token: str | None = None,
        device_identifier_token: str | None = None,
        sim_swap_token: str | None = None,
        device_roaming_status_token: str | None = None,
        device_reachability_status_token: str | None = None,
        connected_network_type_token: str | None = None,
        device_location_notifications_api_key: str | None = None,
        notifications_api_key: str | None = None,
        population_density_data_notifications_api_key: str | None = None,
        region_device_count_notifications_api_key: str | None = None,
        connectivity_insights_notifications_api_key: str | None = None,
        sim_swap_notifications_api_key: str | None = None,
        device_roaming_status_notifications_api_key: str | None = None,
        device_reachability_status_notifications_api_key: str | None = None,
        connected_network_type_notifications_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            customer_insights_token=customer_insights_token or self.customer_insights_token,
            device_swap_token=device_swap_token or self.device_swap_token,
            kyc_age_verification_token=kyc_age_verification_token or self.kyc_age_verification_token,
            kyc_fill_in_token=kyc_fill_in_token or self.kyc_fill_in_token,
            kyc_match_token=kyc_match_token or self.kyc_match_token,
            tenure_token=tenure_token or self.tenure_token,
            number_recycling_token=number_recycling_token or self.number_recycling_token,
            otp_validation_token=otp_validation_token or self.otp_validation_token,
            call_forwarding_signal_token=call_forwarding_signal_token or self.call_forwarding_signal_token,
            device_location_token=device_location_token or self.device_location_token,
            population_density_data_token=population_density_data_token or self.population_density_data_token,
            region_device_count_token=region_device_count_token or self.region_device_count_token,
            web_rtc_token=web_rtc_token or self.web_rtc_token,
            connectivity_insights_token=connectivity_insights_token or self.connectivity_insights_token,
            quality_on_demand_token=quality_on_demand_token or self.quality_on_demand_token,
            device_identifier_token=device_identifier_token or self.device_identifier_token,
            sim_swap_token=sim_swap_token or self.sim_swap_token,
            device_roaming_status_token=device_roaming_status_token or self.device_roaming_status_token,
            device_reachability_status_token=device_reachability_status_token or self.device_reachability_status_token,
            connected_network_type_token=connected_network_type_token or self.connected_network_type_token,
            device_location_notifications_api_key=device_location_notifications_api_key
            or self.device_location_notifications_api_key,
            notifications_api_key=notifications_api_key or self.notifications_api_key,
            population_density_data_notifications_api_key=population_density_data_notifications_api_key
            or self.population_density_data_notifications_api_key,
            region_device_count_notifications_api_key=region_device_count_notifications_api_key
            or self.region_device_count_notifications_api_key,
            connectivity_insights_notifications_api_key=connectivity_insights_notifications_api_key
            or self.connectivity_insights_notifications_api_key,
            sim_swap_notifications_api_key=sim_swap_notifications_api_key or self.sim_swap_notifications_api_key,
            device_roaming_status_notifications_api_key=device_roaming_status_notifications_api_key
            or self.device_roaming_status_notifications_api_key,
            device_reachability_status_notifications_api_key=device_reachability_status_notifications_api_key
            or self.device_reachability_status_notifications_api_key,
            connected_network_type_notifications_api_key=connected_network_type_notifications_api_key
            or self.connected_network_type_notifications_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCamara(AsyncAPIClient):
    # client options
    bearer_token: str
    customer_insights_token: str
    device_swap_token: str
    kyc_age_verification_token: str
    kyc_fill_in_token: str
    kyc_match_token: str
    tenure_token: str
    number_recycling_token: str
    otp_validation_token: str
    call_forwarding_signal_token: str
    device_location_token: str
    population_density_data_token: str
    region_device_count_token: str
    web_rtc_token: str
    connectivity_insights_token: str
    quality_on_demand_token: str
    device_identifier_token: str
    sim_swap_token: str
    device_roaming_status_token: str
    device_reachability_status_token: str
    connected_network_type_token: str
    device_location_notifications_api_key: str
    notifications_api_key: str
    population_density_data_notifications_api_key: str
    region_device_count_notifications_api_key: str
    connectivity_insights_notifications_api_key: str
    sim_swap_notifications_api_key: str
    device_roaming_status_notifications_api_key: str
    device_reachability_status_notifications_api_key: str
    connected_network_type_notifications_api_key: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        customer_insights_token: str | None = None,
        device_swap_token: str | None = None,
        kyc_age_verification_token: str | None = None,
        kyc_fill_in_token: str | None = None,
        kyc_match_token: str | None = None,
        tenure_token: str | None = None,
        number_recycling_token: str | None = None,
        otp_validation_token: str | None = None,
        call_forwarding_signal_token: str | None = None,
        device_location_token: str | None = None,
        population_density_data_token: str | None = None,
        region_device_count_token: str | None = None,
        web_rtc_token: str | None = None,
        connectivity_insights_token: str | None = None,
        quality_on_demand_token: str | None = None,
        device_identifier_token: str | None = None,
        sim_swap_token: str | None = None,
        device_roaming_status_token: str | None = None,
        device_reachability_status_token: str | None = None,
        connected_network_type_token: str | None = None,
        device_location_notifications_api_key: str | None = None,
        notifications_api_key: str | None = None,
        population_density_data_notifications_api_key: str | None = None,
        region_device_count_notifications_api_key: str | None = None,
        connectivity_insights_notifications_api_key: str | None = None,
        sim_swap_notifications_api_key: str | None = None,
        device_roaming_status_notifications_api_key: str | None = None,
        device_reachability_status_notifications_api_key: str | None = None,
        connected_network_type_notifications_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCamara client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `CAMARA_BEARER_TOKEN`
        - `customer_insights_token` from `CAMARA_BEARER_TOKEN`
        - `device_swap_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_age_verification_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_fill_in_token` from `CAMARA_BEARER_TOKEN`
        - `kyc_match_token` from `CAMARA_BEARER_TOKEN`
        - `tenure_token` from `CAMARA_BEARER_TOKEN`
        - `number_recycling_token` from `CAMARA_BEARER_TOKEN`
        - `otp_validation_token` from `CAMARA_BEARER_TOKEN`
        - `call_forwarding_signal_token` from `CAMARA_BEARER_TOKEN`
        - `device_location_token` from `CAMARA_BEARER_TOKEN`
        - `population_density_data_token` from `CAMARA_BEARER_TOKEN`
        - `region_device_count_token` from `CAMARA_BEARER_TOKEN`
        - `web_rtc_token` from `CAMARA_BEARER_TOKEN`
        - `connectivity_insights_token` from `CAMARA_BEARER_TOKEN`
        - `quality_on_demand_token` from `CAMARA_BEARER_TOKEN`
        - `device_identifier_token` from `CAMARA_BEARER_TOKEN`
        - `sim_swap_token` from `CAMARA_BEARER_TOKEN`
        - `device_roaming_status_token` from `CAMARA_BEARER_TOKEN`
        - `device_reachability_status_token` from `CAMARA_BEARER_TOKEN`
        - `connected_network_type_token` from `CAMARA_BEARER_TOKEN`
        - `device_location_notifications_api_key` from `CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY`
        - `notifications_api_key` from `CAMARA_NOTIFICATIONS_API_KEY`
        - `population_density_data_notifications_api_key` from `CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY`
        - `region_device_count_notifications_api_key` from `CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY`
        - `connectivity_insights_notifications_api_key` from `CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY`
        - `sim_swap_notifications_api_key` from `CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY`
        - `device_roaming_status_notifications_api_key` from `CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY`
        - `device_reachability_status_notifications_api_key` from `CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY`
        - `connected_network_type_notifications_api_key` from `CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if bearer_token is None:
            raise CamaraError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if customer_insights_token is None:
            customer_insights_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if customer_insights_token is None:
            raise CamaraError(
                "The customer_insights_token client option must be set either by passing customer_insights_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.customer_insights_token = customer_insights_token

        if device_swap_token is None:
            device_swap_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_swap_token is None:
            raise CamaraError(
                "The device_swap_token client option must be set either by passing device_swap_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_swap_token = device_swap_token

        if kyc_age_verification_token is None:
            kyc_age_verification_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_age_verification_token is None:
            raise CamaraError(
                "The kyc_age_verification_token client option must be set either by passing kyc_age_verification_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_age_verification_token = kyc_age_verification_token

        if kyc_fill_in_token is None:
            kyc_fill_in_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_fill_in_token is None:
            raise CamaraError(
                "The kyc_fill_in_token client option must be set either by passing kyc_fill_in_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_fill_in_token = kyc_fill_in_token

        if kyc_match_token is None:
            kyc_match_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if kyc_match_token is None:
            raise CamaraError(
                "The kyc_match_token client option must be set either by passing kyc_match_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.kyc_match_token = kyc_match_token

        if tenure_token is None:
            tenure_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if tenure_token is None:
            raise CamaraError(
                "The tenure_token client option must be set either by passing tenure_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.tenure_token = tenure_token

        if number_recycling_token is None:
            number_recycling_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if number_recycling_token is None:
            raise CamaraError(
                "The number_recycling_token client option must be set either by passing number_recycling_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.number_recycling_token = number_recycling_token

        if otp_validation_token is None:
            otp_validation_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if otp_validation_token is None:
            raise CamaraError(
                "The otp_validation_token client option must be set either by passing otp_validation_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.otp_validation_token = otp_validation_token

        if call_forwarding_signal_token is None:
            call_forwarding_signal_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if call_forwarding_signal_token is None:
            raise CamaraError(
                "The call_forwarding_signal_token client option must be set either by passing call_forwarding_signal_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.call_forwarding_signal_token = call_forwarding_signal_token

        if device_location_token is None:
            device_location_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_location_token is None:
            raise CamaraError(
                "The device_location_token client option must be set either by passing device_location_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_location_token = device_location_token

        if population_density_data_token is None:
            population_density_data_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if population_density_data_token is None:
            raise CamaraError(
                "The population_density_data_token client option must be set either by passing population_density_data_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.population_density_data_token = population_density_data_token

        if region_device_count_token is None:
            region_device_count_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if region_device_count_token is None:
            raise CamaraError(
                "The region_device_count_token client option must be set either by passing region_device_count_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.region_device_count_token = region_device_count_token

        if web_rtc_token is None:
            web_rtc_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if web_rtc_token is None:
            raise CamaraError(
                "The web_rtc_token client option must be set either by passing web_rtc_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.web_rtc_token = web_rtc_token

        if connectivity_insights_token is None:
            connectivity_insights_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if connectivity_insights_token is None:
            raise CamaraError(
                "The connectivity_insights_token client option must be set either by passing connectivity_insights_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.connectivity_insights_token = connectivity_insights_token

        if quality_on_demand_token is None:
            quality_on_demand_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if quality_on_demand_token is None:
            raise CamaraError(
                "The quality_on_demand_token client option must be set either by passing quality_on_demand_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.quality_on_demand_token = quality_on_demand_token

        if device_identifier_token is None:
            device_identifier_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_identifier_token is None:
            raise CamaraError(
                "The device_identifier_token client option must be set either by passing device_identifier_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_identifier_token = device_identifier_token

        if sim_swap_token is None:
            sim_swap_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if sim_swap_token is None:
            raise CamaraError(
                "The sim_swap_token client option must be set either by passing sim_swap_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.sim_swap_token = sim_swap_token

        if device_roaming_status_token is None:
            device_roaming_status_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_roaming_status_token is None:
            raise CamaraError(
                "The device_roaming_status_token client option must be set either by passing device_roaming_status_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_roaming_status_token = device_roaming_status_token

        if device_reachability_status_token is None:
            device_reachability_status_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if device_reachability_status_token is None:
            raise CamaraError(
                "The device_reachability_status_token client option must be set either by passing device_reachability_status_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.device_reachability_status_token = device_reachability_status_token

        if connected_network_type_token is None:
            connected_network_type_token = os.environ.get("CAMARA_BEARER_TOKEN")
        if connected_network_type_token is None:
            raise CamaraError(
                "The connected_network_type_token client option must be set either by passing connected_network_type_token to the client or by setting the CAMARA_BEARER_TOKEN environment variable"
            )
        self.connected_network_type_token = connected_network_type_token

        if device_location_notifications_api_key is None:
            device_location_notifications_api_key = os.environ.get("CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY")
        if device_location_notifications_api_key is None:
            raise CamaraError(
                "The device_location_notifications_api_key client option must be set either by passing device_location_notifications_api_key to the client or by setting the CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_location_notifications_api_key = device_location_notifications_api_key

        if notifications_api_key is None:
            notifications_api_key = os.environ.get("CAMARA_NOTIFICATIONS_API_KEY")
        if notifications_api_key is None:
            raise CamaraError(
                "The notifications_api_key client option must be set either by passing notifications_api_key to the client or by setting the CAMARA_NOTIFICATIONS_API_KEY environment variable"
            )
        self.notifications_api_key = notifications_api_key

        if population_density_data_notifications_api_key is None:
            population_density_data_notifications_api_key = os.environ.get(
                "CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY"
            )
        if population_density_data_notifications_api_key is None:
            raise CamaraError(
                "The population_density_data_notifications_api_key client option must be set either by passing population_density_data_notifications_api_key to the client or by setting the CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY environment variable"
            )
        self.population_density_data_notifications_api_key = population_density_data_notifications_api_key

        if region_device_count_notifications_api_key is None:
            region_device_count_notifications_api_key = os.environ.get(
                "CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY"
            )
        if region_device_count_notifications_api_key is None:
            raise CamaraError(
                "The region_device_count_notifications_api_key client option must be set either by passing region_device_count_notifications_api_key to the client or by setting the CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY environment variable"
            )
        self.region_device_count_notifications_api_key = region_device_count_notifications_api_key

        if connectivity_insights_notifications_api_key is None:
            connectivity_insights_notifications_api_key = os.environ.get(
                "CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY"
            )
        if connectivity_insights_notifications_api_key is None:
            raise CamaraError(
                "The connectivity_insights_notifications_api_key client option must be set either by passing connectivity_insights_notifications_api_key to the client or by setting the CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.connectivity_insights_notifications_api_key = connectivity_insights_notifications_api_key

        if sim_swap_notifications_api_key is None:
            sim_swap_notifications_api_key = os.environ.get("CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY")
        if sim_swap_notifications_api_key is None:
            raise CamaraError(
                "The sim_swap_notifications_api_key client option must be set either by passing sim_swap_notifications_api_key to the client or by setting the CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY environment variable"
            )
        self.sim_swap_notifications_api_key = sim_swap_notifications_api_key

        if device_roaming_status_notifications_api_key is None:
            device_roaming_status_notifications_api_key = os.environ.get(
                "CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY"
            )
        if device_roaming_status_notifications_api_key is None:
            raise CamaraError(
                "The device_roaming_status_notifications_api_key client option must be set either by passing device_roaming_status_notifications_api_key to the client or by setting the CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_roaming_status_notifications_api_key = device_roaming_status_notifications_api_key

        if device_reachability_status_notifications_api_key is None:
            device_reachability_status_notifications_api_key = os.environ.get(
                "CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY"
            )
        if device_reachability_status_notifications_api_key is None:
            raise CamaraError(
                "The device_reachability_status_notifications_api_key client option must be set either by passing device_reachability_status_notifications_api_key to the client or by setting the CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY environment variable"
            )
        self.device_reachability_status_notifications_api_key = device_reachability_status_notifications_api_key

        if connected_network_type_notifications_api_key is None:
            connected_network_type_notifications_api_key = os.environ.get(
                "CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY"
            )
        if connected_network_type_notifications_api_key is None:
            raise CamaraError(
                "The connected_network_type_notifications_api_key client option must be set either by passing connected_network_type_notifications_api_key to the client or by setting the CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY environment variable"
            )
        self.connected_network_type_notifications_api_key = connected_network_type_notifications_api_key

        if base_url is None:
            base_url = os.environ.get("CAMARA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com/camara"

        custom_headers_env = os.environ.get("CAMARA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def customerinsights(self) -> AsyncCustomerinsightsResource:
        from .resources.customerinsights import AsyncCustomerinsightsResource

        return AsyncCustomerinsightsResource(self)

    @cached_property
    def deviceswap(self) -> AsyncDeviceswapResource:
        """Device Swap"""
        from .resources.deviceswap import AsyncDeviceswapResource

        return AsyncDeviceswapResource(self)

    @cached_property
    def knowyourcustomerageverification(self) -> AsyncKnowyourcustomerageverificationResource:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import AsyncKnowyourcustomerageverificationResource

        return AsyncKnowyourcustomerageverificationResource(self)

    @cached_property
    def knowyourcustomerfill_in(self) -> AsyncKnowyourcustomerfillInResource:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import AsyncKnowyourcustomerfillInResource

        return AsyncKnowyourcustomerfillInResource(self)

    @cached_property
    def knowyourcustomermatch(self) -> AsyncKnowyourcustomermatchResource:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import AsyncKnowyourcustomermatchResource

        return AsyncKnowyourcustomermatchResource(self)

    @cached_property
    def tenure(self) -> AsyncTenureResource:
        """KYC Tenure"""
        from .resources.tenure import AsyncTenureResource

        return AsyncTenureResource(self)

    @cached_property
    def numberrecycling(self) -> AsyncNumberrecyclingResource:
        """Number Recycling"""
        from .resources.numberrecycling import AsyncNumberrecyclingResource

        return AsyncNumberrecyclingResource(self)

    @cached_property
    def otpvalidation(self) -> AsyncOtpvalidationResource:
        """One Time Password SMS"""
        from .resources.otpvalidation import AsyncOtpvalidationResource

        return AsyncOtpvalidationResource(self)

    @cached_property
    def callforwardingsignal(self) -> AsyncCallforwardingsignalResource:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import AsyncCallforwardingsignalResource

        return AsyncCallforwardingsignalResource(self)

    @cached_property
    def devicelocation(self) -> AsyncDevicelocationResource:
        from .resources.devicelocation import AsyncDevicelocationResource

        return AsyncDevicelocationResource(self)

    @cached_property
    def populationdensitydata(self) -> AsyncPopulationdensitydataResource:
        """Population Density Data"""
        from .resources.populationdensitydata import AsyncPopulationdensitydataResource

        return AsyncPopulationdensitydataResource(self)

    @cached_property
    def regiondevicecount(self) -> AsyncRegiondevicecountResource:
        """Region Device Count"""
        from .resources.regiondevicecount import AsyncRegiondevicecountResource

        return AsyncRegiondevicecountResource(self)

    @cached_property
    def webrtc(self) -> AsyncWebrtcResource:
        from .resources.webrtc import AsyncWebrtcResource

        return AsyncWebrtcResource(self)

    @cached_property
    def connectivityinsights(self) -> AsyncConnectivityinsightsResource:
        from .resources.connectivityinsights import AsyncConnectivityinsightsResource

        return AsyncConnectivityinsightsResource(self)

    @cached_property
    def qualityondemand(self) -> AsyncQualityondemandResource:
        """QoS Profiles"""
        from .resources.qualityondemand import AsyncQualityondemandResource

        return AsyncQualityondemandResource(self)

    @cached_property
    def deviceidentifier(self) -> AsyncDeviceidentifierResource:
        """Device Identifier"""
        from .resources.deviceidentifier import AsyncDeviceidentifierResource

        return AsyncDeviceidentifierResource(self)

    @cached_property
    def simswap(self) -> AsyncSimswapResource:
        from .resources.simswap import AsyncSimswapResource

        return AsyncSimswapResource(self)

    @cached_property
    def deviceroamingstatus(self) -> AsyncDeviceroamingstatusResource:
        from .resources.deviceroamingstatus import AsyncDeviceroamingstatusResource

        return AsyncDeviceroamingstatusResource(self)

    @cached_property
    def devicereachabilitystatus(self) -> AsyncDevicereachabilitystatusResource:
        from .resources.devicereachabilitystatus import AsyncDevicereachabilitystatusResource

        return AsyncDevicereachabilitystatusResource(self)

    @cached_property
    def connectednetworktype(self) -> AsyncConnectednetworktypeResource:
        from .resources.connectednetworktype import AsyncConnectednetworktypeResource

        return AsyncConnectednetworktypeResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCamaraWithRawResponse:
        return AsyncCamaraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCamaraWithStreamedResponse:
        return AsyncCamaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._customer_insightsopen_id,
            **self._open_id,
            **self._device_swapopen_id,
            **self._know_your_customer_age_verificationopen_id,
            **self._know_your_customer_fill_inopen_id,
            **self._know_your_customer_matchopen_id,
            **self._tenureopen_id,
            **self._number_recyclingopen_id,
            **self._otp_validationopen_id,
            **self._call_forwarding_signalopen_id,
            **self._device_locationopen_id,
            **self._device_locationnotifications_bearer_auth,
            **self._notifications_bearer_auth,
            **self._population_density_dataopen_id,
            **self._population_density_datanotifications_bearer_auth,
            **self._region_device_countopen_id,
            **self._region_device_countnotifications_bearer_auth,
            **self._web_rt_copen_id,
            **self._connectivity_insightsopen_id,
            **self._connectivity_insightsnotifications_bearer_auth,
            **self._quality_on_demandopen_id,
            **self._device_identifieropen_id,
            **self._sim_swapopen_id,
            **self._sim_swapnotifications_bearer_auth,
            **self._device_roaming_statusopen_id,
            **self._device_roaming_statusnotifications_bearer_auth,
            **self._device_reachability_statusopen_id,
            **self._device_reachability_statusnotifications_bearer_auth,
            **self._connected_network_typeopen_id,
            **self._connected_network_typenotifications_bearer_auth,
        }

    @property
    def _customer_insightsopen_id(self) -> dict[str, str]:
        customer_insights_token = self.customer_insights_token
        return {"Authorization": f"Bearer {customer_insights_token}"}

    @property
    def _open_id(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _device_swapopen_id(self) -> dict[str, str]:
        device_swap_token = self.device_swap_token
        return {"Authorization": f"Bearer {device_swap_token}"}

    @property
    def _know_your_customer_age_verificationopen_id(self) -> dict[str, str]:
        kyc_age_verification_token = self.kyc_age_verification_token
        return {"Authorization": f"Bearer {kyc_age_verification_token}"}

    @property
    def _know_your_customer_fill_inopen_id(self) -> dict[str, str]:
        kyc_fill_in_token = self.kyc_fill_in_token
        return {"Authorization": f"Bearer {kyc_fill_in_token}"}

    @property
    def _know_your_customer_matchopen_id(self) -> dict[str, str]:
        kyc_match_token = self.kyc_match_token
        return {"Authorization": f"Bearer {kyc_match_token}"}

    @property
    def _tenureopen_id(self) -> dict[str, str]:
        tenure_token = self.tenure_token
        return {"Authorization": f"Bearer {tenure_token}"}

    @property
    def _number_recyclingopen_id(self) -> dict[str, str]:
        number_recycling_token = self.number_recycling_token
        return {"Authorization": f"Bearer {number_recycling_token}"}

    @property
    def _otp_validationopen_id(self) -> dict[str, str]:
        otp_validation_token = self.otp_validation_token
        return {"Authorization": f"Bearer {otp_validation_token}"}

    @property
    def _call_forwarding_signalopen_id(self) -> dict[str, str]:
        call_forwarding_signal_token = self.call_forwarding_signal_token
        return {"Authorization": f"Bearer {call_forwarding_signal_token}"}

    @property
    def _device_locationopen_id(self) -> dict[str, str]:
        device_location_token = self.device_location_token
        return {"Authorization": f"Bearer {device_location_token}"}

    @property
    def _device_locationnotifications_bearer_auth(self) -> dict[str, str]:
        device_location_notifications_api_key = self.device_location_notifications_api_key
        return {"Authorization": f"Bearer {device_location_notifications_api_key}"}

    @property
    def _notifications_bearer_auth(self) -> dict[str, str]:
        notifications_api_key = self.notifications_api_key
        return {"Authorization": f"Bearer {notifications_api_key}"}

    @property
    def _population_density_dataopen_id(self) -> dict[str, str]:
        population_density_data_token = self.population_density_data_token
        return {"Authorization": f"Bearer {population_density_data_token}"}

    @property
    def _population_density_datanotifications_bearer_auth(self) -> dict[str, str]:
        population_density_data_notifications_api_key = self.population_density_data_notifications_api_key
        return {"Authorization": f"Bearer {population_density_data_notifications_api_key}"}

    @property
    def _region_device_countopen_id(self) -> dict[str, str]:
        region_device_count_token = self.region_device_count_token
        return {"Authorization": f"Bearer {region_device_count_token}"}

    @property
    def _region_device_countnotifications_bearer_auth(self) -> dict[str, str]:
        region_device_count_notifications_api_key = self.region_device_count_notifications_api_key
        return {"Authorization": f"Bearer {region_device_count_notifications_api_key}"}

    @property
    def _web_rt_copen_id(self) -> dict[str, str]:
        web_rtc_token = self.web_rtc_token
        return {"Authorization": f"Bearer {web_rtc_token}"}

    @property
    def _connectivity_insightsopen_id(self) -> dict[str, str]:
        connectivity_insights_token = self.connectivity_insights_token
        return {"Authorization": f"Bearer {connectivity_insights_token}"}

    @property
    def _connectivity_insightsnotifications_bearer_auth(self) -> dict[str, str]:
        connectivity_insights_notifications_api_key = self.connectivity_insights_notifications_api_key
        return {"Authorization": f"Bearer {connectivity_insights_notifications_api_key}"}

    @property
    def _quality_on_demandopen_id(self) -> dict[str, str]:
        quality_on_demand_token = self.quality_on_demand_token
        return {"Authorization": f"Bearer {quality_on_demand_token}"}

    @property
    def _device_identifieropen_id(self) -> dict[str, str]:
        device_identifier_token = self.device_identifier_token
        return {"Authorization": f"Bearer {device_identifier_token}"}

    @property
    def _sim_swapopen_id(self) -> dict[str, str]:
        sim_swap_token = self.sim_swap_token
        return {"Authorization": f"Bearer {sim_swap_token}"}

    @property
    def _sim_swapnotifications_bearer_auth(self) -> dict[str, str]:
        sim_swap_notifications_api_key = self.sim_swap_notifications_api_key
        return {"Authorization": f"Bearer {sim_swap_notifications_api_key}"}

    @property
    def _device_roaming_statusopen_id(self) -> dict[str, str]:
        device_roaming_status_token = self.device_roaming_status_token
        return {"Authorization": f"Bearer {device_roaming_status_token}"}

    @property
    def _device_roaming_statusnotifications_bearer_auth(self) -> dict[str, str]:
        device_roaming_status_notifications_api_key = self.device_roaming_status_notifications_api_key
        return {"Authorization": f"Bearer {device_roaming_status_notifications_api_key}"}

    @property
    def _device_reachability_statusopen_id(self) -> dict[str, str]:
        device_reachability_status_token = self.device_reachability_status_token
        return {"Authorization": f"Bearer {device_reachability_status_token}"}

    @property
    def _device_reachability_statusnotifications_bearer_auth(self) -> dict[str, str]:
        device_reachability_status_notifications_api_key = self.device_reachability_status_notifications_api_key
        return {"Authorization": f"Bearer {device_reachability_status_notifications_api_key}"}

    @property
    def _connected_network_typeopen_id(self) -> dict[str, str]:
        connected_network_type_token = self.connected_network_type_token
        return {"Authorization": f"Bearer {connected_network_type_token}"}

    @property
    def _connected_network_typenotifications_bearer_auth(self) -> dict[str, str]:
        connected_network_type_notifications_api_key = self.connected_network_type_notifications_api_key
        return {"Authorization": f"Bearer {connected_network_type_notifications_api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        customer_insights_token: str | None = None,
        device_swap_token: str | None = None,
        kyc_age_verification_token: str | None = None,
        kyc_fill_in_token: str | None = None,
        kyc_match_token: str | None = None,
        tenure_token: str | None = None,
        number_recycling_token: str | None = None,
        otp_validation_token: str | None = None,
        call_forwarding_signal_token: str | None = None,
        device_location_token: str | None = None,
        population_density_data_token: str | None = None,
        region_device_count_token: str | None = None,
        web_rtc_token: str | None = None,
        connectivity_insights_token: str | None = None,
        quality_on_demand_token: str | None = None,
        device_identifier_token: str | None = None,
        sim_swap_token: str | None = None,
        device_roaming_status_token: str | None = None,
        device_reachability_status_token: str | None = None,
        connected_network_type_token: str | None = None,
        device_location_notifications_api_key: str | None = None,
        notifications_api_key: str | None = None,
        population_density_data_notifications_api_key: str | None = None,
        region_device_count_notifications_api_key: str | None = None,
        connectivity_insights_notifications_api_key: str | None = None,
        sim_swap_notifications_api_key: str | None = None,
        device_roaming_status_notifications_api_key: str | None = None,
        device_reachability_status_notifications_api_key: str | None = None,
        connected_network_type_notifications_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            customer_insights_token=customer_insights_token or self.customer_insights_token,
            device_swap_token=device_swap_token or self.device_swap_token,
            kyc_age_verification_token=kyc_age_verification_token or self.kyc_age_verification_token,
            kyc_fill_in_token=kyc_fill_in_token or self.kyc_fill_in_token,
            kyc_match_token=kyc_match_token or self.kyc_match_token,
            tenure_token=tenure_token or self.tenure_token,
            number_recycling_token=number_recycling_token or self.number_recycling_token,
            otp_validation_token=otp_validation_token or self.otp_validation_token,
            call_forwarding_signal_token=call_forwarding_signal_token or self.call_forwarding_signal_token,
            device_location_token=device_location_token or self.device_location_token,
            population_density_data_token=population_density_data_token or self.population_density_data_token,
            region_device_count_token=region_device_count_token or self.region_device_count_token,
            web_rtc_token=web_rtc_token or self.web_rtc_token,
            connectivity_insights_token=connectivity_insights_token or self.connectivity_insights_token,
            quality_on_demand_token=quality_on_demand_token or self.quality_on_demand_token,
            device_identifier_token=device_identifier_token or self.device_identifier_token,
            sim_swap_token=sim_swap_token or self.sim_swap_token,
            device_roaming_status_token=device_roaming_status_token or self.device_roaming_status_token,
            device_reachability_status_token=device_reachability_status_token or self.device_reachability_status_token,
            connected_network_type_token=connected_network_type_token or self.connected_network_type_token,
            device_location_notifications_api_key=device_location_notifications_api_key
            or self.device_location_notifications_api_key,
            notifications_api_key=notifications_api_key or self.notifications_api_key,
            population_density_data_notifications_api_key=population_density_data_notifications_api_key
            or self.population_density_data_notifications_api_key,
            region_device_count_notifications_api_key=region_device_count_notifications_api_key
            or self.region_device_count_notifications_api_key,
            connectivity_insights_notifications_api_key=connectivity_insights_notifications_api_key
            or self.connectivity_insights_notifications_api_key,
            sim_swap_notifications_api_key=sim_swap_notifications_api_key or self.sim_swap_notifications_api_key,
            device_roaming_status_notifications_api_key=device_roaming_status_notifications_api_key
            or self.device_roaming_status_notifications_api_key,
            device_reachability_status_notifications_api_key=device_reachability_status_notifications_api_key
            or self.device_reachability_status_notifications_api_key,
            connected_network_type_notifications_api_key=connected_network_type_notifications_api_key
            or self.connected_network_type_notifications_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CamaraWithRawResponse:
    _client: Camara

    def __init__(self, client: Camara) -> None:
        self._client = client

    @cached_property
    def customerinsights(self) -> customerinsights.CustomerinsightsResourceWithRawResponse:
        from .resources.customerinsights import CustomerinsightsResourceWithRawResponse

        return CustomerinsightsResourceWithRawResponse(self._client.customerinsights)

    @cached_property
    def deviceswap(self) -> deviceswap.DeviceswapResourceWithRawResponse:
        """Device Swap"""
        from .resources.deviceswap import DeviceswapResourceWithRawResponse

        return DeviceswapResourceWithRawResponse(self._client.deviceswap)

    @cached_property
    def knowyourcustomerageverification(
        self,
    ) -> knowyourcustomerageverification.KnowyourcustomerageverificationResourceWithRawResponse:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import KnowyourcustomerageverificationResourceWithRawResponse

        return KnowyourcustomerageverificationResourceWithRawResponse(self._client.knowyourcustomerageverification)

    @cached_property
    def knowyourcustomerfill_in(self) -> knowyourcustomerfill_in.KnowyourcustomerfillInResourceWithRawResponse:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import KnowyourcustomerfillInResourceWithRawResponse

        return KnowyourcustomerfillInResourceWithRawResponse(self._client.knowyourcustomerfill_in)

    @cached_property
    def knowyourcustomermatch(self) -> knowyourcustomermatch.KnowyourcustomermatchResourceWithRawResponse:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import KnowyourcustomermatchResourceWithRawResponse

        return KnowyourcustomermatchResourceWithRawResponse(self._client.knowyourcustomermatch)

    @cached_property
    def tenure(self) -> tenure.TenureResourceWithRawResponse:
        """KYC Tenure"""
        from .resources.tenure import TenureResourceWithRawResponse

        return TenureResourceWithRawResponse(self._client.tenure)

    @cached_property
    def numberrecycling(self) -> numberrecycling.NumberrecyclingResourceWithRawResponse:
        """Number Recycling"""
        from .resources.numberrecycling import NumberrecyclingResourceWithRawResponse

        return NumberrecyclingResourceWithRawResponse(self._client.numberrecycling)

    @cached_property
    def otpvalidation(self) -> otpvalidation.OtpvalidationResourceWithRawResponse:
        """One Time Password SMS"""
        from .resources.otpvalidation import OtpvalidationResourceWithRawResponse

        return OtpvalidationResourceWithRawResponse(self._client.otpvalidation)

    @cached_property
    def callforwardingsignal(self) -> callforwardingsignal.CallforwardingsignalResourceWithRawResponse:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import CallforwardingsignalResourceWithRawResponse

        return CallforwardingsignalResourceWithRawResponse(self._client.callforwardingsignal)

    @cached_property
    def devicelocation(self) -> devicelocation.DevicelocationResourceWithRawResponse:
        from .resources.devicelocation import DevicelocationResourceWithRawResponse

        return DevicelocationResourceWithRawResponse(self._client.devicelocation)

    @cached_property
    def populationdensitydata(self) -> populationdensitydata.PopulationdensitydataResourceWithRawResponse:
        """Population Density Data"""
        from .resources.populationdensitydata import PopulationdensitydataResourceWithRawResponse

        return PopulationdensitydataResourceWithRawResponse(self._client.populationdensitydata)

    @cached_property
    def regiondevicecount(self) -> regiondevicecount.RegiondevicecountResourceWithRawResponse:
        """Region Device Count"""
        from .resources.regiondevicecount import RegiondevicecountResourceWithRawResponse

        return RegiondevicecountResourceWithRawResponse(self._client.regiondevicecount)

    @cached_property
    def webrtc(self) -> webrtc.WebrtcResourceWithRawResponse:
        from .resources.webrtc import WebrtcResourceWithRawResponse

        return WebrtcResourceWithRawResponse(self._client.webrtc)

    @cached_property
    def connectivityinsights(self) -> connectivityinsights.ConnectivityinsightsResourceWithRawResponse:
        from .resources.connectivityinsights import ConnectivityinsightsResourceWithRawResponse

        return ConnectivityinsightsResourceWithRawResponse(self._client.connectivityinsights)

    @cached_property
    def qualityondemand(self) -> qualityondemand.QualityondemandResourceWithRawResponse:
        """QoS Profiles"""
        from .resources.qualityondemand import QualityondemandResourceWithRawResponse

        return QualityondemandResourceWithRawResponse(self._client.qualityondemand)

    @cached_property
    def deviceidentifier(self) -> deviceidentifier.DeviceidentifierResourceWithRawResponse:
        """Device Identifier"""
        from .resources.deviceidentifier import DeviceidentifierResourceWithRawResponse

        return DeviceidentifierResourceWithRawResponse(self._client.deviceidentifier)

    @cached_property
    def simswap(self) -> simswap.SimswapResourceWithRawResponse:
        from .resources.simswap import SimswapResourceWithRawResponse

        return SimswapResourceWithRawResponse(self._client.simswap)

    @cached_property
    def deviceroamingstatus(self) -> deviceroamingstatus.DeviceroamingstatusResourceWithRawResponse:
        from .resources.deviceroamingstatus import DeviceroamingstatusResourceWithRawResponse

        return DeviceroamingstatusResourceWithRawResponse(self._client.deviceroamingstatus)

    @cached_property
    def devicereachabilitystatus(self) -> devicereachabilitystatus.DevicereachabilitystatusResourceWithRawResponse:
        from .resources.devicereachabilitystatus import DevicereachabilitystatusResourceWithRawResponse

        return DevicereachabilitystatusResourceWithRawResponse(self._client.devicereachabilitystatus)

    @cached_property
    def connectednetworktype(self) -> connectednetworktype.ConnectednetworktypeResourceWithRawResponse:
        from .resources.connectednetworktype import ConnectednetworktypeResourceWithRawResponse

        return ConnectednetworktypeResourceWithRawResponse(self._client.connectednetworktype)


class AsyncCamaraWithRawResponse:
    _client: AsyncCamara

    def __init__(self, client: AsyncCamara) -> None:
        self._client = client

    @cached_property
    def customerinsights(self) -> customerinsights.AsyncCustomerinsightsResourceWithRawResponse:
        from .resources.customerinsights import AsyncCustomerinsightsResourceWithRawResponse

        return AsyncCustomerinsightsResourceWithRawResponse(self._client.customerinsights)

    @cached_property
    def deviceswap(self) -> deviceswap.AsyncDeviceswapResourceWithRawResponse:
        """Device Swap"""
        from .resources.deviceswap import AsyncDeviceswapResourceWithRawResponse

        return AsyncDeviceswapResourceWithRawResponse(self._client.deviceswap)

    @cached_property
    def knowyourcustomerageverification(
        self,
    ) -> knowyourcustomerageverification.AsyncKnowyourcustomerageverificationResourceWithRawResponse:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import (
            AsyncKnowyourcustomerageverificationResourceWithRawResponse,
        )

        return AsyncKnowyourcustomerageverificationResourceWithRawResponse(self._client.knowyourcustomerageverification)

    @cached_property
    def knowyourcustomerfill_in(self) -> knowyourcustomerfill_in.AsyncKnowyourcustomerfillInResourceWithRawResponse:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import AsyncKnowyourcustomerfillInResourceWithRawResponse

        return AsyncKnowyourcustomerfillInResourceWithRawResponse(self._client.knowyourcustomerfill_in)

    @cached_property
    def knowyourcustomermatch(self) -> knowyourcustomermatch.AsyncKnowyourcustomermatchResourceWithRawResponse:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import AsyncKnowyourcustomermatchResourceWithRawResponse

        return AsyncKnowyourcustomermatchResourceWithRawResponse(self._client.knowyourcustomermatch)

    @cached_property
    def tenure(self) -> tenure.AsyncTenureResourceWithRawResponse:
        """KYC Tenure"""
        from .resources.tenure import AsyncTenureResourceWithRawResponse

        return AsyncTenureResourceWithRawResponse(self._client.tenure)

    @cached_property
    def numberrecycling(self) -> numberrecycling.AsyncNumberrecyclingResourceWithRawResponse:
        """Number Recycling"""
        from .resources.numberrecycling import AsyncNumberrecyclingResourceWithRawResponse

        return AsyncNumberrecyclingResourceWithRawResponse(self._client.numberrecycling)

    @cached_property
    def otpvalidation(self) -> otpvalidation.AsyncOtpvalidationResourceWithRawResponse:
        """One Time Password SMS"""
        from .resources.otpvalidation import AsyncOtpvalidationResourceWithRawResponse

        return AsyncOtpvalidationResourceWithRawResponse(self._client.otpvalidation)

    @cached_property
    def callforwardingsignal(self) -> callforwardingsignal.AsyncCallforwardingsignalResourceWithRawResponse:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import AsyncCallforwardingsignalResourceWithRawResponse

        return AsyncCallforwardingsignalResourceWithRawResponse(self._client.callforwardingsignal)

    @cached_property
    def devicelocation(self) -> devicelocation.AsyncDevicelocationResourceWithRawResponse:
        from .resources.devicelocation import AsyncDevicelocationResourceWithRawResponse

        return AsyncDevicelocationResourceWithRawResponse(self._client.devicelocation)

    @cached_property
    def populationdensitydata(self) -> populationdensitydata.AsyncPopulationdensitydataResourceWithRawResponse:
        """Population Density Data"""
        from .resources.populationdensitydata import AsyncPopulationdensitydataResourceWithRawResponse

        return AsyncPopulationdensitydataResourceWithRawResponse(self._client.populationdensitydata)

    @cached_property
    def regiondevicecount(self) -> regiondevicecount.AsyncRegiondevicecountResourceWithRawResponse:
        """Region Device Count"""
        from .resources.regiondevicecount import AsyncRegiondevicecountResourceWithRawResponse

        return AsyncRegiondevicecountResourceWithRawResponse(self._client.regiondevicecount)

    @cached_property
    def webrtc(self) -> webrtc.AsyncWebrtcResourceWithRawResponse:
        from .resources.webrtc import AsyncWebrtcResourceWithRawResponse

        return AsyncWebrtcResourceWithRawResponse(self._client.webrtc)

    @cached_property
    def connectivityinsights(self) -> connectivityinsights.AsyncConnectivityinsightsResourceWithRawResponse:
        from .resources.connectivityinsights import AsyncConnectivityinsightsResourceWithRawResponse

        return AsyncConnectivityinsightsResourceWithRawResponse(self._client.connectivityinsights)

    @cached_property
    def qualityondemand(self) -> qualityondemand.AsyncQualityondemandResourceWithRawResponse:
        """QoS Profiles"""
        from .resources.qualityondemand import AsyncQualityondemandResourceWithRawResponse

        return AsyncQualityondemandResourceWithRawResponse(self._client.qualityondemand)

    @cached_property
    def deviceidentifier(self) -> deviceidentifier.AsyncDeviceidentifierResourceWithRawResponse:
        """Device Identifier"""
        from .resources.deviceidentifier import AsyncDeviceidentifierResourceWithRawResponse

        return AsyncDeviceidentifierResourceWithRawResponse(self._client.deviceidentifier)

    @cached_property
    def simswap(self) -> simswap.AsyncSimswapResourceWithRawResponse:
        from .resources.simswap import AsyncSimswapResourceWithRawResponse

        return AsyncSimswapResourceWithRawResponse(self._client.simswap)

    @cached_property
    def deviceroamingstatus(self) -> deviceroamingstatus.AsyncDeviceroamingstatusResourceWithRawResponse:
        from .resources.deviceroamingstatus import AsyncDeviceroamingstatusResourceWithRawResponse

        return AsyncDeviceroamingstatusResourceWithRawResponse(self._client.deviceroamingstatus)

    @cached_property
    def devicereachabilitystatus(self) -> devicereachabilitystatus.AsyncDevicereachabilitystatusResourceWithRawResponse:
        from .resources.devicereachabilitystatus import AsyncDevicereachabilitystatusResourceWithRawResponse

        return AsyncDevicereachabilitystatusResourceWithRawResponse(self._client.devicereachabilitystatus)

    @cached_property
    def connectednetworktype(self) -> connectednetworktype.AsyncConnectednetworktypeResourceWithRawResponse:
        from .resources.connectednetworktype import AsyncConnectednetworktypeResourceWithRawResponse

        return AsyncConnectednetworktypeResourceWithRawResponse(self._client.connectednetworktype)


class CamaraWithStreamedResponse:
    _client: Camara

    def __init__(self, client: Camara) -> None:
        self._client = client

    @cached_property
    def customerinsights(self) -> customerinsights.CustomerinsightsResourceWithStreamingResponse:
        from .resources.customerinsights import CustomerinsightsResourceWithStreamingResponse

        return CustomerinsightsResourceWithStreamingResponse(self._client.customerinsights)

    @cached_property
    def deviceswap(self) -> deviceswap.DeviceswapResourceWithStreamingResponse:
        """Device Swap"""
        from .resources.deviceswap import DeviceswapResourceWithStreamingResponse

        return DeviceswapResourceWithStreamingResponse(self._client.deviceswap)

    @cached_property
    def knowyourcustomerageverification(
        self,
    ) -> knowyourcustomerageverification.KnowyourcustomerageverificationResourceWithStreamingResponse:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import (
            KnowyourcustomerageverificationResourceWithStreamingResponse,
        )

        return KnowyourcustomerageverificationResourceWithStreamingResponse(
            self._client.knowyourcustomerageverification
        )

    @cached_property
    def knowyourcustomerfill_in(self) -> knowyourcustomerfill_in.KnowyourcustomerfillInResourceWithStreamingResponse:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import KnowyourcustomerfillInResourceWithStreamingResponse

        return KnowyourcustomerfillInResourceWithStreamingResponse(self._client.knowyourcustomerfill_in)

    @cached_property
    def knowyourcustomermatch(self) -> knowyourcustomermatch.KnowyourcustomermatchResourceWithStreamingResponse:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import KnowyourcustomermatchResourceWithStreamingResponse

        return KnowyourcustomermatchResourceWithStreamingResponse(self._client.knowyourcustomermatch)

    @cached_property
    def tenure(self) -> tenure.TenureResourceWithStreamingResponse:
        """KYC Tenure"""
        from .resources.tenure import TenureResourceWithStreamingResponse

        return TenureResourceWithStreamingResponse(self._client.tenure)

    @cached_property
    def numberrecycling(self) -> numberrecycling.NumberrecyclingResourceWithStreamingResponse:
        """Number Recycling"""
        from .resources.numberrecycling import NumberrecyclingResourceWithStreamingResponse

        return NumberrecyclingResourceWithStreamingResponse(self._client.numberrecycling)

    @cached_property
    def otpvalidation(self) -> otpvalidation.OtpvalidationResourceWithStreamingResponse:
        """One Time Password SMS"""
        from .resources.otpvalidation import OtpvalidationResourceWithStreamingResponse

        return OtpvalidationResourceWithStreamingResponse(self._client.otpvalidation)

    @cached_property
    def callforwardingsignal(self) -> callforwardingsignal.CallforwardingsignalResourceWithStreamingResponse:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import CallforwardingsignalResourceWithStreamingResponse

        return CallforwardingsignalResourceWithStreamingResponse(self._client.callforwardingsignal)

    @cached_property
    def devicelocation(self) -> devicelocation.DevicelocationResourceWithStreamingResponse:
        from .resources.devicelocation import DevicelocationResourceWithStreamingResponse

        return DevicelocationResourceWithStreamingResponse(self._client.devicelocation)

    @cached_property
    def populationdensitydata(self) -> populationdensitydata.PopulationdensitydataResourceWithStreamingResponse:
        """Population Density Data"""
        from .resources.populationdensitydata import PopulationdensitydataResourceWithStreamingResponse

        return PopulationdensitydataResourceWithStreamingResponse(self._client.populationdensitydata)

    @cached_property
    def regiondevicecount(self) -> regiondevicecount.RegiondevicecountResourceWithStreamingResponse:
        """Region Device Count"""
        from .resources.regiondevicecount import RegiondevicecountResourceWithStreamingResponse

        return RegiondevicecountResourceWithStreamingResponse(self._client.regiondevicecount)

    @cached_property
    def webrtc(self) -> webrtc.WebrtcResourceWithStreamingResponse:
        from .resources.webrtc import WebrtcResourceWithStreamingResponse

        return WebrtcResourceWithStreamingResponse(self._client.webrtc)

    @cached_property
    def connectivityinsights(self) -> connectivityinsights.ConnectivityinsightsResourceWithStreamingResponse:
        from .resources.connectivityinsights import ConnectivityinsightsResourceWithStreamingResponse

        return ConnectivityinsightsResourceWithStreamingResponse(self._client.connectivityinsights)

    @cached_property
    def qualityondemand(self) -> qualityondemand.QualityondemandResourceWithStreamingResponse:
        """QoS Profiles"""
        from .resources.qualityondemand import QualityondemandResourceWithStreamingResponse

        return QualityondemandResourceWithStreamingResponse(self._client.qualityondemand)

    @cached_property
    def deviceidentifier(self) -> deviceidentifier.DeviceidentifierResourceWithStreamingResponse:
        """Device Identifier"""
        from .resources.deviceidentifier import DeviceidentifierResourceWithStreamingResponse

        return DeviceidentifierResourceWithStreamingResponse(self._client.deviceidentifier)

    @cached_property
    def simswap(self) -> simswap.SimswapResourceWithStreamingResponse:
        from .resources.simswap import SimswapResourceWithStreamingResponse

        return SimswapResourceWithStreamingResponse(self._client.simswap)

    @cached_property
    def deviceroamingstatus(self) -> deviceroamingstatus.DeviceroamingstatusResourceWithStreamingResponse:
        from .resources.deviceroamingstatus import DeviceroamingstatusResourceWithStreamingResponse

        return DeviceroamingstatusResourceWithStreamingResponse(self._client.deviceroamingstatus)

    @cached_property
    def devicereachabilitystatus(
        self,
    ) -> devicereachabilitystatus.DevicereachabilitystatusResourceWithStreamingResponse:
        from .resources.devicereachabilitystatus import DevicereachabilitystatusResourceWithStreamingResponse

        return DevicereachabilitystatusResourceWithStreamingResponse(self._client.devicereachabilitystatus)

    @cached_property
    def connectednetworktype(self) -> connectednetworktype.ConnectednetworktypeResourceWithStreamingResponse:
        from .resources.connectednetworktype import ConnectednetworktypeResourceWithStreamingResponse

        return ConnectednetworktypeResourceWithStreamingResponse(self._client.connectednetworktype)


class AsyncCamaraWithStreamedResponse:
    _client: AsyncCamara

    def __init__(self, client: AsyncCamara) -> None:
        self._client = client

    @cached_property
    def customerinsights(self) -> customerinsights.AsyncCustomerinsightsResourceWithStreamingResponse:
        from .resources.customerinsights import AsyncCustomerinsightsResourceWithStreamingResponse

        return AsyncCustomerinsightsResourceWithStreamingResponse(self._client.customerinsights)

    @cached_property
    def deviceswap(self) -> deviceswap.AsyncDeviceswapResourceWithStreamingResponse:
        """Device Swap"""
        from .resources.deviceswap import AsyncDeviceswapResourceWithStreamingResponse

        return AsyncDeviceswapResourceWithStreamingResponse(self._client.deviceswap)

    @cached_property
    def knowyourcustomerageverification(
        self,
    ) -> knowyourcustomerageverification.AsyncKnowyourcustomerageverificationResourceWithStreamingResponse:
        """Know Your Customer Age Verification"""
        from .resources.knowyourcustomerageverification import (
            AsyncKnowyourcustomerageverificationResourceWithStreamingResponse,
        )

        return AsyncKnowyourcustomerageverificationResourceWithStreamingResponse(
            self._client.knowyourcustomerageverification
        )

    @cached_property
    def knowyourcustomerfill_in(
        self,
    ) -> knowyourcustomerfill_in.AsyncKnowyourcustomerfillInResourceWithStreamingResponse:
        """Know Your Customer Fill-in"""
        from .resources.knowyourcustomerfill_in import AsyncKnowyourcustomerfillInResourceWithStreamingResponse

        return AsyncKnowyourcustomerfillInResourceWithStreamingResponse(self._client.knowyourcustomerfill_in)

    @cached_property
    def knowyourcustomermatch(self) -> knowyourcustomermatch.AsyncKnowyourcustomermatchResourceWithStreamingResponse:
        """Know Your Customer Match"""
        from .resources.knowyourcustomermatch import AsyncKnowyourcustomermatchResourceWithStreamingResponse

        return AsyncKnowyourcustomermatchResourceWithStreamingResponse(self._client.knowyourcustomermatch)

    @cached_property
    def tenure(self) -> tenure.AsyncTenureResourceWithStreamingResponse:
        """KYC Tenure"""
        from .resources.tenure import AsyncTenureResourceWithStreamingResponse

        return AsyncTenureResourceWithStreamingResponse(self._client.tenure)

    @cached_property
    def numberrecycling(self) -> numberrecycling.AsyncNumberrecyclingResourceWithStreamingResponse:
        """Number Recycling"""
        from .resources.numberrecycling import AsyncNumberrecyclingResourceWithStreamingResponse

        return AsyncNumberrecyclingResourceWithStreamingResponse(self._client.numberrecycling)

    @cached_property
    def otpvalidation(self) -> otpvalidation.AsyncOtpvalidationResourceWithStreamingResponse:
        """One Time Password SMS"""
        from .resources.otpvalidation import AsyncOtpvalidationResourceWithStreamingResponse

        return AsyncOtpvalidationResourceWithStreamingResponse(self._client.otpvalidation)

    @cached_property
    def callforwardingsignal(self) -> callforwardingsignal.AsyncCallforwardingsignalResourceWithStreamingResponse:
        """Call Forwarding Signal"""
        from .resources.callforwardingsignal import AsyncCallforwardingsignalResourceWithStreamingResponse

        return AsyncCallforwardingsignalResourceWithStreamingResponse(self._client.callforwardingsignal)

    @cached_property
    def devicelocation(self) -> devicelocation.AsyncDevicelocationResourceWithStreamingResponse:
        from .resources.devicelocation import AsyncDevicelocationResourceWithStreamingResponse

        return AsyncDevicelocationResourceWithStreamingResponse(self._client.devicelocation)

    @cached_property
    def populationdensitydata(self) -> populationdensitydata.AsyncPopulationdensitydataResourceWithStreamingResponse:
        """Population Density Data"""
        from .resources.populationdensitydata import AsyncPopulationdensitydataResourceWithStreamingResponse

        return AsyncPopulationdensitydataResourceWithStreamingResponse(self._client.populationdensitydata)

    @cached_property
    def regiondevicecount(self) -> regiondevicecount.AsyncRegiondevicecountResourceWithStreamingResponse:
        """Region Device Count"""
        from .resources.regiondevicecount import AsyncRegiondevicecountResourceWithStreamingResponse

        return AsyncRegiondevicecountResourceWithStreamingResponse(self._client.regiondevicecount)

    @cached_property
    def webrtc(self) -> webrtc.AsyncWebrtcResourceWithStreamingResponse:
        from .resources.webrtc import AsyncWebrtcResourceWithStreamingResponse

        return AsyncWebrtcResourceWithStreamingResponse(self._client.webrtc)

    @cached_property
    def connectivityinsights(self) -> connectivityinsights.AsyncConnectivityinsightsResourceWithStreamingResponse:
        from .resources.connectivityinsights import AsyncConnectivityinsightsResourceWithStreamingResponse

        return AsyncConnectivityinsightsResourceWithStreamingResponse(self._client.connectivityinsights)

    @cached_property
    def qualityondemand(self) -> qualityondemand.AsyncQualityondemandResourceWithStreamingResponse:
        """QoS Profiles"""
        from .resources.qualityondemand import AsyncQualityondemandResourceWithStreamingResponse

        return AsyncQualityondemandResourceWithStreamingResponse(self._client.qualityondemand)

    @cached_property
    def deviceidentifier(self) -> deviceidentifier.AsyncDeviceidentifierResourceWithStreamingResponse:
        """Device Identifier"""
        from .resources.deviceidentifier import AsyncDeviceidentifierResourceWithStreamingResponse

        return AsyncDeviceidentifierResourceWithStreamingResponse(self._client.deviceidentifier)

    @cached_property
    def simswap(self) -> simswap.AsyncSimswapResourceWithStreamingResponse:
        from .resources.simswap import AsyncSimswapResourceWithStreamingResponse

        return AsyncSimswapResourceWithStreamingResponse(self._client.simswap)

    @cached_property
    def deviceroamingstatus(self) -> deviceroamingstatus.AsyncDeviceroamingstatusResourceWithStreamingResponse:
        from .resources.deviceroamingstatus import AsyncDeviceroamingstatusResourceWithStreamingResponse

        return AsyncDeviceroamingstatusResourceWithStreamingResponse(self._client.deviceroamingstatus)

    @cached_property
    def devicereachabilitystatus(
        self,
    ) -> devicereachabilitystatus.AsyncDevicereachabilitystatusResourceWithStreamingResponse:
        from .resources.devicereachabilitystatus import AsyncDevicereachabilitystatusResourceWithStreamingResponse

        return AsyncDevicereachabilitystatusResourceWithStreamingResponse(self._client.devicereachabilitystatus)

    @cached_property
    def connectednetworktype(self) -> connectednetworktype.AsyncConnectednetworktypeResourceWithStreamingResponse:
        from .resources.connectednetworktype import AsyncConnectednetworktypeResourceWithStreamingResponse

        return AsyncConnectednetworktypeResourceWithStreamingResponse(self._client.connectednetworktype)


Client = Camara

AsyncClient = AsyncCamara
