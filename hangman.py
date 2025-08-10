import random

# List of words
words = ["python", "hangman", "computer", "programming", "developer"]

# Choose a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

    print(" ".join(guessed))

if "_" not in guessed:
    print("🎉 You win! The word was:", word)
else:
    print("💀 Game over! The word was:", word)
