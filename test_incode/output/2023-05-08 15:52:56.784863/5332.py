#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.
    #It will ask the user to input a fruit name.
    #It will then print the fruit name and the number of times it appears.
    #If the user enters a fruit name that doesn't exist in the list, it will print a message and ask the user to input a fruit name.
    #If the user enters a fruit name that does exist in the list, it will print the fruit name and the number of times it appears.
    fruit = input("Enter a fruit name: ")
    if fruit not in fruirs:
        print("The fruit " + fruit + " doesn't exist.")
        fruit = input("Enter a fruit name: ")
    if fruit in fruirs:
        print("The fruit " + fruit + " appears " + str(len(fruirs)) + " times.")
    else:
        print("The fruit " + fruit + " doesn't exist.")

