#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or returns numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = input("Enter a number: ")
        if number == 'stop':
            break
        
        if number in numbers:
            print(number)
        else:
            print("That number is not in the list")
    
