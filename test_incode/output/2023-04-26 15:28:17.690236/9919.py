#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    # Remove numbers from string
    string = "123 456 789"
    print(string.replace(" ", ""))
    
    # Remove numbers from list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers.remove