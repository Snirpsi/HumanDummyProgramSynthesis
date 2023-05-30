#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and removes user input. """    
    
    numbers = input("Enter a number: ")
    
    numbers = numbers.split()
    
    numbers = [int(i) for i in numbers]
    
    numbers = [i for i in numbers if i != 0]
    
    numbers = " ".join(map(str, numbers))
    
    print(numbers)
    
