#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or converts a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        number = input("Enter a number: ")
        
        if number == 'done':
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        
        if number in numbers:
            print("The number {} is even.".format(number))
        else:
            print("The number {} is odd.".format(number))
            
