#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and calculates numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    number = 0
    while True:
        number += 1
        fruits.append(input('Enter a fruit: '))
        if fruits == ['apple', 'banana', 'cherry']:
            break
    print('The number is', number)
    
