import pydantic


class SchemaModel(pydantic.BaseModel):

    """Common state for all classes that are models for the NIST JSON Schema."""

    class Config:

        extra = pydantic.Extra.forbid
