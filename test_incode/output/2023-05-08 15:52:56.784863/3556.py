#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints out the words in it
    file = open("words.txt","r")
    for line in file:
        print(line)
    file.close()

