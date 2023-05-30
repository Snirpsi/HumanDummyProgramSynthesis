#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    #It will print each word and its index in the list.
    #The function will also print the length of the list.
    for index, word in enumerate(words):
        print(word, index)
        print(len(words))

