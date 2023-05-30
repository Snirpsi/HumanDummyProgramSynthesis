#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens a list of words.
    wordlist = open("wordlist.txt","r")
    wordlist = wordlist.readlines()
    wordlist.close()
    wordlist = list(set(wordlist))
    wordlist.sort()
    print(wordlist)

