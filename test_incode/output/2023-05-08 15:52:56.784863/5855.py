#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens a list of words.
    #The program will then ask the user for input.
    #If the user enters anything other than "quit", the program will exit.
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            print(word)
            #If the user enters a word that isn't in the list, it will print that word again.
            if word not in words:
                print("That word isn't in the list")

