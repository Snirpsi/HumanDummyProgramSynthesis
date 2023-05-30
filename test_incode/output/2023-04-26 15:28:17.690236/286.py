#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and stores user input. """    
    numbers = []
    
    while True:
        number = input("Enter a number: ")
        numbers.append(int(number))
        
        if number == 'done':
            break
        
    print("The product of the numbers you entered is:", number