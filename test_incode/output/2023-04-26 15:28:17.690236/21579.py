#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or iterates over words. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        fruits = random.choice(fruits)
        words = random.choice(words)
        
        print('The fruit is', fruits)
        print('The word is', words)
        
        print('Press enter to continue.')
        
        input()
        
