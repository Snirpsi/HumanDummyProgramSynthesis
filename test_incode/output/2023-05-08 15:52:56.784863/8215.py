#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    #It then prints them out in alphabetical order.
    wordlist = open("words.txt","r").read().split()
    wordlist.sort()
    for word in wordlist:
        print(word)
    #A function that opens a file and reads it.
    #It then prints out the contents of the file.
    file = open("words.txt","r")
    print(file.read())

