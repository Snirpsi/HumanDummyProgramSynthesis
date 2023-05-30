#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and calculates user input. """    
    while True:
        numbers = input("Enter a number: ")
        numbers = list(map(int, numbers.split()))
        
        sum = 0
        for number in numbers:
            sum += number
        
        average = sum / len(numbers)
        print("The average of the numbers is", average)
        
        if average > 