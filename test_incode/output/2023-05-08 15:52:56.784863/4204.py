#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    file = open(words.txt,"r")
    words = file.read().split()
    file.close()
    print(words)

