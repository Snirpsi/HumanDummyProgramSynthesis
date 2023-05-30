#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens words.txt and prints all the words in it
    with open('words.txt','r') as file:
        words = file.read().split()
    for word in words:
        print(word)

