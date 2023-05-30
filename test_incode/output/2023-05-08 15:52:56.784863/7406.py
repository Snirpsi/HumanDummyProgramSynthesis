#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that requests fruits.
    #The function will print out a list of the fruit names and ask the user to input a fruit.
    #If the user inputs a fruit that isn't in the fruirs list, it will print out an error message.
    #If the user inputs a fruit that exists in the fruirs list, it will print out the fruit name.
    fruits = requestFruits()
    if fruits not in fruirs:
        print("Sorry, that fruit isn't in the fruirs list!")
    elif fruits in fruirs:
        print("The fruit is", fruits)
    else:
        print("Sorry, that fruit already exists in the fruirs list!")

