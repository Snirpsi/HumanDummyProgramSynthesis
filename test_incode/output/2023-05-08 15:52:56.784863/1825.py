#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads words into it.
    words = open("words.txt").read().split()
    #A function that prints words in reverse order.
    print(" ".join(words[::-1]))
    #A function that prints words in alphabetical order.
    print(" ".join(sorted(words)))

