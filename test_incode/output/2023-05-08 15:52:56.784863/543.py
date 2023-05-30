#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests a list of words.
    #The program will then print out a list of the words in alphabetical order.
    wordlist = list(set(words))
    wordlist.sort()
    print(wordlist)

