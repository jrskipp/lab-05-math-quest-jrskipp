# ---------- DO NOT EDIT ------------
import random 
random.seed(256)
# ------------------------------------

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
    
    # This will generate a random first and second number for you to use
    first_num = random.randint(1, (10 ** difficulty))
    second_num = random.randint(1, (10 ** difficulty))

    # IF the problem is division, use this code to make the first number the higher one
    first_num = max([first_num, second_num])
    second_num = min([first_num, second_num])

    # eval() returns the solution to your problem.
    int(eval(f"{first_num} {operation} {second_num}"))

    #TODO: Print the operation and return the solution.

# ---------START CODING HERE----------

print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
print('You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.')

print("Would you like to practice addition, subtraction, multiplication, or division?")
print("Please select either addition, subtraction, multiplication, or division")

print(f"How many types of {operation} problems would you like to solve?")
print("Please enter a number greater than 0!")

print(f"Here are your {num_problems} {operation} problems:")
answer = generate_problem(operation, difficulty)

print("Correct! Next problem...")
print("(loud incorrect noise) Wrong! Next problem...")

print(f"Your score was {temp_score}/{num_problems}. We will be increasing the difficulty for next time!")
print(f"Your score was {temp_score}/{num_problems}. We will be lowering the difficulty for next time.")
print("You are already at the lowest difficulty!")

print("Continue? (enter 'quit' to exit)")


print(f"Congrats! Your final score was {final_score} out of {questions}.")







