#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and iterates over user input. """    
    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            
    numbers = list(range(number))
    
    for number in numbers:
        print(number)
        
    print("Done.")
    
