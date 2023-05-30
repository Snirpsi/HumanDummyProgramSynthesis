#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that opens a list of words.
    #It then asks the user to input a word.
    #If the word is found in the list, it prints it.
    #If the word is not found in the list, it prints "Not found".
    word = input("Enter a word: ")
    if word in words:
        print(word)
    else:
        print("Not found")

