#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints every word on a new line
    for line in open("words.txt","r"):
        print(" ".join(line.split()))

