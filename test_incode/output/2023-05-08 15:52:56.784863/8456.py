#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads its content
    wordfile = open(words.txt)
    words = wordfile.read().splitlines()
    wordfile.close()
    #A function that prints all the words in words
    for word in words:
        print(word)

