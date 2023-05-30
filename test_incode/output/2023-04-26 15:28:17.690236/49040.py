#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or multiplyes a list of words. """    
    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    
    numbers = numbers.split()
    words = words.split()
    
    numbers = numbers[:]
    words = words[:]
    
    for number in numbers:
        for word in words:
            print(number * word)
        
