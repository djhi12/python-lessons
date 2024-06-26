"""

Problem Statement:

Write a Python program that prompts the user to enter their age. Based on the provided age, the program should determine and print out the eligibility status for obtaining a driver's license.

Your program should follow these guidelines:
    Prompt the user with the message: "Please enter your age: ".
    Convert the user's input to an integer.
    Use conditional statements (if, elif, and else) to check the age entered by the user.
    If the age is 18 or older, print: "Congratulations! You are eligible for a driver's license."
    If the age is between 16 and 17 (inclusive), print: "You are eligible for a learner's permit."
    If the age is below 16, print: "Sorry, you are not eligible for a driver's license yet."
    
"""

# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the user is eligible for a driver's license
if age >= 18:
    print("Congratulations! You are eligible for a driver's license.")
elif age >= 16:
    print("You are eligible for a learner's permit.")
else:
    print("Sorry, you are not eligible for a driver's license yet.")
