# Program to raise an exception and handle it
# This program can be used to take integer input only

try:
    integer = int(input("Enter a number : ")) # If user enters a non-integer value then this line will give ValueError
except:
    print("Please enter a integer number only")
