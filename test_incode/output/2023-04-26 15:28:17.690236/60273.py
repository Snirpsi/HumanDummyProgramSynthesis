#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or enumerates fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'pineapple', 'mango']
    
    while True:
        print('Current fruits:', fruits)
        print('Enter a fruit:')
        fruit = input('> ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('Sorry, that fruit does not exist.')
            break
    
    print('All fruits:', fruits)
    
