#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that stores a list of words.
    #The loop will run until the user enters quit.
    while True:
        word = input("Enter a word: ")
        if word in words:
            print(word)
        else:
            print("That word is not in the list")
            break

