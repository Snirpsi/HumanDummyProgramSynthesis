#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and prints every word in the file
    with open(words.txt) as file:
        for line in file:
            print(line)

