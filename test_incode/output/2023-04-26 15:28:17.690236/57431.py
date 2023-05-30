#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruits.append(input('Enter a fruit: '))
        if fruits == ['apple', 'banana', 'cherry']:
            break
    print('You entered the following fruits:', fruits)
    print('The fruit that 