import re

class Cases:

    """Utilities for case conversion of identifiers.

    These functions are not perfect. They are specifically intended to handle
    common identifiers and some edge cases, not every possible string.

    Tokens are defined by the characters allowed in Python identifiers:

    - Lower case:  [a-z]
    - Upper case:  [A-Z]
    - Digits:      [0-9]
    - Underscores: _

    Python supports full use of Unicode in symbol names, but functions here are
    dead simple and don't handle anything that isn't ASCII.

    A string must start with a set of legal characters. If it does not it has no
    tokens, even if the rest of the string would have matched.

    Leading underscores are treated as a token because they have special meaning
    in Python identifiers.
    """

    @staticmethod
    def split_camel_case(text):
        """Tokenize a string using capitalized words as tokens.
        The text must start with either an underscore or a capital letter.
        """
        match = re.match("^_*[A-Z]", text)
        if match:
            for match in re.finditer("(_*[A-Z][a-z0-9_]*)", text):
                yield match.group(0)


    @staticmethod
    def split_snake_case(text):
        """Tokenize a string using underscores as delimiters."""
        for match in re.finditer("(^_+|[A-Za-z][A-Za-z0-9]*)", text):
            yield match.group(0)


    @staticmethod
    def camel_to_snake(text):
        """Convert text in 'CamelCase' to 'snake_case'."""
        return "_".join(part.lower() for part in Cases.split_camel_case(text))


    @staticmethod
    def snake_to_camel(text):
        """Convert text in 'snake_case' to 'CamelCase'."""
        return "".join(part.capitalize() for part in Cases.split_snake_case(text))
