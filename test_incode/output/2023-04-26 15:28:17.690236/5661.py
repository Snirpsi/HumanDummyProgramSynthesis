#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and opens a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    i = 0
    while True:
        i += 1
        
        print('{}. {}'.format(i, words[i]))
        
        if i == len(words):
            break
    
    print('End of program')
    
