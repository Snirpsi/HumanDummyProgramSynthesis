#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints every word in the file
    file = open("words.txt","r")
    for line in file:
        print(line)
    file.close()

