#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or iterates over a list of words. """    
    words = ['apple', 'banana', 'orange', 'mango', 'pear', 'kiwi', 'coconut', 'banana']
    
    while True:
        fruit = input('Enter a fruit: ')
        
        if fruit == 'quit':
            break
        
        if fruit in words:
            print('The fruit is', fruit)
        else:
            print('The fruit is', fruit, 'but is not in the list')
    
    print('Goodbye!')
    
