#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads lines from it
    wordlist = open(words.txt,"r")
    for line in wordlist:
        print(line)
    wordlist.close()

