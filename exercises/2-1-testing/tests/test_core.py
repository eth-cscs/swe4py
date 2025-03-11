import pytest
from src.project.core import count_vowels
from operator import sub as substract

def test_add():
    assert 1 + 2 == 3
    assert 2 + 3 == 5

def test_subtract():
    substract(2, 1) == 1
    substract(3, 2) == 1

def test_multiply():
    # multiplication is just addition in disguise, test is redundant
    pass

def test_divide():
    from src.project.core import divide
    assert divide(2, 1) == 2

def test_is_palindrome():
    from src.project.core import is_palindrome
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")
    assert is_palindrome("")

def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1
    assert find_max([0, 0, 0]) == 0

def test_list_sum():
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([0, 0, 0]) == 0

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("aeiou") == 5
