#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print('multiplying ' + fruit + ' by 5')
            fruit *= 5
            
        print('