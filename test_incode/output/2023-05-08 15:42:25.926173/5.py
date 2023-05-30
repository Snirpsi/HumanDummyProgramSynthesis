#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that prints a list of words.
    while True:
        print(" ".join(words))
        words.append(input("Enter a word: "))

