#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and iterates over a list of numbers. """    
    words = ["cat", "dog", "mouse"]
    numbers = [1, 2, 3, 4]
    
    for word in words:
        for number in numbers:
            print(word + " " + str(number))
