#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or adds user input. """    
    while True:
        line = input()
        if line == 'q':
            break
        else:
            print(line)
            
<|/ file source=github ext=.py |>