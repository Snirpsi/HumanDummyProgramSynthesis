#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    wordlist = open("wordlist.txt","r")
    #A function that prints the words in the list.
    print(wordlist.read().split())

