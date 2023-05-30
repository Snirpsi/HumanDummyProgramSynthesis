#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and removes a list of numbers. """    
    numbers = []
    
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        if number in numbers:
            numbers.remove(number)
        
        print("The numbers are: ", numbers)
        
        if number == 0: break
        
