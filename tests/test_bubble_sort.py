from bubble_sort import decompress_braces


def test_empty_string():
    assert decompress_braces("") == ""


def test_no_braces():
    assert decompress_braces("abcxyz") == "abcxyz"


def test_single_digit_expansion():
    assert decompress_braces("2{a}") == "aa"
    assert decompress_braces("3{b}") == "bbb"
    assert decompress_braces("4{xyz}") == "xyzxyzxyzxyz"


def test_nested_braces():
    assert decompress_braces("2{a3{b}}") == "abbbabbb"
    assert decompress_braces("3{ab2{c}}") == "abccabccabcc"
    assert decompress_braces("2{a2{b2{c}}}") == "abccbccabccbcc"


def test_mixed_characters():
    assert decompress_braces("2{ab}3{cd}") == "ababcdcdcd"
    assert decompress_braces("a1{b}2{c}d") == "abccd"


def test_leading_numbers():
    assert (
        decompress_braces("12abc3{d}") == "12abcddd"
    )  # Numbers not in braces are treated as literals


def test_trailing_numbers():
    assert decompress_braces("2{a}3{b}45") == "aabbb45"


def test_mixed_case():
    assert decompress_braces("2{Ab3{Cd}}") == "AbCdCdCdAbCdCdCd"


def test_only_numbers_and_braces():
    assert decompress_braces("2{3{}}") == ""


def test_edge_cases_with_empty_segments():
    assert decompress_braces("2{}") == ""
    assert decompress_braces("2{3{}}") == ""
    assert decompress_braces("2{a3{}}") == "aa"
