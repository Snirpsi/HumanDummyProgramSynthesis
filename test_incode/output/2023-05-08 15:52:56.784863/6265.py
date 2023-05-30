#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    wordfile = open(words.txt,'r')
    words = wordfile.readlines()
    wordfile.close()
    #A function that prints all the words in the file
    print(words)

