#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that returns a list of words.
    wordlist = list(filter(None, words))
    print(wordlist)

