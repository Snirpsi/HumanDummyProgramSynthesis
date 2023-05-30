#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests a list of words.
    while True:
        #Get user input
        word = input("Enter a word: ")
        #Check if word is valid
        if word in words:
            #Print word and break loop
            print(word,end=" ")
            break
        else:
            print("That word is not in the list")

