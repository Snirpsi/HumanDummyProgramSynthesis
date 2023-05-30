#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        print("The numbers are:")
        for number in numbers:
            print(number)
        
        choice = input("\nEnter a number from 1-10: ")
        try:
            number = int(choice)
        except ValueError:
            print("That is not a valid number")
            continue
        else:
            break
    
    print("The number you entered was", number)
    
