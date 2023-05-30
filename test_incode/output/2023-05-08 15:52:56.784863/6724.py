#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that returns a list of words.
    wordlist = list(filter(lambda x: x in words, words))
    print(wordlist)

