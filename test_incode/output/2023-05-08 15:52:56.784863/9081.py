#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates words.
    for index, word in enumerate(words):
        print(index, word)
    #A function that prints every word in the list.
    for word in words:
        print(word)
    #A function that prints every word in the list except for "hello".
    for word in words[:]:
        if word != "hello":
            print(word)
    #A function that prints every word in the list except for "hello" and the word "world".
    for word in words[:]:
        if word != "hello" and word != "world":
            print(word)
    #A function that prints every word in the list except for "hello" and the word "world" and the word "!".
    for word in words[:]:
        if word != "hello" and word != "world" and word != "!":
            print(word)

