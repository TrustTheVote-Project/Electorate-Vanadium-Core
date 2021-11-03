# Electorate-Vanadium-Backend
Electorate is the ElectOS (https://electos.org) subsystem for voter records management. Electorate Vanadium Core is the data warehouse for voter records data and related data on a distributed digital ledger. The Vanadium core is a back-end server that provides a web services API for clients of the warehouse.

The API's interface specification is based on the data schema of the data interoperability guideline for Voter Records Interchange (VRI), published by the US National Institute of Standards and Technology (NIST) as NIST 1500-102.

The API provides clients the ability to make voter registration requests and related transaction requests, with data validation and business logic constraints. The actual primary data storage for the the data warehouse is a distributed digital ledger implemented as a separate component. The Backend makes append requests to the Ledger, and has the privileges for the requests to performed by the Ledger.
