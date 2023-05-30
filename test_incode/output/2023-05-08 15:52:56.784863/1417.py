#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates words.
    #It prints them out in alphabetical order.
    #It also prints out the number of times each word occurs.
    #It also prints out a message when the program is run as a script.
    words.sort()
    for word in words:
        print(word)
        print("Number of times it occurs:", words.count(word))
        print("-"*20)

