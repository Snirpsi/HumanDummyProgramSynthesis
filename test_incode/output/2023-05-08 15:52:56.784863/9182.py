#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that calculates a list of words.
    wordlist = list(set(words))
    wordlist.sort()
    print(wordlist)

