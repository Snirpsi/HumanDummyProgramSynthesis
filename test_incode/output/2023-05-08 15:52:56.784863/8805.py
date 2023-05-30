#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that converts words.
    #It takes a list of words and returns a list of words.
    words = [word.lower() for word in words]
    print(words)

