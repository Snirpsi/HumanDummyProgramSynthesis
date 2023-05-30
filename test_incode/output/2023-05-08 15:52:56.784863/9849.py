#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and reads lines from it
    while True:
        line = input("Enter a word: ")
        if line == "":
            break
        words.append(line)
    print(words)

