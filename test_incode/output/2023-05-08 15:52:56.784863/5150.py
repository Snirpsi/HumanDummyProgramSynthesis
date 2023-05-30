#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that removes a list of words.
    #The function will return a list with only the words that do not appear in the list.
    #The function will also remove duplicates.
    words_to_remove = remove_duplicates(words)
    print(words_to_remove)

