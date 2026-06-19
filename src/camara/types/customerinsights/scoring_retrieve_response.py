# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScoringRetrieveResponse"]


class ScoringRetrieveResponse(BaseModel):
    """
    Scoring information based on the individual's profile owned by a Telco Operator.
    """

    scoring_type: Literal["gaugeMetric", "veritasIndex"] = FieldInfo(alias="scoringType")
    """Scoring measurement system.

    Allowed values are:

    - `gaugeMetric`: ranges from index 850 (lowest risk) to index 300 (highest risk)
    - `veritasIndex`: ranges from index 0 (lowest risk) to index 19 (highest risk)
    """

    scoring_value: int = FieldInfo(alias="scoringValue")
    """
    Result of the Scoring analysis expressed in the measure indicated in the
    `scoringType` field.
    """
