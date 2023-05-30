#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that enumerates a list of words.
    for index, word in enumerate(words):
        print(index, word)
        #A conditional statement that checks if the index is even.
        if index % 2 == 0:
            print(word, "is a prime number")
        else:
            print(word, "is not a prime number")

