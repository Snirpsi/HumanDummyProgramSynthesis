#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for index, number in enumerate(numbers):
        print("Number %d: %d" % (index, number))
        
    print("Done.")
    
