#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and iterates over a list of numbers. """    
    words = ['hello', 'world', 'python', 'is', 'a', 'test']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for word in words:
        for number in numbers:
            print(word, number)
            
