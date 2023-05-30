#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and multiplyes numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for word in words:
        for number in numbers:
            print(word*number)
        
