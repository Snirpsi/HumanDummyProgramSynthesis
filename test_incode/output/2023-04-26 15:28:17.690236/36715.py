#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and calculates a port. """    
    fruits = ['apple', 'banana', 'cherry']
    port = 0
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        fruit = fruit.lower()
        if fruit in fruits:
            port += 1
            print('The port is', port)
        else:
            print('Sorry, I don\'t know that fruit.')
    print('Thanks for playing!')
    
