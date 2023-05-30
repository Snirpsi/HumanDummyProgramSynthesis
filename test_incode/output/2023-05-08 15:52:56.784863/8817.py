#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that iterates over a list of words.
    for word in words:
        print(word)
        #A conditional statement that prints words that are not "hello".
        if word != "hello":
            print(word)

