#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads its content
    wordfile = open("words.txt","r")
    words = wordfile.read().split()
    wordfile.close()
    print(words)

