import pydantic

from vanadium.utils import Cases


class _SchemaModelConfig:

    # Replaces leading '@' character in JSON Schema field names.
    # Note: Ideally this is private (e.g. '_model_'). Consider 'PrivateAttr'?
    _AT_PREFIX = "model__"

    def _field_name_alias(field_name, at_prefix = _AT_PREFIX):
        """Convert fieldnames:

        - Assume snake case for fields, use camel case for serialized JSON.
        - Set the prefix that maps to '@'-prefix schema keys (e.g. '@type').
        """
        if field_name.startswith(at_prefix):
            n = len(at_prefix)
            alias = f"@{field_name[n:]}"
        else:
            alias = Cases.snake_to_camel(field_name)
        return alias

    # Convert field names.
    alias_generator = _field_name_alias

    # Disallow adding fields.
    # Define in JSON Schema using 'additionalProperties' on 'object' elements.
    # All NIST-1500 election schemas set 'additionalProperties' to false.
    extra = pydantic.Extra.forbid


class SchemaModel(pydantic.BaseModel):

    """Common state for all classes that are models for the NIST JSON Schema."""

    Config = _SchemaModelConfig

    # Overrides:
    #
    # - 'dict' and 'json' default to excluding null values.
    # - 'json' defaults to using aliases to be schema-compliant.

    def dict(self, *, exclude_none = True, **opts):
        return super().dict(exclude_none = exclude_none, **opts)


    def json(self, *, by_alias = True, exclude_none = True, **opts):
        return super().json(by_alias = by_alias, exclude_none = exclude_none, **opts)
