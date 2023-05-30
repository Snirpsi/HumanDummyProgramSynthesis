#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that adds words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in words:
            print(word + " is a word!")
        else:
            print(word + " is not a word!")

