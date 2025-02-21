
import random

def math_quiz():
    print("Welcome to the Math Quiz!")
    
    while True:
        difficulty = input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): ")
        if difficulty in ['1', '2', '3']:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
    
    score = 0
    total_questions = 3 

    for _ in range(total_questions):
        if difficulty == '3':
            num1, num2 = random.randint(100, 1000), random.randint(100, 1000)
        elif difficulty == '2':
            num1, num2 = random.randint(10, 100), random.randint(10, 100)
        else:
            num1, num2 = random.randint(1, 10), random.randint(1, 10)

        operator = random.choice(['+', '-', '*', '/'])
        question = f"{num1} {operator} {num2} = ?"
        correct_answer = eval(f"{num1} {operator} {num2}")

        user_answer = float(input(f"{question} "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

    print(f"Your final score is {score}/{total_questions}.")


math_quiz()