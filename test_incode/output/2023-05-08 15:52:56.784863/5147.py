#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that stores fruits.
    #It will ask the user to input a fruit name.
    #If the user inputs a fruit name that already exists,
    #the program will print an error message and exit.
    #If the user inputs a fruit name that does not exist,
    #the program will print the fruit name and exit.
    #If the user inputs a fruit name that does not match any fruit names,
    #the program will print an error message and exit.
    fruit = input("Enter a fruit name: ")
    if fruit in fruirs:
        print("The fruit already exists.")
    else:
        print("The fruit does not exist.")
        exit()

