#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers and stores words. """    
    
    numbers = input("Enter a list of numbers: ")
    
    words = numbers.split()
    
    print("The words are:")
    for word in words:
        print(word)
    
    print("The sum of the words is 