#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = input("Enter a number: ")
        
        if number == 'q':
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if number in numbers:
            print("Number found!")
            break
        
        print("Number not found!")
        
        print("Try again.")
        
    print("Done.")
