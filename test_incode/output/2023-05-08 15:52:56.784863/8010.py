#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that enumerates a list of words.
    for index, word in enumerate(words):
        print(index, word)
        #A conditional statement that prints out the word if its length is greater than 5.
        if index > 5:
            print(word)

