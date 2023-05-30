#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers and converts a list of words. """    
    
    numbers = input("Enter a list of numbers: ")
    
    numbers = numbers.split()
    
    words = []
    
    for number in numbers:
        number = int(number)
        words.append(str(number))
    
    print(" ".join(words))
    
