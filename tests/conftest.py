# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import httpx
import pytest
from pytest_asyncio import is_async_test

from camara import Camara, AsyncCamara, DefaultAioHttpClient
from camara._utils import is_dict

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest  # pyright: ignore[reportPrivateImportUsage]

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("camara").setLevel(logging.DEBUG)


# automatically add `pytest.mark.asyncio()` to all of our async tests
# so we don't have to add that boilerplate everywhere
def pytest_collection_modifyitems(items: list[pytest.Function]) -> None:
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)

    # We skip tests that use both the aiohttp client and respx_mock as respx_mock
    # doesn't support custom transports.
    for item in items:
        if "async_client" not in item.fixturenames or "respx_mock" not in item.fixturenames:
            continue

        if not hasattr(item, "callspec"):
            continue

        async_client_param = item.callspec.params.get("async_client")
        if is_dict(async_client_param) and async_client_param.get("http_client") == "aiohttp":
            item.add_marker(pytest.mark.skip(reason="aiohttp client is not compatible with respx_mock"))


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

bearer_token = "My Bearer Token"
customer_insights_token = "My Customer Insights Token"
device_swap_token = "My Device Swap Token"
kyc_age_verification_token = "My KYC Age Verification Token"
kyc_fill_in_token = "My KYC Fill In Token"
kyc_match_token = "My KYC Match Token"
tenure_token = "My Tenure Token"
number_recycling_token = "My Number Recycling Token"
otp_validation_token = "My Otp Validation Token"
call_forwarding_signal_token = "My Call Forwarding Signal Token"
device_location_token = "My Device Location Token"
population_density_data_token = "My Population Density Data Token"
region_device_count_token = "My Region Device Count Token"
web_rtc_token = "My Web Rtc Token"
connectivity_insights_token = "My Connectivity Insights Token"
quality_on_demand_token = "My Quality On Demand Token"
device_identifier_token = "My Device Identifier Token"
sim_swap_token = "My Sim Swap Token"
device_roaming_status_token = "My Device Roaming Status Token"
device_reachability_status_token = "My Device Reachability Status Token"
connected_network_type_token = "My Connected Network Type Token"
device_location_notifications_api_key = "My Device Location Notifications API Key"
notifications_api_key = "My Notifications API Key"
population_density_data_notifications_api_key = "My Population Density Data Notifications API Key"
region_device_count_notifications_api_key = "My Region Device Count Notifications API Key"
connectivity_insights_notifications_api_key = "My Connectivity Insights Notifications API Key"
sim_swap_notifications_api_key = "My Sim Swap Notifications API Key"
device_roaming_status_notifications_api_key = "My Device Roaming Status Notifications API Key"
device_reachability_status_notifications_api_key = "My Device Reachability Status Notifications API Key"
connected_network_type_notifications_api_key = "My Connected Network Type Notifications API Key"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[Camara]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with Camara(
        base_url=base_url,
        bearer_token=bearer_token,
        customer_insights_token=customer_insights_token,
        device_swap_token=device_swap_token,
        kyc_age_verification_token=kyc_age_verification_token,
        kyc_fill_in_token=kyc_fill_in_token,
        kyc_match_token=kyc_match_token,
        tenure_token=tenure_token,
        number_recycling_token=number_recycling_token,
        otp_validation_token=otp_validation_token,
        call_forwarding_signal_token=call_forwarding_signal_token,
        device_location_token=device_location_token,
        population_density_data_token=population_density_data_token,
        region_device_count_token=region_device_count_token,
        web_rtc_token=web_rtc_token,
        connectivity_insights_token=connectivity_insights_token,
        quality_on_demand_token=quality_on_demand_token,
        device_identifier_token=device_identifier_token,
        sim_swap_token=sim_swap_token,
        device_roaming_status_token=device_roaming_status_token,
        device_reachability_status_token=device_reachability_status_token,
        connected_network_type_token=connected_network_type_token,
        device_location_notifications_api_key=device_location_notifications_api_key,
        notifications_api_key=notifications_api_key,
        population_density_data_notifications_api_key=population_density_data_notifications_api_key,
        region_device_count_notifications_api_key=region_device_count_notifications_api_key,
        connectivity_insights_notifications_api_key=connectivity_insights_notifications_api_key,
        sim_swap_notifications_api_key=sim_swap_notifications_api_key,
        device_roaming_status_notifications_api_key=device_roaming_status_notifications_api_key,
        device_reachability_status_notifications_api_key=device_reachability_status_notifications_api_key,
        connected_network_type_notifications_api_key=connected_network_type_notifications_api_key,
        _strict_response_validation=strict,
    ) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncCamara]:
    param = getattr(request, "param", True)

    # defaults
    strict = True
    http_client: None | httpx.AsyncClient = None

    if isinstance(param, bool):
        strict = param
    elif is_dict(param):
        strict = param.get("strict", True)
        assert isinstance(strict, bool)

        http_client_type = param.get("http_client", "httpx")
        if http_client_type == "aiohttp":
            http_client = DefaultAioHttpClient()
    else:
        raise TypeError(f"Unexpected fixture parameter type {type(param)}, expected bool or dict")

    async with AsyncCamara(
        base_url=base_url,
        bearer_token=bearer_token,
        customer_insights_token=customer_insights_token,
        device_swap_token=device_swap_token,
        kyc_age_verification_token=kyc_age_verification_token,
        kyc_fill_in_token=kyc_fill_in_token,
        kyc_match_token=kyc_match_token,
        tenure_token=tenure_token,
        number_recycling_token=number_recycling_token,
        otp_validation_token=otp_validation_token,
        call_forwarding_signal_token=call_forwarding_signal_token,
        device_location_token=device_location_token,
        population_density_data_token=population_density_data_token,
        region_device_count_token=region_device_count_token,
        web_rtc_token=web_rtc_token,
        connectivity_insights_token=connectivity_insights_token,
        quality_on_demand_token=quality_on_demand_token,
        device_identifier_token=device_identifier_token,
        sim_swap_token=sim_swap_token,
        device_roaming_status_token=device_roaming_status_token,
        device_reachability_status_token=device_reachability_status_token,
        connected_network_type_token=connected_network_type_token,
        device_location_notifications_api_key=device_location_notifications_api_key,
        notifications_api_key=notifications_api_key,
        population_density_data_notifications_api_key=population_density_data_notifications_api_key,
        region_device_count_notifications_api_key=region_device_count_notifications_api_key,
        connectivity_insights_notifications_api_key=connectivity_insights_notifications_api_key,
        sim_swap_notifications_api_key=sim_swap_notifications_api_key,
        device_roaming_status_notifications_api_key=device_roaming_status_notifications_api_key,
        device_reachability_status_notifications_api_key=device_reachability_status_notifications_api_key,
        connected_network_type_notifications_api_key=connected_network_type_notifications_api_key,
        _strict_response_validation=strict,
        http_client=http_client,
    ) as client:
        yield client
