#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        
        fruits_str = ', '.join(fruits)
        
        print('The fruit is', fruits_str)
        
        time.sleep(1)
        
