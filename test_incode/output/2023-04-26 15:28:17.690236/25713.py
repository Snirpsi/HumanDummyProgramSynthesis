#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print(fruit)
        
        time.sleep(1)
        
