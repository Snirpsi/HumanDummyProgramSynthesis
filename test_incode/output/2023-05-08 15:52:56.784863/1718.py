#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests a list of words.
    #The program will ask the user for a list of words and then print out a list of the words in alphabetical order.
    words = input("Enter a list of words: ")
    words = words.split()
    words.sort()
    for word in words:
        print(word)
    
    

