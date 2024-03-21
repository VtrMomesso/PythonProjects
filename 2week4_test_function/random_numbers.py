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


def append_random_numbers():

def append_random_words():

# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()