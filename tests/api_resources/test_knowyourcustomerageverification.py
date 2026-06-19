# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import KnowyourcustomerageverificationVerifyResponse
from camara._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowyourcustomerageverification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Camara) -> None:
        knowyourcustomerageverification = client.knowyourcustomerageverification.verify(
            age_threshold=18,
        )
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params(self, client: Camara) -> None:
        knowyourcustomerageverification = client.knowyourcustomerageverification.verify(
            age_threshold=18,
            birthdate=parse_date("1978-08-22"),
            email="federicaSanchez.Arjona@example.com",
            family_name="Sanchez Arjona",
            family_name_at_birth="YYYY",
            given_name="Federica",
            id_document="66666666q",
            include_content_lock=True,
            include_parental_control=True,
            middle_names="Sanchez",
            name="Federica Sanchez Arjona",
            phone_number="+34629255833",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Camara) -> None:
        response = client.knowyourcustomerageverification.with_raw_response.verify(
            age_threshold=18,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomerageverification = response.parse()
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Camara) -> None:
        with client.knowyourcustomerageverification.with_streaming_response.verify(
            age_threshold=18,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomerageverification = response.parse()
            assert_matches_type(
                KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowyourcustomerageverification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncCamara) -> None:
        knowyourcustomerageverification = await async_client.knowyourcustomerageverification.verify(
            age_threshold=18,
        )
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncCamara) -> None:
        knowyourcustomerageverification = await async_client.knowyourcustomerageverification.verify(
            age_threshold=18,
            birthdate=parse_date("1978-08-22"),
            email="federicaSanchez.Arjona@example.com",
            family_name="Sanchez Arjona",
            family_name_at_birth="YYYY",
            given_name="Federica",
            id_document="66666666q",
            include_content_lock=True,
            include_parental_control=True,
            middle_names="Sanchez",
            name="Federica Sanchez Arjona",
            phone_number="+34629255833",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCamara) -> None:
        response = await async_client.knowyourcustomerageverification.with_raw_response.verify(
            age_threshold=18,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomerageverification = await response.parse()
        assert_matches_type(
            KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCamara) -> None:
        async with async_client.knowyourcustomerageverification.with_streaming_response.verify(
            age_threshold=18,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomerageverification = await response.parse()
            assert_matches_type(
                KnowyourcustomerageverificationVerifyResponse, knowyourcustomerageverification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
