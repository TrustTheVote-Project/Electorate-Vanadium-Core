"""NIST VRI Enumeration types.

Generated with 'datamodel-code-generator' from the NIST SP-1500-102 v1 JSON schema.
The order is as types appear in the schema modified by their dependencies.

Note: The generator creates a class foreach of the enums declared under '@type'
fields. These are replaced with 'typing.Literal'.

See:

- https://github.com/koxudaxi/datamodel-code-generator
- https://github.com/usnistgov/voterrecordsinterchange/NIST_V0_voter_records_interchange.json
"""

from datetime import date
from enum import Enum
from typing import Literal, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from .enumerations import *


class File(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.File"] = "VRI.File"

    Data: str
    FileName: Optional[str] = None
    MimeType: Optional[str] = None


class Image(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Image"] = "VRI.Image"

    Data: str
    FileName: Optional[str] = None
    MimeType: Optional[str] = None


class LatLng(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.LatLng"] = "VRI.LatLng"

    Latitude: float
    Longitude: float
    Source: Optional[str] = None


class Name(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Name"] = "VRI.Name"

    FirstName: Optional[str] = None
    FullName: Optional[str] = None
    LastName: Optional[str] = None
    MiddleName: Optional[List[str]] = Field(None, min_items=0)
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None


class PhoneContactMethod(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.PhoneContactMethod"] = "VRI.PhoneContactMethod"

    Capability: Optional[List[PhoneCapability]] = Field(None, min_items=0)
    OtherType: Optional[str] = None
    Type: ContactMethodType
    Value: str


class RequestAcknowledgement(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestAcknowledgement"] = "VRI.RequestAcknowledgement"

    TransactionId: Optional[str] = None


class AdditionalInfo(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.AdditionalInfo"] = "VRI.AdditionalInfo"

    FileValue: Optional[Union[File, Image]] = None
    Name: str
    StringValue: Optional[str] = None


class ContactMethod(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ContactMethod"] = "VRI.ContactMethod"

    OtherType: Optional[str] = None
    Type: ContactMethodType
    Value: str


class Error(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Error"] = "VRI.Error"

    Name: RequestError
    OtherError: Optional[str] = None
    Ref: Optional[str] = None


class ExternalIdentifier(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ExternalIdentifier"] = "VRI.ExternalIdentifier"

    OtherType: Optional[str] = None
    Type: IdentifierType
    Value: str


class Party(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Party"] = "VRI.Party"

    Abbreviation: Optional[str] = None
    ExternalIdentifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    Name: str


class RequestRejection(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestRejection"] = "VRI.RequestRejection"

    AdditionalDetails: Optional[List[str]] = Field(None, min_items=0)
    Error: Optional[List[Error]] = Field(None, min_items=0)
    TransactionId: Optional[str] = None


class Signature(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Signature"] = "VRI.Signature"

    Date: Optional[date] = None
    FileValue: Optional[Image] = None
    OtherSource: Optional[str] = None
    OtherType: Optional[str] = None
    Source: Optional[SignatureSource] = None
    Type: Optional[SignatureType] = None


class VoterClassification(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterClassification"] = "VRI.VoterClassification"

    Assertion: AssertionValue
    OtherAssertion: Optional[str] = None
    OtherType: Optional[str] = None
    Type: VoterClassificationType


class VoterId(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterId"] = "VRI.VoterId"

    AttestNoSuchId: Optional[bool] = None
    DateOfIssuance: Optional[date] = None
    FileValue: Optional[Union[File, Image]] = None
    OtherType: Optional[str] = None
    StringValue: Optional[str] = None
    Type: VoterIdType


class BallotStyle(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.BallotStyle"] = "VRI.BallotStyle"

    ExternalIdentifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    ImageUri: Optional[List[AnyUrl]] = Field(None, min_items=0)
    Party: Optional[List[Party]] = Field(None, min_items=0)


class Election(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Election"] = "VRI.Election"

    EndDate: Optional[date] = None
    ExternalIdentifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    Name: Optional[str] = None
    StartDate: date


class Address(BaseModel):

    __root__: Union[
        addr.CommunityAddressType,
        addr.FourNumberAddressRangeType,
        addr.GeneralAddressClassType,
        addr.IntersectionAddressType,
        addr.LandmarkAddressType,
        addr.NumberedThoroughfareAddressType,
        addr.TwoNumberAddressRangeType,
        addr.USPSGeneralDeliveryOfficeType,
        addr.USPSPostalDeliveryBoxType,
        addr.USPSPostalDeliveryRouteType,
        addr.UnnumberedThoroughfareAddressType,
    ]


class ElectionBasedBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ElectionBasedBallotRequest"] = "VRI.ElectionBasedBallotRequest"

    BallotReceiptPreference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    Election: Election
    MailForwardingAddress: Optional[Address] = None


class Location(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Location"] = "VRI.Location"

    Address: Optional[Address] = None
    Directions: Optional[str] = None
    LatLng: Optional[LatLng] = None


class PermanentBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.PermanentBallotRequest"] = "VRI.PermanentBallotRequest"

    BallotReceiptPreference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    MailForwardingAddress: Optional[Address] = None


class ReportingUnit(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ReportingUnit"] = "VRI.ReportingUnit"

    ExternalIdentifier: Optional[List[ExternalIdentifier]] = Field(None, min_items=0)
    IsDistricted: Optional[bool] = None
    Location: Optional[Location] = None
    Name: Optional[str] = None
    OtherType: Optional[str] = None
    Type: ReportingUnitType


class RequestHelper(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestHelper"] = "VRI.RequestHelper"

    Address: Optional[Address] = None
    Name: Optional[Name] = None
    Phone: Optional[PhoneContactMethod] = None
    Signature: Optional[Signature] = None
    Type: VoterHelperType


class RequestProxy(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestProxy"] = "VRI.RequestProxy"

    Address: Optional[Address] = None
    Name: Optional[str] = None
    OriginTransactionId: Optional[str] = None
    OtherType: Optional[str] = None
    Phone: Optional[PhoneContactMethod] = None
    TimeStamp: Optional[date] = None
    Type: RequestProxyType


class TemporalBallotRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.TemporalBallotRequest"] = "VRI.TemporalBallotRequest"

    BallotReceiptPreference: Optional[List[BallotReceiptMethod]] = Field(
        None, min_items=0
    )
    EndDate: date
    MailForwardingAddress: Optional[Address] = None
    StartDate: date


class Voter(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.Voter"] = "VRI.Voter"

    ContactMethod: Optional[List[Union[ContactMethod, PhoneContactMethod]]] = Field(
        None, min_items=0
    )
    DateOfBirth: Optional[date] = None
    Ethnicity: Optional[str] = None
    Gender: Optional[str] = None
    MailingAddress: Optional[Address] = None
    Name: Name
    Party: Optional[Party] = None
    PreviousName: Optional[Name] = None
    PreviousResidenceAddress: Optional[Address] = None
    PreviousSignature: Optional[Signature] = None
    ResidenceAddress: Address
    ResidenceAddressIsMailingAddress: Optional[bool] = None
    Signature: Optional[Signature] = None
    VoterClassification: Optional[List[VoterClassification]] = Field(None, min_items=0)
    VoterId: Optional[List[VoterId]] = Field(None, min_items=0)


class VoterParticipation(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterParticipation"] = "VRI.VoterParticipation"

    BallotStyle: Optional[BallotStyle] = None
    Election: Election
    PollingLocation: Optional[ReportingUnit] = None


class VoterRecordsRequest(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecordsRequest"] = "VRI.VoterRecordsRequest"

    AdditionalInfo: Optional[List[AdditionalInfo]] = Field(None, min_items=0)
    BallotRequest: Optional[
        Union[ElectionBasedBallotRequest, PermanentBallotRequest, TemporalBallotRequest]
    ] = None
    Form: Optional[RequestForm] = None
    GeneratedDate: date
    Issuer: Optional[str] = None
    OtherForm: Optional[str] = None
    OtherRequestMethod: Optional[str] = None
    OtherType: Optional[str] = None
    RequestHelper: Optional[List[RequestHelper]] = Field(None, min_items=0)
    RequestMethod: RequestMethod
    RequestProxy: Optional[RequestProxy] = None
    SelectedLanguage: Optional[str] = None
    Subject: Voter
    TransactionId: Optional[str] = None
    Type: List[VoterRequestType] = Field(..., min_items=1)
    VendorApplicationId: Optional[str] = None


class ElectionAdministration(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.ElectionAdministration"] = "VRI.ElectionAdministration"

    ContactMethod: Optional[List[Union[ContactMethod, PhoneContactMethod]]] = Field(
        None, min_items=0
    )
    Location: Optional[Location] = None
    Name: Optional[str] = None
    Uri: Optional[List[AnyUrl]] = Field(None, min_items=0)


class RequestSuccess(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.RequestSuccess"] = "VRI.RequestSuccess"

    Action: Optional[List[SuccessAction]] = Field(None, min_items=0)
    District: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    EffectiveDate: Optional[date] = None
    ElectionAdministration: Optional[ElectionAdministration] = None
    Locality: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    PollingPlace: Optional[ReportingUnit] = None
    TransactionId: Optional[str] = None


class VoterRecord(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecord"] = "VRI.VoterRecord"

    District: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    ElectionAdministration: Optional[ElectionAdministration] = None
    HavaIdRequired: Optional[bool] = None
    Locality: Optional[List[ReportingUnit]] = Field(None, min_items=0)
    OtherStatus: Optional[str] = None
    PollingLocation: Optional[ReportingUnit] = None
    Voter: Voter
    VoterParticipation: Optional[List[VoterParticipation]] = Field(None, min_items=0)
    VoterStatus: Optional[VoterStatus] = None


class VoterRecordResults(BaseModel):

    class Config:
        extra = Extra.forbid

    _type: Literal["VRI.VoterRecordResults"] = "VRI.VoterRecordResults"

    TransactionId: Optional[str] = None
    VoterRecord: Optional[List[VoterRecord]] = Field(None, min_items=0)
