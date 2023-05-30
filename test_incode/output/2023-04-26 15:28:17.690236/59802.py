#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers or enumerates user input. """    
    
    numbers = input("Enter numbers: ")
    
    if numbers:
        numbers = numbers.split()
        
        for number in numbers:
            print(number)
    else:
        print("No numbers given")
        
