#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    wordlist = open("words.txt","r")
    words = wordlist.read().split()
    #A function that prints all the words in words
    print(words)
    #A function that prints all the words in words that starts with "h"
    print(filter(lambda x: x[0]=="h",words))

