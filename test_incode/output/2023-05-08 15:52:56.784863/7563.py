#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    print(words)

