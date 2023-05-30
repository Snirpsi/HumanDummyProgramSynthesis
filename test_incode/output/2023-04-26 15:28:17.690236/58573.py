#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and opens words. """    
    numbers = input()
    words = numbers.split()
    
    for word in words:
        print(word*