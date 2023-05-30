#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and opens words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        else:
            print(line)
            
    
<|/ file filename=word.py |>