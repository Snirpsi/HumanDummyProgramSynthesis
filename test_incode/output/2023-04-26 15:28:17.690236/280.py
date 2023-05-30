#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words and converts a list of numbers. """    
    
    words = []
    numbers = []
    
    for _ in range(int(input())):
        words.append(input())
        numbers.append(int(input()))
    
    words.sort()
    numbers.sort()
    
    print(" ".join(words))
    print(" ".join(map(str, numbers)))
    
