#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and opens a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        numbers = input("Enter a list of numbers: ")
        
        if word == "":
            break
        else:
            print(word)
            print(numbers)
            
