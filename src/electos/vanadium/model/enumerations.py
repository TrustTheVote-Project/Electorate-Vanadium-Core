"""NIST VRI Enumeration types.

Generated with 'datamodel-code-generator' from the NIST SP-1500-102 v1 JSON schema.
The types appear in declaration order.

See:

- https://github.com/koxudaxi/datamodel-code-generator
- https://github.com/usnistgov/voterrecordsinterchange/NIST_V0_voter_records_interchange.json
"""

from enum import Enum


class AssertionValue(Enum):

    no = "no"
    other = "other"
    unknown = "unknown"
    yes = "yes"


class BallotReceiptMethod(Enum):

    email = "email"
    email_or_online = "email-or-online"
    fax = "fax"
    mail = "mail"
    online = "online"


class ContactMethodType(Enum):

    email = "email"
    other = "other"
    phone = "phone"


class IdentifierType(Enum):

    fips = "fips"
    local_level = "local-level"
    national_level = "national-level"
    ocd_id = "ocd-id"
    other = "other"
    state_level = "state-level"


class PhoneCapability(Enum):

    fax = "fax"
    mms = "mms"
    sms = "sms"
    voice = "voice"


class ReportingUnitType(Enum):

    ballot_batch = "ballot-batch"
    ballot_style_area = "ballot-style-area"
    borough = "borough"
    city = "city"
    city_council = "city-council"
    combined_precinct = "combined-precinct"
    congressional = "congressional"
    county = "county"
    county_council = "county-council"
    drop_box = "drop-box"
    judicial = "judicial"
    municipality = "municipality"
    other = "other"
    polling_place = "polling-place"
    precinct = "precinct"
    school = "school"
    special = "special"
    split_precinct = "split-precinct"
    state = "state"
    state_house = "state-house"
    state_senate = "state-senate"
    town = "town"
    township = "township"
    utility = "utility"
    village = "village"
    vote_center = "vote-center"
    ward = "ward"
    water = "water"


class RequestError(Enum):

    identity_lookup_failed = "identity-lookup-failed"
    incomplete = "incomplete"
    ineligible = "ineligible"
    invalid_form = "invalid-form"
    other = "other"


class RequestForm(Enum):

    fpca = "fpca"
    nvra = "nvra"
    other = "other"


class RequestMethod(Enum):

    armed_forces_recruitment_office = "armed-forces-recruitment-office"
    motor_vehicle_office = "motor-vehicle-office"
    other = "other"
    other_agency_designated_by_state = "other-agency-designated-by-state"
    public_assistance_office = "public-assistance-office"
    registration_drive_from_advocacy_group_or_political_party = (
        "registration-drive-from-advocacy-group-or-political-party"
    )
    state_funded_agency_serving_persons_with_disabilities = (
        "state-funded-agency-serving-persons-with-disabilities"
    )
    unknown = "unknown"
    voter_via_election_registrars_office = "voter-via-election-registrars-office"
    voter_via_email = "voter-via-email"
    voter_via_fax = "voter-via-fax"
    voter_via_internet = "voter-via-internet"
    voter_via_mail = "voter-via-mail"


class RequestProxyType(Enum):

    armed_forces_recruitment_office = "armed-forces-recruitment-office"
    motor_vehicle_office = "motor-vehicle-office"
    other = "other"
    other_agency_designated_by_state = "other-agency-designated-by-state"
    public_assistance_office = "public-assistance-office"
    registration_drive_from_advocacy_group_or_political_party = (
        "registration-drive-from-advocacy-group-or-political-party"
    )
    state_funded_agency_serving_persons_with_disabilities = (
        "state-funded-agency-serving-persons-with-disabilities"
    )


class SignatureSource(Enum):

    dmv = "dmv"
    local = "local"
    other = "other"
    state = "state"
    voter = "voter"


class SignatureType(Enum):

    dynamic = "dynamic"
    electronic = "electronic"
    other = "other"


class SuccessAction(Enum):

    address_updated = "address-updated"
    name_updated = "name-updated"
    other = "other"
    registration_cancelled = "registration-cancelled"
    registration_created = "registration-created"
    registration_updated = "registration-updated"
    status_updated = "status-updated"


class VoterClassificationType(Enum):

    activated_national_guard = "activated-national-guard"
    active_duty = "active-duty"
    active_duty_spouse_or_dependent = "active-duty-spouse-or-dependent"
    citizen_abroad_intent_to_return = "citizen-abroad-intent-to-return"
    citizen_abroad_never_resided = "citizen-abroad-never-resided"
    citizen_abroad_return_uncertain = "citizen-abroad-return-uncertain"
    deceased = "deceased"
    declared_incompetent = "declared-incompetent"
    eighteen_on_election_day = "eighteen-on-election-day"
    felon = "felon"
    other = "other"
    permanently_denied = "permanently-denied"
    protected_voter = "protected-voter"
    restored_felon = "restored-felon"
    united_states_citizen = "united-states-citizen"


class VoterHelperType(Enum):

    assistant = "assistant"
    witness = "witness"


class VoterIdType(Enum):

    drivers_license = "drivers-license"
    local_voter_registration_id = "local-voter-registration-id"
    other = "other"
    ssn = "ssn"
    ssn4 = "ssn4"
    state_id = "state-id"
    state_voter_registration_id = "state-voter-registration-id"
    unknown = "unknown"
    unspecified_document = "unspecified-document"
    unspecified_document_with_name_and_address = (
        "unspecified-document-with-name-and-address"
    )
    unspecified_document_with_photo_identification = (
        "unspecified-document-with-photo-identification"
    )


class VoterRequestType(Enum):

    ballot_request = "ballot-request"
    lookup = "lookup"
    other = "other"
    registration = "registration"


class VoterStatus(Enum):

    active = "active"
    inactive = "inactive"
    other = "other"

