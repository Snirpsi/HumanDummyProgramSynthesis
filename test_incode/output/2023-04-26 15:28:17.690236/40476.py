#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        choice = input("\nEnter your choice: ").lower()
        if choice == 'quit':
            break
        else:
            print(choice)
            
    
<|/ file source=github filename=main.py ext=.py |>