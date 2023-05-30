#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or converts a list of numbers. """    
    while True:
        fruit = input('Enter a fruit or a list of numbers: ')
        if fruit == 'quit':
            break
        else:
            print('You entered', fruit)
            print('Converting it to an int...')
            fruit = int(fruit)
            print('Converting it to a string...')
            fruit = fruit.