#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        user_input = input('> ')
        if user_input == 'exit':
            break
        print(user_input)

<|/ file source=github ext=.py |>