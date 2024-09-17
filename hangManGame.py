import random
from wordsList import nigerianStates  # Import the correct list

# Hangman art
hangmanArt = {
    0: ("   ", 
        "   ", 
        "   "),

    1: (" o ", 
        "   ", 
        "   "),

    2: (" o ", 
        " | ", 
        "   "),

    3: (" o ", 
        "/| ", 
        "   "),

    4: (" o   ", 
        "/|\\ ", 
        "     "),

    5: (" o   ", 
        "/|\\ ", 
        "/    "),
        
    6: (" o   ", 
        "/|\\ ", 
        "/ \\ ")
}

def displayMan(wrongGuesses):
    print("************")
    for line in hangmanArt[wrongGuesses]:
        print(line)
    print("************")

def displayHint(hint):
    print(" ".join(hint))

def displayAnswer(answer):
    print("The correct answer was:", " ".join(answer))

def main():
    answer = random.choice(nigerianStates)
    hint = ["_"] * len(answer)
    wrongGuesses = 0
    guessedLetters = set()
    isRunning = True

    while isRunning:
        displayMan(wrongGuesses)
        displayHint(hint)
        guess = input("Enter a letter of states in Nigeria: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessedLetters:
            print(f"{guess} is already guessed.")
            continue

        guessedLetters.add(guess)

        if guess in answer.lower():
            for i in range(len(answer)):
                if answer[i].lower() == guess:
                    hint[i] = answer[i]
        else:
            wrongGuesses += 1

        if "_" not in hint:
            displayMan(wrongGuesses)
            displayAnswer(answer)
            print("You Win!")
            isRunning = False
        elif wrongGuesses >= len(hangmanArt) - 1:
            displayMan(wrongGuesses)
            displayAnswer(answer)
            print("You Lose!")
            isRunning = False 

if __name__ == "__main__":
    main()
