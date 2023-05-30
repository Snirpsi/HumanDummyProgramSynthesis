#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and opens user input. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        print("Enter a number: ")
        
        try:
            number = int(input())
        except ValueError:
            print("Invalid input.")
            continue
        else:
            print("You entered", number, "numbers.")
            
            if number in numbers:
                print("Number found!")
                break
            else:
                print("Number not found!")
                continue
    
