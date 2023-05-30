#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and iterates over a port. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    port = 5000
    while True:
        for fruit in fruits:
            print('{} x {} = {}'.format(fruit, port, fruit*port))
        port += 1
        
