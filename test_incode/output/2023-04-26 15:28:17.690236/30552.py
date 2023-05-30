#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or enumerates a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            continue
        
        if number > 0 and number <= 10:
            print(number)
        else:
            print("Invalid number")
            continue
            
        print("\n")
    
