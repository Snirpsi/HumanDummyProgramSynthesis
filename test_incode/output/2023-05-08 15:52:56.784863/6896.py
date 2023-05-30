#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads line by line
    for line in open("words.txt"):
        #The line is split into words and each word is printed
        print(" ".join(line.split()))

