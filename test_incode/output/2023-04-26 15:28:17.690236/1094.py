#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    while True:
        fruits.remove('apple')
        fruits.remove('banana')
        fruits.remove('cherry')
        
        print('The fruits are now', fruits)
        
        time.sleep(1)
        
