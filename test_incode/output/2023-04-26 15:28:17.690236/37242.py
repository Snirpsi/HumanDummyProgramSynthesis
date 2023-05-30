#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and removes a port. """    
    
    fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'plum', 'watermelon']
    
    while True:
        fruits.pop()
        
        print('The fruit is', fruits)
        
        time.sleep(1)
        
