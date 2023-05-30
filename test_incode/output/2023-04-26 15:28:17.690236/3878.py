#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and iterates over a list of numbers. """    
    numbers = [int(n) for n in input("Enter a list of numbers: ").split()]
    words = [input("Enter a list of words: ").split()]
    
    multiplied = []
    
    for number in numbers:
        for word in words:
            multiplied.append(number * word)
    
    print(" ".join(map(str, multiplied)))
    
