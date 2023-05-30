#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads its content
    file = open(words.txt,'r')
    words = file.read().split()
    print(words)

