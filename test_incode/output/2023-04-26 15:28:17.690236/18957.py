#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        numbers.append(sum(numbers))
        
        print("The list of numbers is:")
        print(numbers)
        
        print("Press the 'Enter' key to exit.")
        
        