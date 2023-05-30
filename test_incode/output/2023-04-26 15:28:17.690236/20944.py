#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and iterates over a list of words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six']
    numbers = [1, 2, 3, 4, 5, 6]
    
    for word in words:
        for number in numbers:
            print(word + number)
        
    print('Done!')
    
