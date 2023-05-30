#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests a list of words.
    #The program will ask the user for a list of words and then print them out in alphabetical order.
    wordlist = input("Enter a words: ")
    wordlist = wordlist.split()
    wordlist.sort()
    for word in wordlist:
        print(word)

