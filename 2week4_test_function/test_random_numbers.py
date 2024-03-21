
# Copyrights 2024  |  By Victor Dos Santos

from random_numbers import append_random_numbers
from random_numbers import append_random_words

import pytest

def test_append_random_numbers():
    """Verify that the append_random_numbers function works correctly.
    Parameters: none
    Return: nothing
    """
    # Create an empty list named numbers_list.
    numbers_list = []

    # Verify that the length of the empty list is zero.
    assert len(numbers_list) == 0

    # Call the append_random_numbers function to append one number.
    append_random_numbers(numbers_list)

def test_append_random_words():


pytest.main(["-v", "--tb=line", "-rN", __file__])