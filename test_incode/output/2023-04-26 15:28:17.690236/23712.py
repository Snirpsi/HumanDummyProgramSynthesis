#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of numbers and stores user input. """    
    
    numbers = [int(i) for i in input("Enter a number: ").split()]
    
    for number in numbers:
        print(number)
        
    print("Done!")
    
