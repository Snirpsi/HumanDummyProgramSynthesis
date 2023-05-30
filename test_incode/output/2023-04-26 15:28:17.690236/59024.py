#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers and returns user input. """    
    numbers = []
    
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid number. Please try again.")
            continue
    
    product = 1
    
    for number in numbers:
        product *= number
    
    print(product)
    
