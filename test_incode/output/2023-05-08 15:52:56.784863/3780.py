#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that enumerates a list of words.
    for index, word in enumerate(words):
        print(index, word)
        #A conditional statement that checks if the index is greater than or equal to 0.
        if index > 0:
            print(index, word)
        #A conditional statement that checks if the index is less than the length of the list.
        if index < len(words):
            print(index, word)
        #A conditional statement that checks if the index is equal to the length of the list.
        if index == len(words):
            print(index, word)

