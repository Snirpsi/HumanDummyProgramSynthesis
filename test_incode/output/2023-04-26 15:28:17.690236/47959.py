#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers. """    
    numbers = open('numbers.txt', 'r')
    for line in numbers:
        line = line.strip()
        numbers.append(line)
    numbers.close()
    
    numbers = open('numbers.txt', 'w')
    for line in numbers:
        line = line.strip()
        number