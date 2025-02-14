import random

# List of 10 pre defined word
words = ["python", "programmering", "dator", "algoritm", "utveckling", "kodning", "debugger", "variabel", "funktion", "loop"]

def display_word(word, guessed_letters):
    #Show the word with guessed letters and underscore for remaining letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = random.choice(words) # Choose a random word from the list
    word_letters = set(word)    # Unique ltters in the word
    guessed_letters = set()     # Guessed letters
    attempts = 20               # Max number of allowed failed trials

    print(f"The word has {len(word)} letters.")

    while len(word_letters) > 0 and attempts > 0:
        print(f"\nYou have {attempts} attempts.")
        print("Gussed letters are: ", ' '.join(guessed_letters))
        print("The word is:", display_word(word, guessed_letters))

        guess = input("Please guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter. Please try again!")
            elif guess in word_letters:
                word_letters.remove(guess)
                guessed_letters.add(guess)
                print("Correct!")
            else:
                attempts -= 1
                guessed_letters.add(guess)
                print("Sorry, this letter does not exist in the word.")
        else:
            print("Please enter only one letter from the alphabet.")

    if attempts == 0:
        print(f"\nSorry, the game is over :( The word is {word}.")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

if __name__ == "__main__":
    print("Welocme to Hangman!")
    hangman()
