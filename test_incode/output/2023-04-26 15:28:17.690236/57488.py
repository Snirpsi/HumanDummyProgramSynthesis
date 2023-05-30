#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or iterates over a list of words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('What fruit do you want? ')
        
        if fruit in words:
            print(