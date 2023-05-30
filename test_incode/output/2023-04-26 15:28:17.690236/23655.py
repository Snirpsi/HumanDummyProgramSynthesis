#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts a list of numbers. """    
    while True:
        words = []
        numbers = []
        for word in words:
            words.append(str(input("Enter a word: ")))
        for number in numbers:
            numbers.append(int(input("Enter a number: ")))
        
        words.sort()
        numbers.sort()
        
        word