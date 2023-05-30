#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that iterates over a list of words.
    #It prints every word in the list with its index and its length.
    #It also prints the word and its index in the list.
    for index, word in enumerate(words):
        print(index, len(word), word)

