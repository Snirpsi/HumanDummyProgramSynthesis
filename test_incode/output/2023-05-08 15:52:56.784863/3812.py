#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that stores a list of words.
    #The program will keep looping until the user enters quit.
    while True:
        word = input("Enter a word: ")
        if word not in words:
            print("That word is not in the list")
        else:
            print(word)
            break

