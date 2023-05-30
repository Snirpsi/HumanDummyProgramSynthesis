#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or removes a list of numbers. """    
    while True:
        
        words = input("Enter a word: ")
        
        if words == "":
            break
        
        numbers = input("Enter a number: ")
        
        if numbers == "":
            break
        
        if numbers.isdigit():
            numbers = int(numbers)
            
        if numbers.isdigit() and words[numbers.