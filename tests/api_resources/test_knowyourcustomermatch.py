# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import KnowyourcustomermatchMatchResponse
from camara._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowyourcustomermatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_match(self, client: Camara) -> None:
        knowyourcustomermatch = client.knowyourcustomermatch.match()
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_match_with_all_params(self, client: Camara) -> None:
        knowyourcustomermatch = client.knowyourcustomermatch.match(
            address="Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            birthdate=parse_date("1978-08-22"),
            city_of_birth="Madrid",
            country="JP",
            country_of_birth="ES",
            email="abc@example.com",
            family_name="Sanchez Arjona",
            family_name_at_birth="YYYY",
            gender="OTHER",
            given_name="Federica",
            house_number_extension="VVVV",
            id_document="66666666q",
            id_document_expiry_date=parse_date("2027-07-12"),
            id_document_type="passport",
            locality="ZZZZ",
            middle_names="Sanchez",
            name="Federica Sanchez Arjona",
            name_kana_hankaku="federica",
            name_kana_zenkaku="Ｆｅｄｅｒｉｃａ",
            nationality="ES",
            phone_number="+34629255833",
            postal_code="1028460",
            region="Tokyo",
            street_name="Nicolas Salmeron",
            street_number="4",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_match(self, client: Camara) -> None:
        response = client.knowyourcustomermatch.with_raw_response.match()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomermatch = response.parse()
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_match(self, client: Camara) -> None:
        with client.knowyourcustomermatch.with_streaming_response.match() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomermatch = response.parse()
            assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowyourcustomermatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_match(self, async_client: AsyncCamara) -> None:
        knowyourcustomermatch = await async_client.knowyourcustomermatch.match()
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_match_with_all_params(self, async_client: AsyncCamara) -> None:
        knowyourcustomermatch = await async_client.knowyourcustomermatch.match(
            address="Tokyo-to Chiyoda-ku Iidabashi 3-10-10",
            birthdate=parse_date("1978-08-22"),
            city_of_birth="Madrid",
            country="JP",
            country_of_birth="ES",
            email="abc@example.com",
            family_name="Sanchez Arjona",
            family_name_at_birth="YYYY",
            gender="OTHER",
            given_name="Federica",
            house_number_extension="VVVV",
            id_document="66666666q",
            id_document_expiry_date=parse_date("2027-07-12"),
            id_document_type="passport",
            locality="ZZZZ",
            middle_names="Sanchez",
            name="Federica Sanchez Arjona",
            name_kana_hankaku="federica",
            name_kana_zenkaku="Ｆｅｄｅｒｉｃａ",
            nationality="ES",
            phone_number="+34629255833",
            postal_code="1028460",
            region="Tokyo",
            street_name="Nicolas Salmeron",
            street_number="4",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_match(self, async_client: AsyncCamara) -> None:
        response = await async_client.knowyourcustomermatch.with_raw_response.match()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomermatch = await response.parse()
        assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_match(self, async_client: AsyncCamara) -> None:
        async with async_client.knowyourcustomermatch.with_streaming_response.match() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomermatch = await response.parse()
            assert_matches_type(KnowyourcustomermatchMatchResponse, knowyourcustomermatch, path=["response"])

        assert cast(Any, response.is_closed) is True
