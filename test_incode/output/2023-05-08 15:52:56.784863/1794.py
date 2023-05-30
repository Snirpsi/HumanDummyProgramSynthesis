#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that calculates words.
    words = words + ["!"]
    words = list(set(words))
    print(words)

