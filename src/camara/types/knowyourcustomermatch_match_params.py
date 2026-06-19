# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KnowyourcustomermatchMatchParams"]


class KnowyourcustomermatchMatchParams(TypedDict, total=False):
    address: str
    """Complete address of the customer.

    For some countries, it is built following the usual concatenation of parameters
    in a country, but for other countries, this is not the case. For some countries,
    it can use streetName, streetNumber and/or houseNumberExtension. For example, in
    ESP, streetName+streetNumber; in NLD, it can be streetName+streetNumber or
    streetName+streetNumber+houseNumberExtension.
    """

    birthdate: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
    (YYYY-MM-DD).
    """

    city_of_birth: Annotated[str, PropertyInfo(alias="cityOfBirth")]
    """City where the customer was born."""

    country: str
    """Country of the customer's address. Format ISO 3166-1 alpha-2"""

    country_of_birth: Annotated[str, PropertyInfo(alias="countryOfBirth")]
    """Country where the customer was born. Format ISO 3166-1 alpha-2."""

    email: str
    """Email address of the customer in the RFC specified format (local-part@domain)."""

    family_name: Annotated[str, PropertyInfo(alias="familyName")]
    """Last name, family name, or surname of the customer."""

    family_name_at_birth: Annotated[str, PropertyInfo(alias="familyNameAtBirth")]
    """Last/family/sur- name at birth of the customer."""

    gender: Literal["MALE", "FEMALE", "OTHER"]
    """Gender of the customer (Male/Female/Other)."""

    given_name: Annotated[str, PropertyInfo(alias="givenName")]
    """First/given name or compound first/given name of the customer."""

    house_number_extension: Annotated[str, PropertyInfo(alias="houseNumberExtension")]
    """Specific identifier of the house needed depending on the property type.

    For example, number of apartment in an apartment building.
    """

    id_document: Annotated[str, PropertyInfo(alias="idDocument")]
    """Id number associated to the official identity document in the country.

    It may contain alphanumeric characters.
    """

    id_document_expiry_date: Annotated[Union[str, date], PropertyInfo(alias="idDocumentExpiryDate", format="iso8601")]
    """Expiration date of the identity document (ISO 8601)."""

    id_document_type: Annotated[
        Literal[
            "passport",
            "national_id_card",
            "residence_permit",
            "diplomatic_id",
            "driver_licence",
            "social_security_id",
            "other",
        ],
        PropertyInfo(alias="idDocumentType"),
    ]
    """Type of the official identity document provided."""

    locality: str
    """Locality of the customer's address"""

    middle_names: Annotated[str, PropertyInfo(alias="middleNames")]
    """Middle name/s of the customer."""

    name: str
    """
    Complete name of the customer, usually composed of first/given name and
    last/family/sur- name in a country. Depending on the country, the order of
    first/give name and last/family/sur- name varies, and middle name could be
    included. It can use givenName, middleNames, familyName and/or
    familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
    name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.
    """

    name_kana_hankaku: Annotated[str, PropertyInfo(alias="nameKanaHankaku")]
    """
    Complete name of the customer in Hankaku-Kana format (reading of name) for
    Japan.
    """

    name_kana_zenkaku: Annotated[str, PropertyInfo(alias="nameKanaZenkaku")]
    """
    Complete name of the customer in Zenkaku-Kana format (reading of name) for
    Japan.
    """

    nationality: str
    """ISO 3166-1 alpha-2 code of the customer’s nationality.

    In the case a customer has more than one nationality, it is supposed to be the
    nationality related to the ID document provided in the match request.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """Zip code or postal code"""

    region: str
    """Region/prefecture of the customer's address"""

    street_name: Annotated[str, PropertyInfo(alias="streetName")]
    """Name of the street of the customer's address.

    It should not include the type of the street.
    """

    street_number: Annotated[str, PropertyInfo(alias="streetNumber")]
    """The street number of the customer's address.

    Number identifying a specific property on the 'streetName'.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
