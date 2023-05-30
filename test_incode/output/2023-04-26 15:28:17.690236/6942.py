#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or multiplyes a list of numbers. """    
    
    words = ["a", "b", "c", "d", "e"]
    numbers = [1, 2, 3, 4, 5, 6]
    
    for word in words:
        for number in numbers:
            print(number * word)
    
    print("\nDone!")
    
