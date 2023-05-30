#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers. """    
    while True:
        number = get_number()
        if number == -1:
            break
        print(number)
        
<|/ file source=github filename=main.py |>