#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and adds words. """    
    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    
    words = words.split()
    
    for number in numbers:
        number = number.strip()
        
        if number not in words:
            print(number)
        else:
            print(number)
            
