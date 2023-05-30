#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that enumerates a list of words.
    for index, word in enumerate(words):
        print("The word at index {} is {}".format(index, word))

