#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    wordlist = open("words.txt","r")
    wordlist = wordlist.readlines()
    wordlist = list(set(wordlist))
    wordlist.sort()
    wordlist = list(wordlist)
    print(wordlist)

