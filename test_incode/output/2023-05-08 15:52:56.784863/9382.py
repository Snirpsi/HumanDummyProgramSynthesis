#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that removes a list of words.
    words = words.copy()
    words.pop(0) #remove the first word
    print(words)

