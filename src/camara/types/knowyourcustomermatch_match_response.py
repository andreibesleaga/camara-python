# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .match_result import MatchResult

__all__ = ["KnowyourcustomermatchMatchResponse"]


class KnowyourcustomermatchMatchResponse(BaseModel):
    address_match: Optional[MatchResult] = FieldInfo(alias="addressMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    address_match_score: Optional[int] = FieldInfo(alias="addressMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    birthdate_match: Optional[MatchResult] = FieldInfo(alias="birthdateMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    city_of_birth_match: Optional[MatchResult] = FieldInfo(alias="cityOfBirthMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    city_of_birth_match_score: Optional[int] = FieldInfo(alias="cityOfBirthMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    country_match: Optional[MatchResult] = FieldInfo(alias="countryMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    country_of_birth_match: Optional[MatchResult] = FieldInfo(alias="countryOfBirthMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    email_match: Optional[MatchResult] = FieldInfo(alias="emailMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    email_match_score: Optional[int] = FieldInfo(alias="emailMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    family_name_at_birth_match: Optional[MatchResult] = FieldInfo(alias="familyNameAtBirthMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    family_name_at_birth_match_score: Optional[int] = FieldInfo(alias="familyNameAtBirthMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    family_name_match: Optional[MatchResult] = FieldInfo(alias="familyNameMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    family_name_match_score: Optional[int] = FieldInfo(alias="familyNameMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    gender_match: Optional[MatchResult] = FieldInfo(alias="genderMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    given_name_match: Optional[MatchResult] = FieldInfo(alias="givenNameMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    given_name_match_score: Optional[int] = FieldInfo(alias="givenNameMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    house_number_extension_match: Optional[MatchResult] = FieldInfo(alias="houseNumberExtensionMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    id_document_expiry_date_match: Optional[MatchResult] = FieldInfo(alias="idDocumentExpiryDateMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    id_document_match: Optional[MatchResult] = FieldInfo(alias="idDocumentMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    id_document_type_match: Optional[MatchResult] = FieldInfo(alias="idDocumentTypeMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    locality_match: Optional[MatchResult] = FieldInfo(alias="localityMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    locality_match_score: Optional[int] = FieldInfo(alias="localityMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    middle_names_match: Optional[MatchResult] = FieldInfo(alias="middleNamesMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    middle_names_match_score: Optional[int] = FieldInfo(alias="middleNamesMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    name_kana_hankaku_match: Optional[MatchResult] = FieldInfo(alias="nameKanaHankakuMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    name_kana_hankaku_match_score: Optional[int] = FieldInfo(alias="nameKanaHankakuMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    name_kana_zenkaku_match: Optional[MatchResult] = FieldInfo(alias="nameKanaZenkakuMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    name_kana_zenkaku_match_score: Optional[int] = FieldInfo(alias="nameKanaZenkakuMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    name_match: Optional[MatchResult] = FieldInfo(alias="nameMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    name_match_score: Optional[int] = FieldInfo(alias="nameMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    nationality_match: Optional[MatchResult] = FieldInfo(alias="nationalityMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    postal_code_match: Optional[MatchResult] = FieldInfo(alias="postalCodeMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    region_match: Optional[MatchResult] = FieldInfo(alias="regionMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    region_match_score: Optional[int] = FieldInfo(alias="regionMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    street_name_match: Optional[MatchResult] = FieldInfo(alias="streetNameMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    street_name_match_score: Optional[int] = FieldInfo(alias="streetNameMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """

    street_number_match: Optional[MatchResult] = FieldInfo(alias="streetNumberMatch", default=None)
    """
    true - the attribute provided matches with the one in the Operator systems,
    which is equal to a `match_score` of 100. false - the attribute provided does
    not match with the one in the Operator systems. not_available - the attribute is
    not available to validate.
    """

    street_number_match_score: Optional[int] = FieldInfo(alias="streetNumberMatchScore", default=None)
    """
    Indicates the similarity score assigned to the input value when it does not
    exactly match the value stored in the operator's system. This property shall
    only be returned when the value of the corresponding match field is `false`. A
    perfect match with a score of 100 is indicated by `match` being 'true' and no
    `matchScore` is returned in this case.
    """
