import random

# Lista med 10 fördefinierade ord
words = ["python", "programmering", "dator", "algoritm", "utveckling", "kodning", "debugger", "variabel", "funktion", "loop"]

def display_word(word, guessed_letters):
    #Visar ordet med gissade bokstäver och understreck för ogissade
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = random.choice(words) #Väljer ett slumpmässigt ord från listan
    word_letters = set(word)    # Unika bokstäver i ordet
    guessed_letters = set()     # Gissade bokstäver
    attempts = 20               # Antal max felgissningar

    print(f"Ordet består av {len(word)} bokstäver.")

    while len(word_letters) > 0 and attempts > 0:
        print(f"\nDu har {attempts} försök kvar.")
        print("Gissade bokstäver:", ' '.join(guessed_letters))
        print("Nuvarande ord:", display_word(word, guessed_letters))

        guess = input("Gissa en bokstav: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Du har redan gissat den bokstaven. Försök igen!")
            elif guess in word_letters:
                word_letters.remove(guess)
                guessed_letters.add(guess)
                print("Bra gissning!")
            else:
                attempts -= 1
                guessed_letters.add(guess)
                print("Tyvärr, den bokstaven finns inte i ordet.")
        else:
            print("Ogiltig gissning. Vänligen ange en enskild bokstav.")

    if attempts == 0:
        print(f"\nTyvärr, du har slut på försök. Ordet var {word}.")
    else:
        print(f"\nGrattis! Du gissade rätt ord: {word}")

if __name__ == "__main__":
    print("Välkommen till Hangman!")
    hangman()
