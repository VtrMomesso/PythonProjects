# Copyrights 2024 - By Victor dos Santos

# Random Number and Random Words With Functions

"""
Write and call functions that demonstrate both
default parameter values and pass by reference.
"""

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"Numbers {numbers}")

    # Call the append_ random_numbers function
    # with one arguments to add one random number
    # to the numbers list.
    append_random_numbers(numbers)
    print(f"Numbers {numbers}")

    # Call the append_ random_numbers function
    # with one arguments to add three random number
    # to the numbers list.
    append_random_numbers(numbers)
    print(f"Numbers {numbers}")
    
    # Create a list to store random words.
    words = []

    # Call the append_random_words function
    # with with one argument to add one random
    # word to the list.
    append_random_words(words)
    print(f"Words: {words}")

    # Call the append_random_words function
    # with with one argument to add one random
    # word to the list.
    append_random_words(words, 5)
    print(f"Words: {words}")


def append_random_numbers(numbers_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    
    Parameters:
        numbers_list: A list of numbers where this function
            will append random numbers.
        quantity: The number of random numbers that this 
            function will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to 
        return anything because this function changes the 
        numbers_list.
    """


def append_random_words():

# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()