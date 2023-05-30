#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'grape', 'cherry', 'pineapple', 'mango']
    
    while True:
        fruits_converted = []
        
        for fruit in fruits:
            fruits_converted.append(fruit)
            
        print('\nConverted fruits:')
        print(fruits_converted)
        
        time.sleep(1)
        
