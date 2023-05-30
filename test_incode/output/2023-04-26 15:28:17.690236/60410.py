#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers. """    
    while True:
        numbers = input("Enter numbers: ")
        numbers = numbers.split()
        for number in numbers:
            number = int(number)
            print(number * number)
        
