#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests a list of words.
    wordlist = input("Enter a list of words: ")
    words = wordlist.split()
    print(words)

