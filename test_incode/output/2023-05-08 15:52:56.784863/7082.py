#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    wordlist = open(words.txt)
    wordlist = wordlist.read().split()
    wordlist.sort()
    print(wordlist)

