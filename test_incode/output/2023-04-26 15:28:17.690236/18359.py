#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number)
        else:
            print(number)
            
    
