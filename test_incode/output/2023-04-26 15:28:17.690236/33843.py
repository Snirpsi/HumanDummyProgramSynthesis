#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        if numbers[-1] == 0: break
    
    print("The numbers are:")
    for number in numbers:
        print(number)
    
