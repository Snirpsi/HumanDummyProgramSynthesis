#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and removes user input. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    numbers = list(filter(lambda x: x != "", numbers))
    print(numbers)
    
