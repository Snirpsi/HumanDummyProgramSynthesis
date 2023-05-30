#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints out the words in it
    wordfile = open("words.txt","r")
    wordlist = wordfile.readlines()
    wordfile.close()
    for word in wordlist:
        print(word)

