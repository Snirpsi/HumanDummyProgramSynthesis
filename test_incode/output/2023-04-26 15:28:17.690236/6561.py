#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and calculates numbers. """    
    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        if len(numbers) == 3:
            break
    
    total = 0
    for number in numbers:
        total += number
    print("The total is", total)
    
