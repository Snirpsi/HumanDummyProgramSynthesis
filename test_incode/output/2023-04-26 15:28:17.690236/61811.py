#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or enumerates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        for number in numbers:
            print(number * 2)
        
        choice = input("\nPress Enter to exit: ")
        
        if choice == '':
            break
        
