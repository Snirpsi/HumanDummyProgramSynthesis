#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens a list of words.
    #It then prints out the words in reverse order.
    for word in words:
        print(word[::-1])
    #A program that opens a file and prints out the contents of that file.
    with open('words.txt') as file:
        print(file.read())

