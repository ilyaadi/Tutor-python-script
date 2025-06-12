import random
import time

wrong = 0
count = 0

def inputNum():
    while True:
        highNum = input("Enter how high numbers should be used: ")
        if highNum.isnumeric() and int(highNum) > 0:
            return int(highNum)
        print("Please enter a valid number.")

def inputEquation():
    while True:
        typeOfEquations = input("Enter the type of equations to use (add, subtract, multiply, divide): ").strip().lower()
        if typeOfEquations in ["add", "subtract", "multiply", "divide"]:
            return typeOfEquations
        print("Invalid type of equations. Please enter 'add', 'subtract', 'multiply', or 'divide'.")

def inputQuest():
    while True:
        numOfEquations = input("Enter number of questions you would like: ")
        if numOfEquations.isnumeric() and int(numOfEquations) > 0:
            return int(numOfEquations)
        print("Please enter a valid number.")

def randomNum(highNum):
    return random.randint(1, highNum)

def ask_questions(highNum, typeOfEquations, numOfEquations):
    global wrong
    global count
    for i in range(numOfEquations):
        num1 = randomNum(highNum)
        num2 = randomNum(highNum)
        if typeOfEquations == "add":
            correct = num1 + num2
            op = "+"
        elif typeOfEquations == "subtract":
            correct = num1 - num2
            op = "-"
        elif typeOfEquations == "multiply":
            correct = num1 * num2
            op = "*"
        elif typeOfEquations == "divide":
            num2 = random.randint(1, highNum)
            num1 = num2 * random.randint(1, highNum)
            correct = num1 // num2
            op = "/"
        else:
            continue

        while True:
            try:
                ans = int(input(f"{num1} {op} {num2} = "))
                if ans == correct:
                    count += 1
                    print("Correct!")
                    break
                else:
                    print("Try again.")
                    wrong += 1
                    count += 1
            except ValueError:
                print("Please enter a valid integer.")

def main():
    highNum = inputNum()
    typeOfEquations = inputEquation()
    numOfEquations = inputQuest()
    start_time = time.time()
    ask_questions(highNum, typeOfEquations, numOfEquations)
    end_time = time.time()
    print(f"You got {count - wrong} out of {count} correct.")
    print(f"Which is {((count - wrong) / count) * 100:.2f}% correct.")
    print(f"You took {end_time - start_time} seconds.")
    repeat()

def repeat():
    global rep
    while True:
        rep = input("Do you wanna continue, choose 'yes' or 'no': ")
        if rep in ["yes", "no"]:
            break
        else:
            print("Invalid input, please enter 'yes' or 'no': ")
    if rep == "yes":
        main() 
    else:
        print("Bye")

main()

