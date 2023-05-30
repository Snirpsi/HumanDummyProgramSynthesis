#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests a list of words.
    while True:
        words = input("Enter a word: ")
        if words:
            print(" ".join(words))
        else:
            print("You entered nothing!")

