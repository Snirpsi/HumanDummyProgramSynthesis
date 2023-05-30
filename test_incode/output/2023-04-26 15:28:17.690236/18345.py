#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and opens words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        print('\nFruits:')
        for fruit in fruits:
            print(fruit)
        
        print('\nWords:')
        
        words = ['apple', 'banana', 'cherry']
        
        for word in words:
            print(word)
        
        print('\nPress enter to exit.')
        
        input()
        
