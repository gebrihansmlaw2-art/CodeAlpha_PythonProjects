import random

words = ["python", "apple", "intern", "computer", "science"]
word = random.choice(words)

guessed = []
attempts = 6

print("=== HANGMAN GAME ===")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong! Remaining:", attempts)

if attempts == 0:
    print("Game Over! Word was:", word)
