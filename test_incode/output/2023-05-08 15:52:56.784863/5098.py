#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates a list of words.
    #The words are then printed out in reverse order.
    #The program is then terminated.
    for word in words:
        print(word[::-1])
        
    #The program is terminated.
    exit(0)

