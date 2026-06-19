# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KnowyourcustomerfillInCreateResponse"]


class KnowyourcustomerfillInCreateResponse(BaseModel):
    address: Optional[str] = None
    """Complete address of the customer stored on the Operator's system.

    For some countries, it is built following the usual concatenation of parameters
    in a country, but for other countries, this is not the case. For some countries,
    it can use streetName, streetNumber and/or houseNumberExtension. For example, in
    ESP, streetName+streetNumber; in NLD, it can be streetName+streetNumber or
    streetName+streetNumber+houseNumberExtension.
    """

    birthdate: Optional[date] = None
    """
    Birthdate of the customer, in ISO 8601 calendar date format (YYYY-MM-DD), stored
    on the Operator's system.
    """

    city_of_birth: Optional[str] = FieldInfo(alias="cityOfBirth", default=None)
    """City where the customer was born."""

    country: Optional[str] = None
    """Country of the customer's address stored on the Operator's system.

    Format ISO 3166-1 alpha-2.
    """

    country_of_birth: Optional[str] = FieldInfo(alias="countryOfBirth", default=None)
    """Country where the customer was born. Format ISO 3166-1 alpha-2."""

    email: Optional[str] = None
    """
    Email address of the customer in the RFC specified format (local-part@domain),
    stored on the Operator's system.
    """

    family_name: Optional[str] = FieldInfo(alias="familyName", default=None)
    """
    Last name, family name, or surname of the customer stored on the Operator's
    system.
    """

    family_name_at_birth: Optional[str] = FieldInfo(alias="familyNameAtBirth", default=None)
    """Last/family/sur- name at birth of the customer stored on the Operator's system."""

    gender: Optional[Literal["MALE", "FEMALE", "OTHER"]] = None
    """Gender of the customer stored on the Operator's system (Male/Female/Other)."""

    given_name: Optional[str] = FieldInfo(alias="givenName", default=None)
    """
    First/given name or compound first/given name of the customer on the Operator's
    system.
    """

    house_number_extension: Optional[str] = FieldInfo(alias="houseNumberExtension", default=None)
    """House number extension of the customer stored on the Operator's system.

    Specific identifier of the house needed depending on the property type. For
    example, number of apartment in an apartment building.
    """

    id_document: Optional[str] = FieldInfo(alias="idDocument", default=None)
    """
    Id number associated to the id_document of the customer stored on the Operator's
    system.
    """

    id_document_expiry_date: Optional[date] = FieldInfo(alias="idDocumentExpiryDate", default=None)
    """Expiration date of the identity document (ISO 8601)."""

    id_document_type: Optional[
        Literal[
            "passport",
            "national_id_card",
            "residence_permit",
            "diplomatic_id",
            "driver_licence",
            "social_security_id",
            "other",
        ]
    ] = FieldInfo(alias="idDocumentType", default=None)
    """Type of the official identity document provided."""

    locality: Optional[str] = None
    """Locality of the customer's address, stored on the Operator's system."""

    middle_names: Optional[str] = FieldInfo(alias="middleNames", default=None)
    """Middle name/s of the customer stored on the Operator's system."""

    name: Optional[str] = None
    """Complete name of the customer stored on the Operator's system.

    It is usually composed of first/given name and last/family/sur- name in a
    country. Depending on the country, the order of first/give name and
    last/family/sur- name varies, and middle name could be included. It can use
    givenName, middleNames, familyName and/or familyNameAtBirth. For example, in
    ESP, name+familyName; in NLD, it can be name+middleNames+familyName or
    name+middleNames+familyNameAtBirth, etc.
    """

    name_kana_hankaku: Optional[str] = FieldInfo(alias="nameKanaHankaku", default=None)
    """
    Complete name of the customer in Hankaku-Kana format (reading of name) for
    Japan, stored on the Operator's system.
    """

    name_kana_zenkaku: Optional[str] = FieldInfo(alias="nameKanaZenkaku", default=None)
    """
    Complete name of the customer in Zenkaku-Kana format (reading of name) for
    Japan, stored on the Operator's system.
    """

    nationality: Optional[str] = None
    """ISO 3166-1 alpha-2 code of the customer’s nationality.

    In the case a customer has more than one nationality, it is supposed to be the
    nationality related to the ID document provided in the match request.
    """

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """
    The postal code or Zip code of the customer's address, stored on the Operator's
    system.
    """

    region: Optional[str] = None
    """Region/prefecture of the customer's address, stored on the Operator's system."""

    street_name: Optional[str] = FieldInfo(alias="streetName", default=None)
    """Name of the street of the customer's address on the Operator's system.

    It should not include the type of the street.
    """

    street_number: Optional[str] = FieldInfo(alias="streetNumber", default=None)
    """The street number of the customer's address on the Operator's system.

    Number identifying a specific property on the 'streetName'.
    """
