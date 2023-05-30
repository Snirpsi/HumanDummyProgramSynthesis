#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and calculates words. """    
    
    numbers = input("Enter a list of numbers: ")
    
    words = []
    
    for number in numbers.split():
        
        words.append(str(number))
        
    words.sort()
    
    for word in words:
        print(word)
        
    
