#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores words.
    #It will print them out in alphabetical order.
    #The program will ask the user for an input.
    #If the input is not in the list, it will print out "Sorry, that word is not in the list."
    #If the input is in the list, the program will print out "The word is " + the input.
    #If the input is invalid, the program will print out "Sorry, that word is not in the list."
    #If the input is valid, the program will print out "The word is " + the input.
    word = input("Enter a word: ")
    if word in words:
        print("The word is " + word)
    else:
        print("Sorry, that word is not in the list.")

