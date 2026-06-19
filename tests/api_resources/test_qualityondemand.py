# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import (
    QosProfile,
    QualityondemandRetrieveQosProfilesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQualityondemand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_qos_profile(self, client: Camara) -> None:
        qualityondemand = client.qualityondemand.retrieve_qos_profile(
            name="voice",
        )
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_qos_profile_with_all_params(self, client: Camara) -> None:
        qualityondemand = client.qualityondemand.retrieve_qos_profile(
            name="voice",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_qos_profile(self, client: Camara) -> None:
        response = client.qualityondemand.with_raw_response.retrieve_qos_profile(
            name="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualityondemand = response.parse()
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_qos_profile(self, client: Camara) -> None:
        with client.qualityondemand.with_streaming_response.retrieve_qos_profile(
            name="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualityondemand = response.parse()
            assert_matches_type(QosProfile, qualityondemand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_qos_profile(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.qualityondemand.with_raw_response.retrieve_qos_profile(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_qos_profiles(self, client: Camara) -> None:
        qualityondemand = client.qualityondemand.retrieve_qos_profiles()
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_qos_profiles_with_all_params(self, client: Camara) -> None:
        qualityondemand = client.qualityondemand.retrieve_qos_profiles(
            device={
                "ipv4_address": {
                    "private_address": "203.0.113.0",
                    "public_address": "203.0.113.0",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@domain.com",
                "phone_number": "+123456789",
            },
            name="voice",
            status="ACTIVE",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_qos_profiles(self, client: Camara) -> None:
        response = client.qualityondemand.with_raw_response.retrieve_qos_profiles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualityondemand = response.parse()
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_qos_profiles(self, client: Camara) -> None:
        with client.qualityondemand.with_streaming_response.retrieve_qos_profiles() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualityondemand = response.parse()
            assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQualityondemand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_qos_profile(self, async_client: AsyncCamara) -> None:
        qualityondemand = await async_client.qualityondemand.retrieve_qos_profile(
            name="voice",
        )
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_qos_profile_with_all_params(self, async_client: AsyncCamara) -> None:
        qualityondemand = await async_client.qualityondemand.retrieve_qos_profile(
            name="voice",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_qos_profile(self, async_client: AsyncCamara) -> None:
        response = await async_client.qualityondemand.with_raw_response.retrieve_qos_profile(
            name="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualityondemand = await response.parse()
        assert_matches_type(QosProfile, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_qos_profile(self, async_client: AsyncCamara) -> None:
        async with async_client.qualityondemand.with_streaming_response.retrieve_qos_profile(
            name="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualityondemand = await response.parse()
            assert_matches_type(QosProfile, qualityondemand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_qos_profile(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.qualityondemand.with_raw_response.retrieve_qos_profile(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_qos_profiles(self, async_client: AsyncCamara) -> None:
        qualityondemand = await async_client.qualityondemand.retrieve_qos_profiles()
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_qos_profiles_with_all_params(self, async_client: AsyncCamara) -> None:
        qualityondemand = await async_client.qualityondemand.retrieve_qos_profiles(
            device={
                "ipv4_address": {
                    "private_address": "203.0.113.0",
                    "public_address": "203.0.113.0",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@domain.com",
                "phone_number": "+123456789",
            },
            name="voice",
            status="ACTIVE",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_qos_profiles(self, async_client: AsyncCamara) -> None:
        response = await async_client.qualityondemand.with_raw_response.retrieve_qos_profiles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qualityondemand = await response.parse()
        assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_qos_profiles(self, async_client: AsyncCamara) -> None:
        async with async_client.qualityondemand.with_streaming_response.retrieve_qos_profiles() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qualityondemand = await response.parse()
            assert_matches_type(QualityondemandRetrieveQosProfilesResponse, qualityondemand, path=["response"])

        assert cast(Any, response.is_closed) is True
