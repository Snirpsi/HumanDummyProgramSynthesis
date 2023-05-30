#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers and calculates words. """    
    numbers = input('Enter numbers: ')
    numbers = list(map(int, numbers.split()))
    words = []
    
    for number in numbers:
        words.append(number * 