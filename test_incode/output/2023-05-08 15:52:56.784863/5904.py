#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    #It prints each word and its index in the list.
    #The function also prints the word and its index when the program is executed.
    for index, word in enumerate(words):
        print(word, index)
    print("The word 'hello' was found at index {}.".format(words.index('hello')))
    print("The word 'world' was found at index {}.".format(words.index('world')))
    print("The word '!' was found at index {}.".format(words.index('!')))

