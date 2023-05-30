#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts a list of words.
    wordlist = list(set(words))
    wordlist.sort()
    print(wordlist)

