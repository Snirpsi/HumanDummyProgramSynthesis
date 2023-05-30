#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that adds a list of words.
    words = input("Enter a words: ")
    words = words.split()
    words.extend(["!"])
    print(" ".join(words))

