#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts a list of words.
    #The program will ask the user for a list of words and then print out the words in reverse order.
    words = input("Enter a list of words: ")
    words = words.split()
    words.reverse()
    for word in words:
        print(word)
    print("\n")

