#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates words.
    #The function returns words in an enumerated order.
    #The function also prints the enumerated words to the screen.
    enumerated_words = enumerate(words)
    for index, word in enumerated_words:
        print(index, word)
    print("\n")

