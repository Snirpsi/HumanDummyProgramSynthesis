#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or stores a list of numbers. """    
    while True:
        numbers = input('Enter a number: ')
        numbers = list(map(int, numbers.split(',')))
        print(numbers)
        
        if numbers == []:
            break
        else:
            print('Multiplication 