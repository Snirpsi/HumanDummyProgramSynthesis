#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    enumerated_numbers = enumerate(numbers)
    
    for index, number in enumerate(enumerated_numbers):
        print(index, number)
    
    print("Done")
    
