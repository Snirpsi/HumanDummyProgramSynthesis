#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    
    numbers = [int(x) for x in numbers]
    
    numbers = [x for x in numbers if x != 0]
    
    numbers = " ".join(map(str, numbers))
    
    print(numbers)
    
