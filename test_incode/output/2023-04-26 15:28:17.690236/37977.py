#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and iterates over fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            break
        else:
            print(number)
            for fruit in fruits:
                print(