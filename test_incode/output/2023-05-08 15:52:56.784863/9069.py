#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads each line and prints it
    for line in open("words.txt"):
        print(line)

