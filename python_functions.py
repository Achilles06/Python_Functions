import random

#1. The Calculator App
#Task 1: Create functions for each arithmetic operation.

def addition(a, b):
    c = a + b 
    return c

def subtraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    if b != 0:
        c = a / b
        return c
    else: 
        print("B cannot be zero.")

#Task 2: Implement user input to receive numbers and an operation choice.
#Task 3: Ensure your program can handle division by zero and other potential errors.

def main(a, b):
    number1 = float(input("What is your first number?"))
    number2 = float(input("What is your second number?"))
    operation = input("What operation do dyou want? Addition, subtraction, multiplication or division?")
    try:

        if operation == "Addition" or "addition" or "+":
            answer = addition(number1, number2)
        elif operation == "Subtraction" or "subtraction" or "-":
            answer = subtraction(number1, number2)
        elif operation == "multiplication" or "Multiplication" or "x" or "*":
            answer == multiplication(number1, number2)
        elif operation == "Division" or "division" or "/":
            division(number1, number2)
        else: 
            print("Improper selection. Please enter correctly.")
    
        return
    except ValueError as e:
        print(f"Error: {e}")

    print("Result:",answer)



#2. The Shopping List Maker
def shopping_list():
    items = []
    print("Enter items to add to the list. Type done when finished.")

    while True:
        item = input("Enter an item: ")
        if item == "done":
            break
        items.apprend(item)
        print(f"Item '{item}' added to the list.")

    return items

def remove_items(items):
    print("Enter items to remove from the list. Type done when finished.")

    while True:
        item = input("Enter an item:")
        if item == 'done':
            break
        if item in items:
            items.remove(item)
            print(f"Item '{item}' removed from the list.")

        else:
            print(f"Item '{item}' not found in the list.")
    return items

def print_list(items):
    if not items:
        print("The list is empty.")
    else:
        print("List of items:")
        for i, item in enumerate(items, start = 1):
            print(f"{i}.{item}")

#3. The Grade Analyzer
#Task 1. Code a function to calculate the average grade.
def calculate_average(grades):
    if not grades:
        print("No grades entered.")
        return None
    return sum(grades) / len(grades)

#Task 2.  Implement a function to find the highest and lowest grade.
def high_and_low_grades(grades):
    if not grades:
        print("No grades entered.")
        return None
    highest = max(grades)
    lowest = min(grades)
    return highest, lowest

#Task 3.Create a feature that categorizes grades into letter grades (A, B, C, etc.)
def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
#4. The Quiz Game
#Task 1. Develop a list of questions and answers.
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote 'The Lone Drow'?", "answer": "R.A. Salvatore"},
    {"question": "The Celtics have how many championships", "answer": "17"}
]

#Task 2. Write a function that quizzes the user and takes their answers.
def quiz_game(questions):
    question = random.choice(questions)
    user_answer = input(f"Question: {question['question']}? ").strip().lower()
    if user_answer == question['answer'].lower():
        print("Correct!")
        return True
    else:
        print(f"Oops! The correct answer is {question['answer']}.")
        return False
    
#Task 3. Score the quiz and give the user feedback on their performance.
num_questions = len(questions)
correct_answers = 0

for a in range(num_questions):
    if quiz_game(questions):
        correct_answers += 1

score = (correct_answers / num_questions) * 100
print("your score:", score:.2%)
if score >= 70:
    print("Good job! You did well.")
else: 
    print("Keep trying.")


#5. The Fitness Tracker
#Task 1. 