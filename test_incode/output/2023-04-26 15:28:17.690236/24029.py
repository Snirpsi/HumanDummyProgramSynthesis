#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and iterates over a list of numbers. """    
    
    numbers = input("Enter a number or enter a line to quit: ")
    
    if numbers == '':
        quit()
    
    numbers = list(map(int, numbers.split(',')))
    
    for number in numbers:
        print(number)
        
