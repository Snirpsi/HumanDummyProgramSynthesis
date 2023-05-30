#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts words.
    wordlist = words.copy()
    wordlist.sort()
    wordlist.reverse()
    print(wordlist)

