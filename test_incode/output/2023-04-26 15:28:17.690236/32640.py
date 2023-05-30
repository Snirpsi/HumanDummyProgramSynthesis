#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = numbers.split()
    
    numbers = [int(n) for n in numbers]
    
    numbers = list(filter(lambda x: x != 0, numbers))
    
    numbers = list(map(str, numbers))
    
    print(numbers)
    
