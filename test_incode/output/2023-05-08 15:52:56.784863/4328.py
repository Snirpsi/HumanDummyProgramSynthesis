#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it.
    wordlist = open(words.txt,'r')
    words = wordlist.read().split()
    wordlist.close()
    print(words)

