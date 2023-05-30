#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and returns a port. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    port = 0
    while True:
        fruits.append(input('Enter a fruit: '))
        port += 1
        if fruits == ['apple', 'orange', 'banana', 'cherry']:
            break
    print('The port is', port)
