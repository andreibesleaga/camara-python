# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import TenureVerifyResponse
from camara._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify(self, client: Camara) -> None:
        tenure = client.tenure.verify(
            tenure_date=parse_date("2023-07-03"),
        )
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params(self, client: Camara) -> None:
        tenure = client.tenure.verify(
            tenure_date=parse_date("2023-07-03"),
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Camara) -> None:
        response = client.tenure.with_raw_response.verify(
            tenure_date=parse_date("2023-07-03"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenure = response.parse()
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Camara) -> None:
        with client.tenure.with_streaming_response.verify(
            tenure_date=parse_date("2023-07-03"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenure = response.parse()
            assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTenure:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncCamara) -> None:
        tenure = await async_client.tenure.verify(
            tenure_date=parse_date("2023-07-03"),
        )
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncCamara) -> None:
        tenure = await async_client.tenure.verify(
            tenure_date=parse_date("2023-07-03"),
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncCamara) -> None:
        response = await async_client.tenure.with_raw_response.verify(
            tenure_date=parse_date("2023-07-03"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenure = await response.parse()
        assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncCamara) -> None:
        async with async_client.tenure.with_streaming_response.verify(
            tenure_date=parse_date("2023-07-03"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenure = await response.parse()
            assert_matches_type(TenureVerifyResponse, tenure, path=["response"])

        assert cast(Any, response.is_closed) is True
