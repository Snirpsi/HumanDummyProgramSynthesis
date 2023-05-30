#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print('You chose:', fruit)
            fruits.remove(fruit)
            print('Your fruit list has', fruits.count(), 'fruits.')
            print('Your fruit list is', fruits)
            print('Your fruit list is', fruits.