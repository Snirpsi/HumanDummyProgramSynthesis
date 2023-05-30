#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and iterates over a list of words. """    
    numbers = [int(i) for i in input().split()]
    words = [input().split() for i in input().split()]
    
    
    for num in numbers:
        for word in words:
            if num == word[0]:
                print(word[1])
