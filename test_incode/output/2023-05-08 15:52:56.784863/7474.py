#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads words into it
    wordlist = open("words.txt","r")
    wordlist = wordlist.read()
    wordlist = wordlist.split()
    wordlist = list(set(wordlist))
    wordlist.sort()
    print(wordlist)

