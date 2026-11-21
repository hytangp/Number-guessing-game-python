import random, art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_LEVEL_TURNS

    return HARD_LEVEL_TURNS

def make_a_new_guess():
    return int(input("Make a guess: "))

def check_answer(user_guess_number, guessed_number):
    if user_guess_number == guessed_number:
        print(f"You got it! The answer was {user_guess_number}.")
        return True
    elif user_guess_number > guessed_number:
        print("Too high!")
        return False
    else:
        print("Too low!")
        return False

def check_play_again():
    play_again = input("Do you want to play again? Type 'y' or 'n': ")

    if play_again == "y":
        print("\n" * 50)
        game()
    else:
        print("GoodBye!")

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    tries_left = check_difficulty()
    print(f"You have {tries_left} attempts remaining to guess the number.")

    guessed_number = random.randint(1, 100)

    while tries_left > 0:
        user_guess = make_a_new_guess()

        correct_guess = check_answer(user_guess, guessed_number)

        if correct_guess:
            break

        tries_left -= 1
        if tries_left == 0:
            print("Game Over! You lose.")
        else:
            print("Guess again.")
            print(f"You have {tries_left} attempts remaining to guess the number.")

    check_play_again()

game()