# Sentences 

"""This program brings some sentences"""

# By Victor dos Santos

import random



def main():
    for _ in range(1):
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
    
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    a = get_determiner(1), get_noun(1), get_verb(1, "past")
    b = get_determiner(1), get_noun(1), get_verb(1, "present")
    c = get_determiner(1), get_noun(1), get_verb(1, "future")
    d = get_determiner(2), get_noun(2), get_verb(2, "past")
    e = get_determiner(2), get_noun(2), get_verb(2, "present")
    f = get_determiner(2), get_noun(2), get_verb(2, "future")

    return f"{word} {noun} {verb}"

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
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

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



if __name__ == "__main__":
    main()