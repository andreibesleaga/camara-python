# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScoringRetrieveParams"]


class ScoringRetrieveParams(TypedDict, total=False):
    id_document: Annotated[str, PropertyInfo(alias="idDocument")]
    """
    Identification number associated to the official identity document in the
    country. It may contain alphanumeric characters.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    scoring_type: Annotated[Literal["gaugeMetric", "veritasIndex"], PropertyInfo(alias="scoringType")]
    """Scoring type, i.e.: scale.

    API Client may use this field to indicate the Scoring in one of the defined
    scales; if this field is not informed, the API will return the Scoring in the
    scale configured by default in the system.

    Allowed values are:

    - `gaugeMetric`: ranges from index 850 (lowest risk) to index 300 (highest risk)
    - `veritasIndex`: ranges from index 0 (lowest risk) to index 19 (highest risk)
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
