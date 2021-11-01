"""NIST VRI Enumeration types.

Generated with 'datamodel-code-generator' from the NIST SP-1500-102 v1 JSON schema.
The types appear in declaration order.

See:

- https://github.com/koxudaxi/datamodel-code-generator
- https://github.com/usnistgov/voterrecordsinterchange/NIST_V0_voter_records_interchange.json
"""

from enum import Enum


class AssertionValue(Enum):

    NO = "no"
    OTHER = "other"
    UNKNOWN = "unknown"
    YES = "yes"


class BallotReceiptMethod(Enum):

    EMAIL = "email"
    EMAIL_OR_ONLINE = "email-or-online"
    FAX = "fax"
    MAIL = "mail"
    ONLINE = "online"


class ContactMethodType(Enum):

    EMAIL = "email"
    OTHER = "other"
    PHONE = "phone"


class IdentifierType(Enum):

    FIPS = "fips"
    LOCAL_LEVEL = "local-level"
    NATIONAL_LEVEL = "national-level"
    OCD_ID = "ocd-id"
    OTHER = "other"
    STATE_LEVEL = "state-level"


class PhoneCapability(Enum):

    FAX = "fax"
    MMS = "mms"
    SMS = "sms"
    VOICE = "voice"


class ReportingUnitType(Enum):

    BALLOT_BATCH = "ballot-batch"
    BALLOT_STYLE_AREA = "ballot-style-area"
    BOROUGH = "borough"
    CITY = "city"
    CITY_COUNCIL = "city-council"
    COMBINED_PRECINCT = "combined-precinct"
    CONGRESSIONAL = "congressional"
    COUNTY = "county"
    COUNTY_COUNCIL = "county-council"
    DROP_BOX = "drop-box"
    JUDICIAL = "judicial"
    MUNICIPALITY = "municipality"
    OTHER = "other"
    POLLING_PLACE = "polling-place"
    PRECINCT = "precinct"
    SCHOOL = "school"
    SPECIAL = "special"
    SPLIT_PRECINCT = "split-precinct"
    STATE = "state"
    STATE_HOUSE = "state-house"
    STATE_SENATE = "state-senate"
    TOWN = "town"
    TOWNSHIP = "township"
    UTILITY = "utility"
    VILLAGE = "village"
    VOTE_CENTER = "vote-center"
    WARD = "ward"
    WATER = "water"


class RequestError(Enum):

    IDENTITY_LOOKUP_FAILED = "identity-lookup-failed"
    INCOMPLETE = "incomplete"
    INELIGIBLE = "ineligible"
    INVALID_FORM = "invalid-form"
    OTHER = "other"


class RequestForm(Enum):

    FPCA = "fpca"
    NVRA = "nvra"
    OTHER = "other"


class RequestMethod(Enum):

    ARMED_FORCES_RECRUITMENT_OFFICE = "armed-forces-recruitment-office"
    MOTOR_VEHICLE_OFFICE = "motor-vehicle-office"
    OTHER = "other"
    OTHER_AGENCY_DESIGNATED_BY_STATE = "other-agency-designated-by-state"
    PUBLIC_ASSISTANCE_OFFICE = "public-assistance-office"
    REGISTRATION_DRIVE_FROM_ADVOCACY_GROUP_OR_POLITICAL_PARTY = (
        "registration-drive-from-advocacy-group-or-political-party"
    )
    STATE_FUNDED_AGENCY_SERVING_PERSONS_WITH_DISABILITIES = (
        "state-funded-agency-serving-persons-with-disabilities"
    )
    UNKNOWN = "unknown"
    VOTER_VIA_ELECTION_REGISTRARS_OFFICE = "voter-via-election-registrars-office"
    VOTER_VIA_EMAIL = "voter-via-email"
    VOTER_VIA_FAX = "voter-via-fax"
    VOTER_VIA_INTERNET = "voter-via-internet"
    VOTER_VIA_MAIL = "voter-via-mail"


class RequestProxyType(Enum):

    ARMED_FORCES_RECRUITMENT_OFFICE = "armed-forces-recruitment-office"
    MOTOR_VEHICLE_OFFICE = "motor-vehicle-office"
    OTHER = "other"
    OTHER_AGENCY_DESIGNATED_BY_STATE = "other-agency-designated-by-state"
    PUBLIC_ASSISTANCE_OFFICE = "public-assistance-office"
    REGISTRATION_DRIVE_FROM_ADVOCACY_GROUP_OR_POLITICAL_PARTY = (
        "registration-drive-from-advocacy-group-or-political-party"
    )
    STATE_FUNDED_AGENCY_SERVING_PERSONS_WITH_DISABILITIES = (
        "state-funded-agency-serving-persons-with-disabilities"
    )


class SignatureSource(Enum):

    DMV = "dmv"
    LOCAL = "local"
    OTHER = "other"
    STATE = "state"
    VOTER = "voter"


class SignatureType(Enum):

    DYNAMIC = "dynamic"
    ELECTRONIC = "electronic"
    OTHER = "other"


class SuccessAction(Enum):

    ADDRESS_UPDATED = "address-updated"
    NAME_UPDATED = "name-updated"
    OTHER = "other"
    REGISTRATION_CANCELLED = "registration-cancelled"
    REGISTRATION_CREATED = "registration-created"
    REGISTRATION_UPDATED = "registration-updated"
    STATUS_UPDATED = "status-updated"


class VoterClassificationType(Enum):

    ACTIVATED_NATIONAL_GUARD = "activated-national-guard"
    ACTIVE_DUTY = "active-duty"
    ACTIVE_DUTY_SPOUSE_OR_DEPENDENT = "active-duty-spouse-or-dependent"
    CITIZEN_ABROAD_INTENT_TO_RETURN = "citizen-abroad-intent-to-return"
    CITIZEN_ABROAD_NEVER_RESIDED = "citizen-abroad-never-resided"
    CITIZEN_ABROAD_RETURN_UNCERTAIN = "citizen-abroad-return-uncertain"
    DECEASED = "deceased"
    DECLARED_INCOMPETENT = "declared-incompetent"
    EIGHTEEN_ON_ELECTION_DAY = "eighteen-on-election-day"
    FELON = "felon"
    OTHER = "other"
    PERMANENTLY_DENIED = "permanently-denied"
    PROTECTED_VOTER = "protected-voter"
    RESTORED_FELON = "restored-felon"
    UNITED_STATES_CITIZEN = "united-states-citizen"


class VoterHelperType(Enum):

    ASSISTANT = "assistant"
    WITNESS = "witness"


class VoterIdType(Enum):

    DRIVERS_LICENSE = "drivers-license"
    LOCAL_VOTER_REGISTRATION_ID = "local-voter-registration-id"
    OTHER = "other"
    SSN = "ssn"
    SSN4 = "ssn4"
    STATE_ID = "state-id"
    STATE_VOTER_REGISTRATION_ID = "state-voter-registration-id"
    UNKNOWN = "unknown"
    UNSPECIFIED_DOCUMENT = "unspecified-document"
    UNSPECIFIED_DOCUMENT_WITH_NAME_AND_ADDRESS = (
        "unspecified-document-with-name-and-address"
    )
    UNSPECIFIED_DOCUMENT_WITH_PHOTO_IDENTIFICATION = (
        "unspecified-document-with-photo-identification"
    )


class VoterRequestType(Enum):

    BALLOT_REQUEST = "ballot-request"
    LOOKUP = "lookup"
    OTHER = "other"
    REGISTRATION = "registration"


class VoterStatus(Enum):

    ACTIVE = "active"
    INACTIVE = "inactive"
    OTHER = "other"

