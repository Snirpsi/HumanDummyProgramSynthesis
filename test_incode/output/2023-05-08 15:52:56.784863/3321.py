#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores words.
    wordlist = list(set(words))
    wordlist.sort()
    print(wordlist)

