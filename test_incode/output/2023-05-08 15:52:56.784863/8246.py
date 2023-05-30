#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that enumerates a list of words.
    wordlist = list(words)
    for index, word in enumerate(wordlist):
        print("{} : {}".format(index, word))

