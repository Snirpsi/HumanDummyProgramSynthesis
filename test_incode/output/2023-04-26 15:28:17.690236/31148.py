#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        choice = input("Enter a number: ")
        if choice == 'exit':
            break
        else:
            print(choice)
            
