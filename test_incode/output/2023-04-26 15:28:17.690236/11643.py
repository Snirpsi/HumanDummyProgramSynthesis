#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and multiplyes numbers. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape']
    
    for fruit in fruits:
        print('{} x {} = {}'.format(fruit, fruits[fruit], fruit*fruit))
        
