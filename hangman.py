import random

def play_hangman():
    words = ["python", "computer", "programming", "developer", "keyboard"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("================================")
    print("       WELCOME TO HANGMAN")
    print("================================")
    print("Guess the word one letter at a time!")
    print("You have", attempts, "incorrect attempts available.")

    while attempts > 0:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Attempts remaining:", attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a single letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    else:
        print("\nGame over! The word was:", secret_word)

    print("\nThanks for playing Hangman!")


if __name__ == "__main__":
    play_hangman()
