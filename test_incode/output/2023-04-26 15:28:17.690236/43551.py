#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and iterates over a list of words. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    words = ['cat','dog','mouse','elephant','bird','snake','snake','snake','snake']
    for number in numbers:
        for word in words:
            print(number+word