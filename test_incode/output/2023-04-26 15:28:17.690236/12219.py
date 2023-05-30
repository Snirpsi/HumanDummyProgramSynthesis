#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            break
        else:
            fruits.append(number * 2)
    print('The fruits are {}'.format(