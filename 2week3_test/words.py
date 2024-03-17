# Victor dos Santos

# Using functions and learning how to test that

# Copyright 2024, BYU-I. All rights reserved.

def prefix(string1, string2):
    """Return the prefix, if any, that appears in both string1 and
    string2. In other words, return a string of the characters
    that appear at the beginning of both string1 and string2. For 
    example, if string1 is "inconceivable" and string2 is 
    "inconvenient", this function will return "incon".

    Parameters
        string1: a string of text.
        string2: another string of text.
    Return: a string
    """

    # Convert both strings to lower case.
    string1 = string1.lower()
    string2 = string2.lower()

    # Start at the beginning of both strings.
    i = 0

    # Repeat until the computer finds tow
    # character that are not the same.
    limit = min(len(string1), len(string2))
    while i < limit:
        if string1[i] != string2[i]:
            break
        i += 1