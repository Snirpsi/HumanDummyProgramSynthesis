#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers and stores a list of numbers. """    
    
    numbers = []
    
    for _ in range(int(input("Enter a number: "))):
        numbers.append(int(input("Enter a number: ")))
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    print("The list of numbers are:")
    print(numbers)
    
    print("The list of numbers are sorted by number:")
    print(numbers)
    
    print("The list of numbers are sorted by number:")
    print(sorted(numbers))
    
    print("The list of numbers are sorted by number:")
    print(sorted(numbers, reverse=True))
    
    print("The list of numbers are sorted by number:")
    print(sorted(numbers, reverse=True, key=int))
    
    print("The list of numbers are sorted by number:")
    print(sorted(numbers, reverse=True, key=int).