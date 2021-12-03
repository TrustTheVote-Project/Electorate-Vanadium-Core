from vanadium.utils import Cases

import pytest


# --- Test data

CAMEL_CASE_TESTS = [
    ( "",       () ),
    ( "_",      () ),
    ( "a",      () ),
    ( "ab",     () ),
    ( "aB",     () ),
    ( "Ab",     ( "Ab",     ) ),
    ( "AbC",    ( "Ab", "C" ) ),
    ( "A_b",    ( "A_b",    ) ),
    ( "A_C",    ( "A_", "C" ) ),
    ( "_a",     () ),
    ( "_A",     ( "_A",     ) ),
    ( "_aB",    () ),
    ( "_Ab",    ( "_Ab",    ) ),
    ( "_A_C",   ( "_A_", "C" ) ),
]


SNAKE_CASE_TESTS = [
    ( "",       () ),
    # Leading underscores are tokens
    ( "_",      ( "_", ) ),
    ( "__",     ( "__", ) ),
    ( "_a",     ( "_", "a" ) ),
    ( "_ab",    ( "_", "ab" ) ),
    ( "_a_b",   ( "_", "a", "b" ) ),
    ( "_a__b",  ( "_", "a", "b" ) ),
    ( "__a",    ( "__", "a", ) ),
    ( "_a0",    ( "_", "a0" ) ),
    # All other underscores get dropped
    ( "a",      ( "a", ) ),
    ( "ab",     ( "ab", ) ),
    ( "a_b",    ( "a", "b" ) ),
    ( "a__b",   ( "a", "b" ) ),
    ( "0",      () ),
    # ( "0a",     () ),
    # ( "0_a",    () ),
    # ( "_0",     () ),
    # ( "_0a",    () ),
    # ( "_a_0",   ( "_", "a", ) ),
]


CAMEL_TO_SNAKE_TESTS = [
    ( "A",          "a" ),
    ( "Ab",         "ab" ),
    ( "AB",         "a_b" ),
    ( "ABc",        "a_bc" ),
    ( "AbcDefGhi",  "abc_def_ghi" ),
]


SNAKE_TO_CAMEL_TESTS = [
    ( "a",           "A" ),
    ( "ab",          "Ab" ),
    ( "a_b",         "AB" ),
    ( "a_bc",        "ABc" ),
    ( "abc_def_ghi", "AbcDefGhi" ),
]


# --- Test cases

@pytest.mark.parametrize("text,expected", SNAKE_CASE_TESTS)
def test_split_snake_case(text, expected):
    actual = tuple(Cases.split_snake_case(text))
    assert actual == expected


@pytest.mark.parametrize("text,expected", CAMEL_CASE_TESTS)
def test_split_camel_case(text, expected):
    actual = tuple(Cases.split_camel_case(text))
    assert actual == expected


@pytest.mark.parametrize("text,expected", CAMEL_TO_SNAKE_TESTS)
def test_camel_to_snake(text, expected):
    actual = Cases.camel_to_snake(text)
    assert actual == expected


@pytest.mark.parametrize("text,expected", SNAKE_TO_CAMEL_TESTS)
def test_snake_to_camel(text, expected):
    actual = Cases.snake_to_camel(text)
    assert actual == expected
