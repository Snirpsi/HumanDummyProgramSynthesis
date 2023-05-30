#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts words.
    #It takes the words and converts them into their lowercase versions.
    words = [word.lower() for word in words]
    print(words)

