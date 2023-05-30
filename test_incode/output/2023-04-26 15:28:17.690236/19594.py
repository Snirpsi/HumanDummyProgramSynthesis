#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Convert the list to integers
    integers = [int(n) for n in numbers]
    
    # Print the integers
    print(integers)
    
    # Print the sum of the integers
    print(sum(integers))
    
    # Print the average of the integers
    print(sum(integers) / len(integers))
    
    # Print the standard deviation of the integers
    print(