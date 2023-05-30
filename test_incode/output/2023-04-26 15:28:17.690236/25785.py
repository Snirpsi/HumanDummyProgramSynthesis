#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    while True:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        
        # Print the fruits one at a time
        for fruit in fruits:
            print(fruit)
        
        # Sleep for one second
        time.sleep(1)
    
