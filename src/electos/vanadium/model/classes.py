"""NIST VRI Enumeration types.

Generated with 'datamodel-code-generator' from the NIST SP-1500-102 v1 JSON schema.
The order is as types appear in the schema modified by their dependencies.

Note: The generator creates a class foreach of the enums declared under '@type'
fields. These are replaced with 'typing.Literal'.

See:

- https://github.com/koxudaxi/datamodel-code-generator
- https://github.com/usnistgov/voterrecordsinterchange/NIST_V0_voter_records_interchange.json
"""

from datetime import date as Date
from enum import Enum
from typing import Literal, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from .enumerations import *


class File(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.File"] = "VRI.File"

    data: bytes
    file_name: Optional[str] = None
    mime_type: Optional[str] = None


class Image(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Image"] = "VRI.Image"

    data: bytes
    file_name: Optional[str] = None
    mime_type: Optional[str] = None


class LatLng(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.LatLng"] = "VRI.LatLng"

    latitude: float
    longitude: float
    source: Optional[str] = None


class Name(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Name"] = "VRI.Name"

    first_name: Optional[str] = None
    full_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[List[str]] = Field(None, min_items=0)
    prefix: Optional[str] = None
    suffix: Optional[str] = None


class PhoneContactMethod(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.PhoneContactMethod"] = "VRI.PhoneContactMethod"

    capability: Optional[List[PhoneCapability]] = Field(None, min_items=0)
    other_type: Optional[str] = None
    type: ContactMethodType
    value: str


class RequestAcknowledgement(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestAcknowledgement"] = "VRI.RequestAcknowledgement"

    transaction_id: Optional[str] = None


class AdditionalInfo(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.AdditionalInfo"] = "VRI.AdditionalInfo"

    file_value: Optional[Union[File, Image]] = None
    name: str
    string_value: Optional[str] = None


class ContactMethod(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ContactMethod"] = "VRI.ContactMethod"

    other_type: Optional[str] = None
    type: ContactMethodType
    value: str


class Error(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Error"] = "VRI.Error"

    name: RequestError
    other_error: Optional[str] = None
    ref: Optional[str] = None


class ExternalIdentifier(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ExternalIdentifier"] = "VRI.ExternalIdentifier"

    other_type: Optional[str] = None
    type: IdentifierType
    value: str


class Party(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Party"] = "VRI.Party"

    abbreviation: Optional[str] = None
    external_identifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    name: str


class RequestRejection(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestRejection"] = "VRI.RequestRejection"

    additional_details: Optional[List[str]] = Field(None, min_items=0)
    error: Optional[List[Error]] = Field(None, min_items=0)
    transaction_id: Optional[str] = None


class Signature(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Signature"] = "VRI.Signature"

    date: Optional[Date] = None
    file_value: Optional[Image] = None
    other_source: Optional[str] = None
    other_type: Optional[str] = None
    source: Optional[SignatureSource] = None
    type: Optional[SignatureType] = None


class VoterClassification(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterClassification"] = "VRI.VoterClassification"

    assertion: AssertionValue
    other_assertion: Optional[str] = None
    other_type: Optional[str] = None
    type: VoterClassificationType


class VoterId(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterId"] = "VRI.VoterId"

    attest_no_such_id: Optional[bool] = None
    date_of_issuance: Optional[Date] = None
    file_value: Optional[Union[File, Image]] = None
    other_type: Optional[str] = None
    string_value: Optional[str] = None
    type: VoterIdType


class BallotStyle(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.BallotStyle"] = "VRI.BallotStyle"

    external_identifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    image_uri: Optional[List[AnyUrl]] = Field(None, min_items=0)
    party: Optional[List[Party]] = Field(None, min_items=0)


class Election(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Election"] = "VRI.Election"

    end_date: Optional[Date] = None
    external_identifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    name: Optional[str] = None
    start_date: Date


# class Address(BaseModel):
#
#     __root__: Union[
#         addr.CommunityAddressType,
#         addr.FourNumberAddressRangeType,
#         addr.GeneralAddressClassType,
#         addr.IntersectionAddressType,
#         addr.LandmarkAddressType,
#         addr.NumberedThoroughfareAddressType,
#         addr.TwoNumberAddressRangeType,
#         addr.USPSGeneralDeliveryOfficeType,
#         addr.USPSPostalDeliveryBoxType,
#         addr.USPSPostalDeliveryRouteType,
#         addr.UnnumberedThoroughfareAddressType,
#     ]


class ElectionBasedBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ElectionBasedBallotRequest"] = "VRI.ElectionBasedBallotRequest"

    ballot_receipt_preference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    election: Election
    # mail_forwarding_address: Optional[Address] = None


class Location(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Location"] = "VRI.Location"

    # address: Optional[Address] = None
    directions: Optional[str] = None
    lat_lng: Optional[LatLng] = None


class PermanentBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.PermanentBallotRequest"] = "VRI.PermanentBallotRequest"

    ballot_receipt_preference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    # mail_forwarding_address: Optional[Address] = None


class ReportingUnit(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ReportingUnit"] = "VRI.ReportingUnit"

    external_identifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    is_districted: Optional[bool] = None
    location: Optional[Location] = None
    name: Optional[str] = None
    other_type: Optional[str] = None
    type: ReportingUnitType


class RequestHelper(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestHelper"] = "VRI.RequestHelper"

    # address: Optional[Address] = None
    name: Optional[Name] = None
    phone: Optional[PhoneContactMethod] = None
    signature: Optional[Signature] = None
    type: VoterHelperType


class RequestProxy(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestProxy"] = "VRI.RequestProxy"

    # address: Optional[Address] = None
    name: Optional[str] = None
    origin_transaction_id: Optional[str] = None
    other_type: Optional[str] = None
    phone: Optional[PhoneContactMethod] = None
    time_stamp: Optional[Date] = None
    type: RequestProxyType


class TemporalBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.TemporalBallotRequest"] = "VRI.TemporalBallotRequest"

    ballot_receipt_preference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    end_date: Date
    # mail_forwarding_address: Optional[Address] = None
    start_date: Date


class Voter(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Voter"] = "VRI.Voter"

    contact_method: Optional[List[Union[ContactMethod, PhoneContactMethod]]] = Field(
        None, min_items=0
    )
    date_of_birth: Optional[Date] = None
    ethnicity: Optional[str] = None
    gender: Optional[str] = None
    # mailing_address: Optional[Address] = None
    name: Name
    party: Optional[Party] = None
    previous_name: Optional[Name] = None
    # previous_residence_address: Optional[Address] = None
    previous_signature: Optional[Signature] = None
    # residence_address: Address
    residence_address_is_mailing_address: Optional[bool] = None
    signature: Optional[Signature] = None
    voter_classification: Optional[List[VoterClassification]] = Field(None, min_items=0)
    voter_id: Optional[List[VoterId]] = Field(None, min_items=0)


class VoterParticipation(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterParticipation"] = "VRI.VoterParticipation"

    ballot_style: Optional[BallotStyle] = None
    election: Election
    polling_location: Optional[ReportingUnit] = None


class VoterRecordsRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecordsRequest"] = "VRI.VoterRecordsRequest"

    additional_info: Optional[List[AdditionalInfo]] = Field(None, min_items=0)
    ballot_request: Optional[
        Union[ElectionBasedBallotRequest, PermanentBallotRequest, TemporalBallotRequest]
    ] = None
    form: Optional[RequestForm] = None
    generated_date: Date
    issuer: Optional[str] = None
    other_form: Optional[str] = None
    other_request_method: Optional[str] = None
    other_type: Optional[str] = None
    request_helper: Optional[List[RequestHelper]] = Field(None, min_items=0)
    request_method: RequestMethod
    request_proxy: Optional[RequestProxy] = None
    selected_language: Optional[str] = None
    subject: Voter
    transaction_id: Optional[str] = None
    type: List[VoterRequestType] = Field(..., min_items=1)
    vendor_application_id: Optional[str] = None


class ElectionAdministration(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ElectionAdministration"] = "VRI.ElectionAdministration"

    contact_method: Optional[List[Union[ContactMethod, PhoneContactMethod]]] = Field(
        None, min_items=0
    )
    location: Optional[Location] = None
    name: Optional[str] = None
    uri: Optional[List[AnyUrl]] = Field(None, min_items=0)


class RequestSuccess(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestSuccess"] = "VRI.RequestSuccess"

    action: Optional[List[SuccessAction]] = Field(None, min_items=0)
    district: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    effective_date: Optional[Date] = None
    election_administration: Optional[ElectionAdministration] = None
    locality: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    polling_place: Optional[ReportingUnit] = None
    transaction_id: Optional[str] = None


class VoterRecord(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecord"] = "VRI.VoterRecord"

    district: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    election_administration: Optional[ElectionAdministration] = None
    hava_id_required: Optional[bool] = None
    locality: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    other_status: Optional[str] = None
    polling_location: Optional[ReportingUnit] = None
    voter: Voter
    voter_participation: Optional[List[VoterParticipation]] = Field(None, min_items=0)
    voter_status: Optional[VoterStatus] = None


class VoterRecordResults(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecordResults"] = "VRI.VoterRecordResults"

    transaction_id: Optional[str] = None
    voter_record: Optional[List[VoterRecord]] = Field(None, min_items=0)
