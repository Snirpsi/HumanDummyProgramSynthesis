#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints all the words in it
    wordfile = open("words.txt","r")
    for line in wordfile:
        print(line)
    wordfile.close()

