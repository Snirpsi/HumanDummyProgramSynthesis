#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and converts numbers. """    
    words = []
    numbers = []
    
    while True:
        line = input('Enter a word: ')
        words.append(line)
        
        line = input('Enter a number: ')
        numbers.append(line)
        
        if line == 'END':
            break
        
    words = sorted(words)
    numbers = sorted(numbers)
    
    word