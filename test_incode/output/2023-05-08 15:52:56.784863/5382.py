#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts words.
    words = [word.lower() for word in words]
    print(" ".join(words))

