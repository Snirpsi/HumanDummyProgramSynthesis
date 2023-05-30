#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that adds a list of words.
    #The program will ask the user for a list of words and then print
    #the words in alphabetical order.
    words = []
    words.append(input("Enter a list of words: "))
    words.sort()
    print(words)

