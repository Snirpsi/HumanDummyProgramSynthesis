#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens a list of words.
    wordlist = open("wordlist.txt","r")
    for line in wordlist:
        words = line.split(" ")
    for word in words:
        print(word)

