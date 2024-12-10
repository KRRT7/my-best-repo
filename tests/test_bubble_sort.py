import pytest
from bubble_sort import decompress_braces


def test_decompress_braces_invalid_input():
    with pytest.raises(IndexError):
        decompress_braces("2{a3{b}")
    with pytest.raises(IndexError):
        decompress_braces("3{a2{b}")
    with pytest.raises(IndexError):
        decompress_braces("2{3{a}2{b")
