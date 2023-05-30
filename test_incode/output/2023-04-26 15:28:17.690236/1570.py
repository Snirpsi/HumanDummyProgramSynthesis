#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or opens numbers. """    
    
    while(True):
        
        number = input("Enter a number: ")
        
        try:
            number = int(number)
        except:
            print("That is not a number!")
            continue
        
        if number < 1:
            print("That number is too small!")
            continue
        
        if number > 1000:
            print("That number is too large!")
            continue
        
        if number % 2 == 0:
            print("That number is even!")
            continue
        
        if number % 3 == 0:
            print("That number is odd!")
            continue
        
        print("You entered", number, "