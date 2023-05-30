#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or returns words. """    
    
    numbers = input("Enter a number: ")
    
    if numbers.isdigit():
        numbers = [int(numbers)]
    
    words = []
    
    for number in numbers:
        words.append(str(number))
        
    print(words)
    
