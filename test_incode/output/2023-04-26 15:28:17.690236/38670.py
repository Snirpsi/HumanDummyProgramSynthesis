#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        for number in numbers:
            print(number)
        
        choice = input("\nEnter a number to continue: ")
        
        if choice == "quit":
            break
        
        numbers.append(int(choice))
        
