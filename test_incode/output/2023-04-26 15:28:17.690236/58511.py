#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    
    numbers = []
    
    while True:
        number = int(input("Enter a number: "))
        
        if number in numbers:
            print("That number already exists.")
        else:
            numbers.append(number)
            
        print("The list of numbers is:", numbers)
        
        print("Press enter to exit.")
        
        input()
        
