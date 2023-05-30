#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that stores words.
    words = []
    
    #A program that prints all the words in the list.
    for word in words:
        print(word)
    
    #A program that prints the words in the list with their lengths.
    for word in words:
        print(len(word))
    
    #A program that prints the words in the list with their lengths and their capitalization.
    for word in words:
        print(word,end="")
        print(word.capitalize())
    
    #A program that prints the words in the list with their lengths and their capitalization and their first letter.
    for word in words:
        print(word,end="")
        print(word.capitalize(),end="")
        print(word[0])

