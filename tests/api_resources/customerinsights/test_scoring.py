# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types.customerinsights import ScoringRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Camara) -> None:
        scoring = client.customerinsights.scoring.retrieve()
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Camara) -> None:
        scoring = client.customerinsights.scoring.retrieve(
            id_document="idDocument",
            phone_number="+4960513",
            scoring_type="gaugeMetric",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Camara) -> None:
        response = client.customerinsights.scoring.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = response.parse()
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Camara) -> None:
        with client.customerinsights.scoring.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = response.parse()
            assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScoring:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCamara) -> None:
        scoring = await async_client.customerinsights.scoring.retrieve()
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCamara) -> None:
        scoring = await async_client.customerinsights.scoring.retrieve(
            id_document="idDocument",
            phone_number="+4960513",
            scoring_type="gaugeMetric",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCamara) -> None:
        response = await async_client.customerinsights.scoring.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring = await response.parse()
        assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCamara) -> None:
        async with async_client.customerinsights.scoring.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring = await response.parse()
            assert_matches_type(ScoringRetrieveResponse, scoring, path=["response"])

        assert cast(Any, response.is_closed) is True
