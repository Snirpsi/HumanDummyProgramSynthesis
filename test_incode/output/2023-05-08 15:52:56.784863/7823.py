#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts a list of words.
    #The program will ask the user for a word, and print out the
    #word in the form of a sentence.
    word = input("Enter a word: ")
    sentence = ""
    for word in words:
        sentence = sentence + word + " "
    print(sentence)

