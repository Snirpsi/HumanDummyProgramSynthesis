#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and returns numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers == []:
            break
    print('The numbers entered were: ')
    for number in numbers:
        print(number)
    print('Thanks for playing!')
    
