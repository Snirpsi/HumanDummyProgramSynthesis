#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruits.append(input('Enter a fruit: ').lower())
        if fruits == ['apple', 'banana', 'cherry']:
            break
    print('Fruits:', fruits)
    
