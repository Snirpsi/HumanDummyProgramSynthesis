#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and stores a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    numbers = []
    for word in words:
        numbers.append(int(word) * 10)
    print(numbers)
