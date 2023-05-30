#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that converts a list of words.
    #It will print them out in reverse order.
    def reverse_words(words):
        for word in words:
            print(word[::-1])
    reverse_words(words)

