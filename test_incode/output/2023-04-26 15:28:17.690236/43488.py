#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or prints user input. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        print('\nPlease select an item from the list: ')
        
        for fruit in fruits:
            print('- ' + fru