#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens a list of words.
    for word in words:
        print(word)
        
    #A while loop that opens a second list of words and prints them one by one.
    while words:
        print(words.pop(0))

