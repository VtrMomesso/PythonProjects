# Word Puzzle Project 

# By Victor Dos Santos

""" This project contain a word puzzle game, witch we can work to find the secred word, we can guess that using the words with same quantities of letters, then this game give some informations if it's right or no. """

# Variable declarations
secred_word = "mosiah"
attempts = 1
chances = 3

# Printing game instructions 
print("Welcome to the word guessing game!")
print(f"You can guess up to {chances} times only!")
print("Your hint is _ _ _ _ _ _ ")

# Begin the Loop of The Game
while chances > 0:
    guess = input("What is your guess? ")

    # The guess must have the same number of letters as the secret word and if it's wrong you loss one chance and make one attempt. If it's ok go to the next part.
    if len(guess) != len(secred_word):
        print("Sorry, the guess must have the same number of letter as the secret word.\n")
        attempts = attempts + 1
        chances = chances - 1
        print(f"You have {chances} chances left. ")

        continue

    # If guess is correct it stops the loop    
    if guess.lower() == secred_word:
        print("Congratulations! You guessed it! ")
        print(f"It took you {attempts} guesses. ")
        answer = input("Do you want to play again? (Yes/no) ")
        if answer.lower() != "yes":
            chances = 0
    
    # Here we have the Hint, where we can see the informations about the guess, if the letter is in the right place, and if we have a wrong letter. This else work on the "For Loop".
    else:
        attempts = attempts + 1
        chances = chances - 1
        #  Hint mechaniscs c 
        hint = ""
        for i in range(len(secred_word)):
            if guess[i] == secred_word[i]:
                hint = hint + " " + guess[i].upper() + " "
            elif guess[i] in secred_word:
                hint = hint + " " + guess[i].lower() + " "
            else:
                hint = hint + "_ "
        
        print(f"Your hint is {hint}. ")
