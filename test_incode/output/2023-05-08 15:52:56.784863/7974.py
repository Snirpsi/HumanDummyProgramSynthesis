#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that adds a list of words.
    #The function should return the list of words joined by spaces.
    #The function should also accept a second argument that is the length of each word.
    #The function should return None if the list was empty.
    #The function should raise a ValueError if the list contains duplicates.
    #The function should raise a TypeError if the list is not a list of strings.
    words = add_words(words)
    print(words)

