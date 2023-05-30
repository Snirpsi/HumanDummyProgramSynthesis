#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores a list of words.
    words = open("words.txt","r").read().split()
    print(words)

