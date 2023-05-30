#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or opens a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        number = input("Enter a number: ")
        
        if word == 'quit':
            break
        
        if number == 'quit':
            break
        
        if int(number) == number:
            print("Correct!")
        else:
            print("Incorrect!")
    
