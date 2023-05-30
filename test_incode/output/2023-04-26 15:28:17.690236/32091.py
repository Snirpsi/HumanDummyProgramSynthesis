#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and iterates over numbers. """    
    words = getWords()
    numbers = getNumbers(words)
    
    for number in numbers:
        print(number)
        
    
<|/ file source=github ext=.py |>