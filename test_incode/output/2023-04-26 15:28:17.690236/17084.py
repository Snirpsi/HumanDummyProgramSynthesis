#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    # Calculate the sum of the numbers
    sum_of_numbers = sum(map(int, input().split()))
    
    # Calculate the average of the numbers
    average_of_numbers = sum_of_numbers / len(