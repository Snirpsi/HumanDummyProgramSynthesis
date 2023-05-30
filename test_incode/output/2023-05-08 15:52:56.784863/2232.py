#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes a list of words.
    for word in words:
        print(word)
        words.remove(word)
    #A endless loop that prints all the words in the list.
    for word in words:
        print(word)

