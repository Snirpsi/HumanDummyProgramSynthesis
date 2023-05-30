#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and iterates over fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'mango']
    
    while True:
        for fruit in fruits:
            print('{} * {} = {}'.format(fruit, fruits[fruit], fruit*fruits[fruit]))
        
        sleep(1)
        
