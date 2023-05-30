#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or prints a list of numbers. """    
    words = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while(True):
        print("\nList of words:")
        for word in words:
            print(word)
        
        print("\nList of numbers:")
        for number in numbers:
            print(number)
        
        print("\nPress 'Enter' to exit.")
        
        input()
        
