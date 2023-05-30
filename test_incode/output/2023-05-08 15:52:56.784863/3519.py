#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that requests words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in words:
            print(word)
        else:
            print("That word is not in the list")

