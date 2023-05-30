#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints all the words in it.
    wordlist = open("words.txt","r")
    for line in wordlist:
        line = line.strip()
        for word in words:
            if word in line:
                print(word)
    wordlist.close()

