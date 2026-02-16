# ---------- DO NOT EDIT ------------
import random 
random.seed(256)
# ------------------------------------
"""
Author:         Jason Skipper
Date:           2/12/26
Assignment:     Lab 05
Course:         CPSC1051
Lab Section:    002

This code 

"""
def generate_problem(operation: str, difficulty: int) -> int:
    """
    Generates a random math problem (+, -, *, /) based on the given operation and difficulty. The operation is a string that says what operation the problem will be performing.
    The difficulty is from 1-infinity. The more difficult the problem, the bigger the numbers are in the equation.

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        difficulty: The difficulty for the problem from 1-infinity that determines how big the numbers are.
    
    Returns:
        Prints out a random math problem difficulty
    """

    if operation == "multiplication":
        first_num = random.randint(1, (10 ** difficulty))
        second_num = random.randint(1, (10 ** difficulty))
        print(f"{first_num} * {second_num}")
        return first_num * second_num

    if operation == "subtraction":
        first_num = random.randint(1, (10 ** difficulty))
        second_num = random.randint(1, (10 ** difficulty))
        print(f"{first_num} - {second_num}")
        return first_num - second_num

    if operation == "addition":
        first_num = random.randint(1, (10 ** difficulty))
        second_num = random.randint(1, (10 ** difficulty))
        print(f"{first_num} + {second_num}")
        return first_num + second_num

    first_num = random.randint(1, (10 ** difficulty))
    second_num = random.randint(1, (10 ** difficulty))

    first_num = max([first_num, second_num])
    second_num = min([first_num, second_num])

    print(f"{first_num} / {second_num}")
    return first_num // second_num

def get_valid_op() -> str:
    print("Would you like to practice addition, subtraction, multiplication, or division?", end="")
    operation = input().strip()
    print()

    while (operation != "addition" and operation != "subtraction" and operation != "multiplication" and operation != "division"):
        print("Please select either addition, subtraction, multiplication, or division")
        operation = input().strip()

    return operation

def get_positive(prompt: str) -> int:
    print(prompt, end="")
    raw = input().strip()
    print()

    valid = False
    value = 0

    while valid == False:
        all_digits = True

        if raw == "":
            all_digits = False
        else:
            for i in raw:
                if i < "0" or i > "9":
                    all_digits = False

        if all_digits and int(raw) > 0:
            value = int(raw)
            valid = True
        else:
            print("Please enter a number greater than 0!")
            raw = input().strip()

    return value

if __name__ == "__main__":
    print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
    print("You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.")

    difficulty = 1
    total_correct = 0
    total_questions = 0

    playing = True
    while playing:
        operation = get_valid_op()

        num_problems = get_positive(f"How many types of {operation} problems would you like to solve?")

        print(f"Here are your {num_problems} {operation} problems:")

        round_correct = 0
        for _ in range(num_problems):
            answer = generate_problem(operation, difficulty)
            guess = int(input().strip())

            if guess == answer:
                round_correct += 1
                print("Correct! Next problem...")
            else:
                print("(loud incorrect noise) Wrong! Next problem...")

        total_correct += round_correct
        total_questions += num_problems

        if round_correct > (num_problems / 2):
            print(f"Your score was {round_correct}/{num_problems}. We will be increasing the difficulty for next time!")
            difficulty += 1
        else:
            if difficulty == 1:
                print("You are already at the lowest difficulty!")
            else:
                print(f"Your score was {round_correct}/{num_problems}. We will be lowering the difficulty for next time.")
                difficulty -= 1

        print("Continue? (enter 'quit' to exit)", end="")
        cont = input().strip()
        print()

        if cont == "quit":
            playing = False

    print(f"Congrats! Your final score was {total_correct} out of {total_questions}.", end="")
