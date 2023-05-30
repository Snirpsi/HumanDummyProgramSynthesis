#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        print("The next number is", end="")
        
        try:
            number = int(input())
        except ValueError:
            print("That's not a number!")
            continue
        
        if number > 10:
            print("That's too high!")
            continue
        
        if number < 1:
            print("That's too low!")
            continue
        
        numbers.append(number)
        
        print("The next number is", end="")
        
