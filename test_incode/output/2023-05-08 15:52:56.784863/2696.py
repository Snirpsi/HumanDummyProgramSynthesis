#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == "!":
            break
    print(" ".join(words))

