#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and prints numbers. """    
    
    numbers = []
    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        numbers.append(number)
    
    for number in numbers:
        print(number)
        
