#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens a list of words.
    wordlist = open("wordlist.txt","r")
    words = wordlist.readlines()
    wordlist.close()
    wordlist = open("wordlist.txt","w")
    for word in words:
        wordlist.write(word)
    wordlist.close()

