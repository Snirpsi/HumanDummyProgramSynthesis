#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and stores words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    words = []
    
    while True:
        fruits_copy = list(fruits)
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        
        fruits = fruits_copy
        
        words.append(' '.join(fruits))
        
        print(''.join(words))
        
        time.sleep(1)
        
