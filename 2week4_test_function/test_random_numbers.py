
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

    # Verify that the numbers list now has one element.
    assert len(numbers_list) == 1

    # Verify that all the elements in the numbers list
    # are floating point numbers.
    for x in numbers_list:
        assert isinstance(x, float)

    # Call the append_random_numbers function to append three numbers.
    append_random_numbers(numbers_list, 3)

    # Verify that the numbers list now has four elements.
    assert len(numbers_list) == 4

    # Verify that all the elements in the numbers list
    # are floating point numbers.
    for x in numbers_list:
        assert isinstance(x, float)


def test_append_random_words():
    """Verify that the append_random_words function works correctly.
    Parameters: none
    Return: nothing
    """
    # Create an empty list named words_list.
    words_list = []

    # Verify that the length of the empty list is zero.
    assert len(words_list) == 0

    # Call the append_random_words function to append one number.
    append_random_words(words_list)

    # Verify that the words_list now has one element.
    assert len(words_list) == 1

    # Verify that all the elements in the words list
    # are strings characteres.
    for word in words_list:
        assert isinstance(word, str)
        assert len(word) >= 1

    # Call the append_random_words function to append three words.
    append_random_words(words_list, 3)
   
    # Verify that the words_list now has four element.
    assert len(words_list) == 4

    # Verify that all the elements in the words list
    # are strings characteres.
    for word in words_list:
        assert isinstance(word, str)
        assert len(word) >= 1


pytest.main(["-v", "--tb=line", "-rN", __file__])