# Sentences 

"""This program brings some sentences.
The main point is how to work with functions during this project.

    Now we will have the simple semantic of the code.

1. The computer starts executing the sentences.py program by calling
the main function.
2. While executing the main function, the computer calls the 
make_sentence function.
3. While executing the make_sentence function, the computer calls the
get_determiner, get_noun, get_verb, and get_prepositional_phrase
functions.
4. While executing the get_prepositional_phrase function, the computer
calls the get_preposition, get_determiner, and get_noun functions.
5. While executing each of the get_determiner, get_noun, get_verb, 
and get_preposition functions, the computer calls the random.choice function.
6. Then, the computer executes the str.capitalize method.
7. Finally, the computer executes the print function.
"""

# By Victor dos Santos

import random



def main():
   
    sentence_singular_past = make_sentence(1, "past")
    sentence_singular_present = make_sentence(1, "present")
    sentence_singular_future = make_sentence(1, "future")
    sentence_plural_past = make_sentence(2, "past")
    sentence_plural_present = make_sentence(2, "present")
    sentence_plural_future = make_sentence(2, "future")

    print(sentence_singular_past)
    print(sentence_singular_present)
    print(sentence_singular_future)
    print(sentence_plural_past)
    print(sentence_plural_present)
    print(sentence_plural_future)


def make_sentence(quantity, tense):
    """Return the following functions get_determiner, get_noun,
    get_verb and get_preposition_phrase. This function bring two
    parameters too, quantity and tense. This help in the creation
    of the sentences further.

    Parameter
        Variables: word, noun, verb, preposition_phrase.
            It function takes the previous functions and 
            fill the variables with a right quantity or 
            tense, depending on the parameters that will
            be passed in the main function. 
        Quantity: an integer.
            The quantity will be call here to come back 
            to main function.
        Tense: past, present, future.
            There are need to call this parameter, to 
            call this on the main function later.
    Return: a phrase with all these variables and capitalize word.
    """
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition_phrase = get_preposition_phrase(quantity)

    return f"{word.capitalize()} {noun} {verb} {preposition_phrase}"



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    return determiner


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    """Conditional working to find the kind of the sentences
    if it will be a "past sentence", "presente singular sentence",
    "presente plural sentence" or a "future sentence".
    """
    if tense == "past":
        verbs = random.choice(past_verbs)
        return verbs
    
    elif tense == "present":
        if quantity == 1:
            verbs = random.choice(present_singular_verbs)
            return verbs

        else:
            verbs = random.choice(present_plural_verbs)
            return verbs
        
    elif tense == "future":
        verbs = random.choice(future_verbs)
        return verbs
    
    
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(prepositions)
    return preposition

def get_preposition_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner and a 
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an interger that determines if the
        determiner and noun in the prepositional 
        phrase returned from this function should 
        be single or plural.
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)

    preposition_phrase = f"{preposition} {word} {noun}"
    return preposition_phrase


if __name__ == "__main__":
    main()