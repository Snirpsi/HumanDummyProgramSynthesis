#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints every word in the file
    with open('words.txt', 'r') as file:
        for line in file:
            print(line)

