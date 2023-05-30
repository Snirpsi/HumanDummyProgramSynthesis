#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that calculates a list of words.
    #The program will ask the user to input a word.
    #The program will then print out the words that begin
    #with the word entered.
    word = input("Enter a word: ")
    words = word.split()
    for word in words:
        if word.startswith(word):
            print(word)

