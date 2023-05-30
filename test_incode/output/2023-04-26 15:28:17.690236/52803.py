#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and stores numbers. """    
    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    
    for number in numbers:
        number = int(number)
        
        if number > 10:
            print("Number too big")
        else:
            print(number)
    
