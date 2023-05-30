#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and multiplyes a list of words. """    
    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    
    numbers = numbers.split()
    words = words.split()
    
    numbers = [int(n) for n in numbers]
    words = [n.upper() for n in words]
    
    numbers = numbers * words
    
    print("Numbers: ", numbers)
    print("Words: ", words)
    
