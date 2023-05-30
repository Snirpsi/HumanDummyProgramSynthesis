#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests a list of words.
    #The program will ask the user for a list of words and then print them out.
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words == []:
            break
    print(words)

