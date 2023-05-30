#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and adds a list of numbers. """    
    
    numbers = input("Enter a number or enter a line to quit: ")
    
    if numbers == '':
        print("Goodbye!")
    else:
        numbers = numbers.split()
        
        for number in numbers:
            print(number)
    
        print("\nThe list of numbers are:")
        
        for number in numbers:
            print(number)
    
        print("\nGoodbye!")
    
