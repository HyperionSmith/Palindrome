"""
Test Palindrome file. This is to test the regular palindrome file.
The regular palindrome file checks to see if a word or number is a palindrome
"""
import pytest
from palindrome import is_palindrome


def test_called_with_():
    """
    Testing a nothing string.
        Parameters:
                    ""
        Returns:
                ValueError
    """
    with pytest.raises(ValueError):
        assert is_palindrome("")


def test_called_with_a():
    """
    Testing a nothing string.
        Parameters:
                    "a"
        Returns:
                True
    """
    assert is_palindrome("a") is True


def test_called_with_bb():
    """
    Testing a nothing string.
        Parameters:
                    "bb"
        Returns:
                True
    """
    assert is_palindrome("bb") is True


def test_called_with_abc():
    """
    Testing a nothing string.
        Parameters:
                    "abc"
        Returns:
                False
    """
    assert is_palindrome("abc") is False


def test_called_with_laval():
    """
    Testing a nothing string.
        Parameters:
                    "laval"
        Returns:
                True
    Laval near Motreal is actually a very nice place :) Eat at lucille's!
    """
    assert is_palindrome("laval") is True


def test_called_with_toronto():
    """
    Testing a nothing string.
        Parameters:
                    "toronto"
        Returns:
                False
    """
    assert is_palindrome("toronto") is False


def test_called_with_able():
    """
    Testing a nothing string.
        Parameters:
                    "Able_was_I_ere_I_saw_Elba"
        Returns:
                True
    """
    assert is_palindrome("Able was I ere I saw Elba") is True
