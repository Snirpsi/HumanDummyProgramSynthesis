#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that adds words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word not in words:
            print("That word is not in the list")
        else:
            print(word)

