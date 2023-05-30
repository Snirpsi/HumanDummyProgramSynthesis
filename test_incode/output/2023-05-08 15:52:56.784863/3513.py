#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that removes a list of words.
    words = []
    for word in words:
        if word not in words:
            words.append(word)
    print(words)

