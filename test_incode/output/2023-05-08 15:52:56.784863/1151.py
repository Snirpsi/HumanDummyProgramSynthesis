#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads words into an array
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    print(words)

