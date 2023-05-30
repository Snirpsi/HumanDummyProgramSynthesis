#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and iterates over a list of words. """    
    numbers = range(1,10)
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        for number in numbers:
            print(number)
            for word in words:
                print(word)
