"""Verify that the prefix and suffix functions work correctly."""

""" 

    By Victor Dos Santos

    
    This code will work as a compliment from the week3_words.py,
    you can find this inthe folder 2week3_test_function. This code
    will run by after install some dependencies as the following:

    python -m pip install --user --upgrade pip setuptools wheel

    python -m pip install --user pytest

    This will work on windows, to other operational sistem 
    make a deep search.
"""

from week3_words import prefix, suffix
import pytest



def test_prefix():
    """Verify that the prefix function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"


    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


def test_suffix():
    """Verify that the suffix function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the suffix function and verify that.
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("angelic", "awesome") == ""


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])