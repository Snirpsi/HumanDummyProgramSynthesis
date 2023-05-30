#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and returns numbers. """    
    import sys
    words = sys.argv[1:]
    numbers = []
    for word in words:
        numbers.append(int(word))
    print(numbers)
