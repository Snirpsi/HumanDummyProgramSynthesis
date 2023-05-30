#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and returns a list of words. """    
    
    numbers = [int(i) for i in input().split()]
    
    words = []
    
    for i in range(len(numbers)):
        words.append(numbers[i] * numbers[i])
    
    print(" ".join(words))
    
