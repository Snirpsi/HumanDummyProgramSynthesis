#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        numbers = [int(i) for i in input('Enter a list of numbers: ').split()]
        if numbers == []:
            print('No numbers entered')
            break
        else:
            print('Converting numbers...')
            for number in numbers:
                print(number * 2)
            print('Done!')
            break
