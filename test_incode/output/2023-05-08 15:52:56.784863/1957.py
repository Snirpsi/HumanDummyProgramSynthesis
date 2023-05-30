#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that stores fruits.
    #It will ask the user to input a fruit name.
    #The program will then print out the fruit name.
    #If the user inputs a fruit that doesn't exist,
    #the program will print out "Sorry, that fruit does not exist."
    #If the user inputs a fruit that already exists,
    #the program will print out "Sorry, that fruit already exists."
    fruit = input("Enter a fruit name: ")
    if fruit not in fruirs:
        print("Sorry, that fruit does not exist.")
    elif fruit in fruirs:
        print("Sorry, that fruit already exists.")
    else:
        print("The fruit is", fruit)

