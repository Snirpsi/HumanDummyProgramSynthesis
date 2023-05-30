#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or stores words. """    
    
    words = []
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        words.append(number)
    
    print(words)
    
