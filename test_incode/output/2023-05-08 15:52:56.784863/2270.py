#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that returns words.
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            print(word)

