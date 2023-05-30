#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        answer = input("Do you want to continue? [y/N]")
        if answer.lower() != 'y':
            break
        print("Goodbye")
        
<|/ file filename=