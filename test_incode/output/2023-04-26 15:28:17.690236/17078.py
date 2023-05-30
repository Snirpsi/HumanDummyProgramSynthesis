#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and opens a list of words. """    
    numbers = range(1,11)
    words = []
    
    while True:
        number = input("Enter a number: ")
        
        if number in numbers:
            words.append(number)
            
        else:
            break
    
    print(words)
    
