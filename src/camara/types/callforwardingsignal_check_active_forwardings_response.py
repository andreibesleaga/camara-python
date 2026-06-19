# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

__all__ = ["CallforwardingsignalCheckActiveForwardingsResponse"]

CallforwardingsignalCheckActiveForwardingsResponse: TypeAlias = List[
    Literal["inactive", "unconditional", "conditional_busy", "conditional_not_reachable", "conditional_no_answer"]
]
