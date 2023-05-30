#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that enumerates a list of words.
    wordlist = ["hello","world","!"]
    for index, word in enumerate(wordlist):
        print("The word at index {} is {}".format(index, word))

