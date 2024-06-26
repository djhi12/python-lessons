"""
Problem Statement:

Write a Python program that takes the user's age as input and determines if they are old enough to vote. If the user's age is less than 18, the program should print "You are not old enough to vote." If the user's age is 18 or older, the program should print "You are old enough to vote."

Your task is to:

    Prompt the user to enter their age.
    Convert the input to an integer.
    Use an if statement to check if the age is less than 18.
    If the age is less than 18, print "You are not old enough to vote."
    If the age is 18 or older, print "You are old enough to vote."

"""

age = int(input("\nEnter your age: "))
# print(type(age))

if age < 18:
    print("You are not old enough to vote.\n")
else:
    print("You are old enough to vote.\n")
