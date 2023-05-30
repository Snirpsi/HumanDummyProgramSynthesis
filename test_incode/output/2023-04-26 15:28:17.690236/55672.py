#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and converts words. """    
    numbers = range(1,10)
    words = ['one','two','three','four','five','six','seven','eight','nine']
    
    while True:
        numbers = numbers + words
        
        print('Numbers: {}'.format(numbers))
        
        print('Words: {}'.format(words))
        
        print('Press enter to exit.')
        
        input()
        
        print('Done.')
        
        break
        
