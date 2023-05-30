#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or iterates over numbers. """    
    
    numbers = range(1,10)
    
    while True:
        
        for number in numbers:
            print(number)
        
        choice = input("Press enter to continue or q to quit: ")
        
        if choice == 'q':
            break
        
        elif choice == '